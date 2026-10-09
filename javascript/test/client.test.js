import test from "node:test";
import assert from "node:assert/strict";
import {
  BBBClient, CrawloraClientError, CrawloraNetworkError,
  CrawloraServerError, groups, operations, operationCount
} from "../src/index.js";

const json = (data, status = 200, headers = {}) => new Response(JSON.stringify(data), {
  status, headers: { "content-type": "application/json", ...headers }
});

test("exports only this platform and exposes direct and grouped methods", async () => {
  const client = new BBBClient({ apiKey: "test-key", fetch: async () => json({ ok: true }) });
  assert.equal(operationCount, Object.keys(operations).length);
  assert.deepEqual(Object.keys(groups), ["bbb"]);
  assert.equal(typeof client["business"], "function");
  assert.equal(typeof client["bbb"]["business"], "function");
});

test("serializes required query/path values, adds API key and platform User-Agent", async () => {
  let seen;
  const client = new BBBClient({ apiKey: "secret", fetch: async (url, init) => {
    seen = { url: String(url), headers: init.headers };
    return json({ ok: true });
  } });
  await client.request("bbb-business", {"url": "sample"});
  assert.match(seen.url, /\/bbb\/business/);
  assert.equal(seen.headers["x-api-key"], "secret");
  assert.equal(seen.headers["user-agent"], "crawlora-bbb-js/0.1.1");
});

test("allows caller User-Agent override and response text mode", async () => {
  let seen;
  const client = new BBBClient({ apiKey: "key", userAgent: "custom-agent", fetch: async (_url, init) => {
    seen = init.headers;
    return new Response("caption text", { headers: { "content-type": "text/plain" } });
  } });
  const result = await client.request("bbb-business", {"url": "sample"}, { responseType: "text" });
  assert.equal(seen["user-agent"], "custom-agent");
  assert.equal(result, "caption text");

  const rawFeed = "1~home|2~away\n";
  const autoClient = new BBBClient({ fetch: async () => new Response(rawFeed, {
    headers: { "content-type": "text/plain" }
  }) });
  assert.equal(await autoClient.request("bbb-business", {"url": "sample"}), rawFeed);
});

test("maps API errors and retries server failures", async () => {
  let calls = 0;
  const client = new BBBClient({ apiKey: "key", retries: 1, retryDelay: 0, fetch: async () => {
    calls++;
    return calls === 1 ? json({ msg: "try again" }, 503) : json({ ok: true });
  } });
  assert.deepEqual(await client.request("bbb-business", {"url": "sample"}), { ok: true });
  assert.equal(calls, 2);

  const bad = new BBBClient({ fetch: async () => json({ msg: "bad input" }, 400) });
  await assert.rejects(bad.request("bbb-business", {"url": "sample"}), CrawloraClientError);
  const down = new BBBClient({ fetch: async () => json({ msg: "down" }, 503) });
  await assert.rejects(down.request("bbb-business", {"url": "sample"}), CrawloraServerError);
});

test("reports timeout and caller cancellation as network errors", async () => {
  const hanging = (_url, { signal }) => new Promise((_resolve, reject) => {
    signal.addEventListener("abort", () => reject(new Error("aborted")), { once: true });
  });
  const timed = new BBBClient({ timeout: 5, fetch: hanging });
  await assert.rejects(timed.request("bbb-business", {"url": "sample"}), CrawloraNetworkError);

  const controller = new AbortController();
  const aborted = new BBBClient({ fetch: hanging });
  const pending = aborted.request("bbb-business", {"url": "sample"}, { signal: controller.signal });
  controller.abort();
  await assert.rejects(pending, CrawloraNetworkError);
});

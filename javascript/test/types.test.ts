import { BBBClient } from "../src/index.js";

const client = new BBBClient({ apiKey: "test-key" });
void client.article({"url": "sample"});
void client.request("bbb-article", {"url": "sample"});
const streamResponse: Promise<Response> = client.request("bbb-article", {"url": "sample"}, { responseType: "stream" });
const operationStream: Promise<Response> = client.operation("bbb-article", {"url": "sample"}, { responseType: "stream" });
const directStream: Promise<Response> = client.article({"url": "sample"}, { responseType: "stream" });
void streamResponse; void operationStream; void directStream;
void client.request("bbb-article", {"url": "sample"}, { responseType: "text" });
const rawText: Promise<string> = client.request("bbb-article", {"url": "sample"}, { responseType: "text" });
void rawText;


void client.regions();
void client.request("bbb-regions");
// @ts-expect-error The selected operation requires its documented params.
void client.article();

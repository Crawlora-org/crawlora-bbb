import { BBBClient } from "../src/index.js";

const client = new BBBClient({ apiKey: "test-key" });
void client.business({"url": "sample"});
void client.request("bbb-business", {"url": "sample"});
const streamResponse: Promise<Response> = client.request("bbb-business", {"url": "sample"}, { responseType: "stream" });
const operationStream: Promise<Response> = client.operation("bbb-business", {"url": "sample"}, { responseType: "stream" });
const directStream: Promise<Response> = client.business({"url": "sample"}, { responseType: "stream" });
void streamResponse; void operationStream; void directStream;
void client.request("bbb-business", {"url": "sample"}, { responseType: "text" });
const rawText: Promise<string> = client.request("bbb-business", {"url": "sample"}, { responseType: "text" });
void rawText;


void client.scamtrackerSearch();
void client.request("bbb-scamtracker-search");
// @ts-expect-error The selected operation requires its documented params.
void client.business();

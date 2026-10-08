import { BBBClient } from "../javascript/src/index.js";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new BBBClient({ apiKey });

  const search = await client.search({ query: "coffee", location: "New York, NY" });
  console.log("search", search);
  const business = await client.business({ url: "https://www.bbb.org/us/tx/austin/profile/plumber/calixto-plumbing-0825-1000223803" });
  console.log("business", business);
  const scamtrackerSearch = await client.scamtrackerSearch({ query: "package delivery", state: "NY" });
  console.log("scamtrackerSearch", scamtrackerSearch);

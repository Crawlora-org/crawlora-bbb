import { groups } from "./operations.js";
import {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
} from "./client.js";

export class BBBClient extends CrawloraClient {
  constructor(options = {}) {
    super({ ...options, userAgent: options.userAgent ?? "crawlora-bbb-js/0.1.0" });
    this["business"] = (...args) => this.request("bbb-business", ...args);
    this["businessComplaints"] = (...args) => this.request("bbb-business-complaints", ...args);
    this["businessMoreInfo"] = (...args) => this.request("bbb-business-more-info", ...args);
    this["businessReviews"] = (...args) => this.request("bbb-business-reviews", ...args);
    this["category"] = (...args) => this.request("bbb-category", ...args);
    this["scamtrackerSearch"] = (...args) => this.request("bbb-scamtracker-search", ...args);
    this["scamtrackerStateStats"] = (...args) => this.request("bbb-scamtracker-state-stats", ...args);
    this["scamtrackerDetail"] = (...args) => this.request("bbb-scamtracker-detail", ...args);
    this["search"] = (...args) => this.request("bbb-search", ...args);
  }
}

export { BBBClient as Client };
export {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
};
export { groups, operations, operationCount, OperationIds } from "./operations.js";
export const VERSION = "0.1.0";
export default BBBClient;

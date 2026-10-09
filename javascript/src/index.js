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
    super({ ...options, userAgent: options.userAgent ?? "crawlora-bbb-js/0.2.0" });
    this["article"] = (...args) => this.request("bbb-article", ...args);
    this["business"] = (...args) => this.request("bbb-business", ...args);
    this["businessComplaints"] = (...args) => this.request("bbb-business-complaints", ...args);
    this["businessMoreInfo"] = (...args) => this.request("bbb-business-more-info", ...args);
    this["businessReviews"] = (...args) => this.request("bbb-business-reviews", ...args);
    this["category"] = (...args) => this.request("bbb-category", ...args);
    this["localBbb"] = (...args) => this.request("bbb-local-bbb", ...args);
    this["localBbbs"] = (...args) => this.request("bbb-local-bbbs", ...args);
    this["news"] = (...args) => this.request("bbb-news", ...args);
    this["newsTopics"] = (...args) => this.request("bbb-news-topics", ...args);
    this["regions"] = (...args) => this.request("bbb-regions", ...args);
    this["scamtrackerSearch"] = (...args) => this.request("bbb-scamtracker-search", ...args);
    this["scamtrackerStateStats"] = (...args) => this.request("bbb-scamtracker-state-stats", ...args);
    this["scamtrackerDetail"] = (...args) => this.request("bbb-scamtracker-detail", ...args);
    this["search"] = (...args) => this.request("bbb-search", ...args);
    this["searchFilters"] = (...args) => this.request("bbb-search-filters", ...args);
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
export const VERSION = "0.2.0";
export default BBBClient;

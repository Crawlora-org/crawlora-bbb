import type {
  CrawloraGeneratedGroups,
  OperationId,
  OperationParamsMap,
  OperationRequestArgs,
  OperationResponseMap
} from "./types.js";

export type CrawloraParams = Record<string, unknown>;
export type CrawloraLogEvent = { event: string; [key: string]: unknown };
export interface CrawloraRequestContext { operationId: string; method: string; url: string; headers: Record<string, string> }
export type CrawloraBeforeRequest = (ctx: CrawloraRequestContext) => void | Promise<void>;
export type CrawloraAfterResponse = (operationId: string, status: number, headers: Record<string, string>, body: unknown) => unknown;

export interface CrawloraClientOptions {
  apiKey?: string;
  jwtToken?: string;
  baseUrl?: string;
  timeout?: number;
  retries?: number;
  retryDelay?: number;
  maxRetryDelay?: number;
  retryStatuses?: Iterable<number>;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
  onRetry?: (attempt: number, error: CrawloraError, delay: number) => void;
  requestId?: boolean;
  idempotencyKeys?: boolean;
  rateLimit?: number;
  maxConcurrency?: number;
  logger?: (event: CrawloraLogEvent) => void;
  beforeRequest?: CrawloraBeforeRequest | Iterable<CrawloraBeforeRequest>;
  afterResponse?: CrawloraAfterResponse | Iterable<CrawloraAfterResponse>;
  headers?: Record<string, string>;
  userAgent?: string | false;
  fetch?: typeof globalThis.fetch;
}

export interface CrawloraRequestOptions {
  headers?: Record<string, string>;
  responseType?: "auto" | "json" | "text" | "stream";
  timeout?: number;
  signal?: AbortSignal;
  retries?: number;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
}

export interface OperationDefinition {
  id: string; method: string; path: string; pathParams: string[];
  queryParams: Array<{ name: string; in?: "query"; collectionFormat?: string; type?: string; required?: boolean; enum?: string[] }>;
  formParams: Array<{ name: string; in?: "formData"; type?: string; required?: boolean; enum?: string[] }>;
  bodyParam?: string; bodyRequired?: boolean; consumes: string[]; produces: string[]; security: string[];
  paginatable?: boolean; cursorParams?: string[];
}

export class CrawloraError extends Error {
  status: number; code?: number; body: unknown; headers: Record<string, string>;
  response?: Response; cause?: unknown; retryable?: boolean; requestId?: string;
}
export class CrawloraClientError extends CrawloraError {}
export class CrawloraServerError extends CrawloraError {}
export class CrawloraNetworkError extends CrawloraError {}

export interface CrawloraPaginateOptions extends CrawloraRequestOptions {
  pageParam?: string; cursorParam?: string; nextCursor?: (page: unknown) => unknown;
  start?: unknown; step?: number; maxPages?: number;
}
export interface CrawloraPaginateItemsOptions extends CrawloraPaginateOptions {
  items?: (page: unknown) => Iterable<unknown>;
}

export class CrawloraClient {
  constructor(options?: CrawloraClientOptions);
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  paginate<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateOptions): AsyncGenerator<OperationResponseMap[I], void, unknown>;
  paginateItems<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateItemsOptions): AsyncGenerator<unknown, void, unknown>;
  [group: string]: unknown;
}
export interface CrawloraClient extends CrawloraGeneratedGroups {}

export class BBBClient extends CrawloraClient {
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  article(params: OperationParamsMap["bbb-article"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  business(params: OperationParamsMap["bbb-business"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  businessComplaints(params: OperationParamsMap["bbb-business-complaints"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  businessMoreInfo(params: OperationParamsMap["bbb-business-more-info"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  businessReviews(params: OperationParamsMap["bbb-business-reviews"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  category(params: OperationParamsMap["bbb-category"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  localBbb(params: OperationParamsMap["bbb-local-bbb"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  localBbbs(params: OperationParamsMap["bbb-local-bbbs"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  news(params: OperationParamsMap["bbb-news"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  newsTopics(params: OperationParamsMap["bbb-news-topics"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  regions(params?: OperationParamsMap["bbb-regions"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  scamtrackerSearch(params?: OperationParamsMap["bbb-scamtracker-search"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  scamtrackerStateStats(params?: OperationParamsMap["bbb-scamtracker-state-stats"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  scamtrackerDetail(params: OperationParamsMap["bbb-scamtracker-detail"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  search(params: OperationParamsMap["bbb-search"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  searchFilters(params?: OperationParamsMap["bbb-search-filters"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  article(params: OperationParamsMap["bbb-article"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  business(params: OperationParamsMap["bbb-business"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  businessComplaints(params: OperationParamsMap["bbb-business-complaints"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  businessMoreInfo(params: OperationParamsMap["bbb-business-more-info"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  businessReviews(params: OperationParamsMap["bbb-business-reviews"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  category(params: OperationParamsMap["bbb-category"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  localBbb(params: OperationParamsMap["bbb-local-bbb"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  localBbbs(params: OperationParamsMap["bbb-local-bbbs"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  news(params: OperationParamsMap["bbb-news"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  newsTopics(params: OperationParamsMap["bbb-news-topics"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  regions(params?: OperationParamsMap["bbb-regions"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  scamtrackerSearch(params?: OperationParamsMap["bbb-scamtracker-search"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  scamtrackerStateStats(params?: OperationParamsMap["bbb-scamtracker-state-stats"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  scamtrackerDetail(params: OperationParamsMap["bbb-scamtracker-detail"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  search(params: OperationParamsMap["bbb-search"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  searchFilters(params?: OperationParamsMap["bbb-search-filters"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;

  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  article(...args: OperationRequestArgs<"bbb-article">): Promise<OperationResponseMap["bbb-article"]>;
  business(...args: OperationRequestArgs<"bbb-business">): Promise<OperationResponseMap["bbb-business"]>;
  businessComplaints(...args: OperationRequestArgs<"bbb-business-complaints">): Promise<OperationResponseMap["bbb-business-complaints"]>;
  businessMoreInfo(...args: OperationRequestArgs<"bbb-business-more-info">): Promise<OperationResponseMap["bbb-business-more-info"]>;
  businessReviews(...args: OperationRequestArgs<"bbb-business-reviews">): Promise<OperationResponseMap["bbb-business-reviews"]>;
  category(...args: OperationRequestArgs<"bbb-category">): Promise<OperationResponseMap["bbb-category"]>;
  localBbb(...args: OperationRequestArgs<"bbb-local-bbb">): Promise<OperationResponseMap["bbb-local-bbb"]>;
  localBbbs(...args: OperationRequestArgs<"bbb-local-bbbs">): Promise<OperationResponseMap["bbb-local-bbbs"]>;
  news(...args: OperationRequestArgs<"bbb-news">): Promise<OperationResponseMap["bbb-news"]>;
  newsTopics(...args: OperationRequestArgs<"bbb-news-topics">): Promise<OperationResponseMap["bbb-news-topics"]>;
  regions(...args: OperationRequestArgs<"bbb-regions">): Promise<OperationResponseMap["bbb-regions"]>;
  scamtrackerSearch(...args: OperationRequestArgs<"bbb-scamtracker-search">): Promise<OperationResponseMap["bbb-scamtracker-search"]>;
  scamtrackerStateStats(...args: OperationRequestArgs<"bbb-scamtracker-state-stats">): Promise<OperationResponseMap["bbb-scamtracker-state-stats"]>;
  scamtrackerDetail(...args: OperationRequestArgs<"bbb-scamtracker-detail">): Promise<OperationResponseMap["bbb-scamtracker-detail"]>;
  search(...args: OperationRequestArgs<"bbb-search">): Promise<OperationResponseMap["bbb-search"]>;
  searchFilters(...args: OperationRequestArgs<"bbb-search-filters">): Promise<OperationResponseMap["bbb-search-filters"]>;
}
export { BBBClient as Client };
export const operations: Record<string, OperationDefinition>;
export const groups: Record<string, Record<string, string>>;
export const operationCount: number;
export const OperationIds: Readonly<Record<string, OperationId>>;
export const VERSION: string;
export * from "./types.js";
export default BBBClient;

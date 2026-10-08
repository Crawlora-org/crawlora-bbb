# Crawlora Better Business Bureau JavaScript Client Operations

Generated from `openapi/public.json`. Deprecated, admin, and internal operations are excluded from this SDK contract.

Total operations: `9`

| Group | SDK method | Operation ID | HTTP | Params | Auth | Response | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| bbb | `bbb.business` | `bbb-business` | `GET /bbb/business` | `url` (query string required) | `ApiKeyAuth` | `BbbBusinessResponse` |  |
| bbb | `bbb.businessComplaints` | `bbb-business-complaints` | `GET /bbb/business/complaints` | `url` (query string required) | `ApiKeyAuth` | `BbbBusinessComplaintsResponse` |  |
| bbb | `bbb.businessMoreInfo` | `bbb-business-more-info` | `GET /bbb/business/more-info` | `url` (query string required) | `ApiKeyAuth` | `BbbBusinessMoreInfoResponse` |  |
| bbb | `bbb.businessReviews` | `bbb-business-reviews` | `GET /bbb/business/reviews` | `url` (query string required)<br>`page` (query number) | `ApiKeyAuth` | `BbbBusinessReviewsResponse` |  |
| bbb | `bbb.category` | `bbb-category` | `GET /bbb/category` | `url` (query string required)<br>`page` (query number) | `ApiKeyAuth` | `BbbCategoryResponse` |  |
| bbb | `bbb.scamtrackerSearch` | `bbb-scamtracker-search` | `GET /bbb/scamtracker/search` | `query` (query string)<br>`scam_type` (query "Advance Fee Loan" \| "Bank/Credit Card Company Imposter" \| "Business Email Compromise" \| "Charity" \| "Counterfeit Product" \| "COVID-19" \| "Credit Cards" \| "Credit Repair/Debt Relief" \| "CryptoCurrency" \| "Debt Collections" \| "Employment" \| "Fake Check/Money Order" \| "Fake Invoice/Supplier Bill" \| "Family/Friend Emergency" \| "Foreign Money Exchange" \| "Government Agency Imposter" \| "Government Grant" \| "Healthcare/Medicaid/Medicare" \| "Home Improvement" \| "Identity Theft" \| "Investment" \| "Moving" \| "Online Purchase" \| "Other" \| "Phishing" \| "Rental" \| "Retail Business" \| "Romance" \| "Scholarship" \| "Sweepstakes/Lottery/Prizes" \| "Tax Collection" \| "Tech Support" \| "Travel/Vacation/Timeshare" \| "Utility" \| "Vanity Award" \| "Worthless Problem-solving Service" \| "Yellow Pages/Directories")<br>`state` (query string)<br>`scammer_state` (query string)<br>`date_from` (query string)<br>`date_to` (query string)<br>`min_dollars_lost` (query number)<br>`max_dollars_lost` (query number)<br>`page` (query number) | `ApiKeyAuth` | `BbbScamtrackerSearchResponse` |  |
| bbb | `bbb.scamtrackerStateStats` | `bbb-scamtracker-state-stats` | `GET /bbb/scamtracker/state-stats` | `period` (query "30" \| "90" \| "365" \| "all") | `ApiKeyAuth` | `BbbScamtrackerStateStatsResponse` |  |
| bbb | `bbb.scamtrackerDetail` | `bbb-scamtracker-detail` | `GET /bbb/scamtracker/{id}` | `id` (path string required) | `ApiKeyAuth` | `BbbScamtrackerDetailResponse` |  |
| bbb | `bbb.search` | `bbb-search` | `GET /bbb/search` | `query` (query string required)<br>`location` (query string required)<br>`page` (query number) | `ApiKeyAuth` | `BbbSearchResponse` |  |

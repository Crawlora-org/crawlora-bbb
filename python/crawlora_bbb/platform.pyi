from __future__ import annotations

import sys
from typing import Any, Callable, Iterable, Iterator, Literal, Mapping, overload

if sys.version_info >= (3, 11):
    from typing import NotRequired, Required, TypedDict, Unpack
else:
    from typing_extensions import NotRequired, Required, TypedDict, Unpack

ResponseType = Literal["auto", "json", "text", "stream"]

class CrawloraError(Exception):
    status: int
    code: int | None
    body: Any
    raw_body: str
    headers: Mapping[str, str]
    request_id: str | None
    def __init__(self, message: str, *, status: int = ..., code: int | None = ..., body: Any = ..., raw_body: str = ..., headers: Mapping[str, str] | None = ..., request_id: str | None = ..., cause: BaseException | None = ...) -> None: ...

class CrawloraClientError(CrawloraError): ...
class CrawloraServerError(CrawloraError): ...
class CrawloraNetworkError(CrawloraError): ...

class _RequestOptions(TypedDict, total=False):
    _response_type: ResponseType
    _timeout: float
    _headers: Mapping[str, str]

ModelAppResponse = TypedDict('ModelAppResponse', {
    'code': NotRequired[int],
    'data': NotRequired[Any],
    'msg': NotRequired[Any],
}, total=False)

ModelBbbSearchFiltersResponseDoc = TypedDict('ModelBbbSearchFiltersResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelBbbSearchFiltersResponse],
    'msg': NotRequired[str],
}, total=False)

ModelBbbSearchFiltersResponse = TypedDict('ModelBbbSearchFiltersResponse', {
    'categories': NotRequired[list[ModelBbbSearchFilterValue]],
    'country': NotRequired[Literal['USA', 'CAN']],
    'location': NotRequired[str],
    'page': NotRequired[int],
    'query': NotRequired[str],
    'sorts': NotRequired[list[ModelBbbSearchSortOption]],
    'states': NotRequired[list[ModelBbbSearchFilterValue]],
    'total_results': NotRequired[int],
}, total=False)

ModelBbbSearchFilterValue = TypedDict('ModelBbbSearchFilterValue', {
    'label': NotRequired[str],
    'value': NotRequired[str],
}, total=False)

ModelBbbSearchSortOption = TypedDict('ModelBbbSearchSortOption', {
    'is_active': NotRequired[bool],
    'label': NotRequired[str],
    'value': NotRequired[Literal['Relevance', 'Distance', 'Rating', 'AToZ', 'ZToA']],
}, total=False)

ModelBbbSearchResponseDoc = TypedDict('ModelBbbSearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelBbbSearchResponse],
    'msg': NotRequired[str],
}, total=False)

ModelBbbSearchResponse = TypedDict('ModelBbbSearchResponse', {
    'location': NotRequired[str],
    'page': NotRequired[int],
    'query': NotRequired[str],
    'related_categories': NotRequired[list[ModelBbbRelatedCategory]],
    'results': NotRequired[list[ModelBbbBusinessSearchResult]],
    'source_url': NotRequired[str],
    'total_results': NotRequired[int],
}, total=False)

ModelBbbBusinessSearchResult = TypedDict('ModelBbbBusinessSearchResult', {
    'accredited': NotRequired[bool],
    'address': NotRequired[str],
    'categories': NotRequired[list[str]],
    'hq_profile_url': NotRequired[str],
    'image_url': NotRequired[str],
    'name': NotRequired[str],
    'phone': NotRequired[str],
    'quote_url': NotRequired[str],
    'rating': NotRequired[str],
    'service_areas': NotRequired[list[str]],
    'url': NotRequired[str],
}, total=False)

ModelBbbRelatedCategory = TypedDict('ModelBbbRelatedCategory', {
    'name': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelBbbscamtrackerDetailResponseDoc = TypedDict('ModelBbbscamtrackerDetailResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelBbbscamtrackerDetailResponse],
    'msg': NotRequired[str],
}, total=False)

ModelBbbscamtrackerDetailResponse = TypedDict('ModelBbbscamtrackerDetailResponse', {
    'business_name': NotRequired[str],
    'date_reported': NotRequired[str],
    'description': NotRequired[str],
    'dollars_lost': NotRequired[str],
    'id': NotRequired[str],
    'scam_type': NotRequired[str],
    'scammer_email': NotRequired[str],
    'scammer_location': NotRequired[str],
    'scammer_phone': NotRequired[str],
    'scammer_url': NotRequired[str],
    'source_url': NotRequired[str],
    'targeted_location': NotRequired[str],
}, total=False)

ModelBbbscamtrackerStateStatsResponseDoc = TypedDict('ModelBbbscamtrackerStateStatsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelBbbscamtrackerStateStatsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelBbbscamtrackerStateStatsResponse = TypedDict('ModelBbbscamtrackerStateStatsResponse', {
    'aggregated_at': NotRequired[str],
    'period': NotRequired[str],
    'states': NotRequired[list[ModelBbbscamtrackerStateStat]],
}, total=False)

ModelBbbscamtrackerStateStat = TypedDict('ModelBbbscamtrackerStateStat', {
    'code': NotRequired[str],
    'country': NotRequired[str],
    'losses': NotRequired[int],
    'losses_per_capita': NotRequired[float],
    'median_loss': NotRequired[int],
    'name': NotRequired[str],
    'pct_reporting_loss': NotRequired[float],
    'population': NotRequired[int],
    'reports': NotRequired[int],
    'reports_per_capita': NotRequired[float],
    'reports_with_loss': NotRequired[int],
    'scam_type_breakdown': NotRequired[list[ModelBbbscamtrackerScamTypeShare]],
    'top_scam_type': NotRequired[str],
    'yoy_change_pct': NotRequired[float],
}, total=False)

ModelBbbscamtrackerScamTypeShare = TypedDict('ModelBbbscamtrackerScamTypeShare', {
    'count': NotRequired[int],
    'pct': NotRequired[float],
    'type': NotRequired[str],
}, total=False)

ModelBbbscamtrackerSearchResponseDoc = TypedDict('ModelBbbscamtrackerSearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelBbbscamtrackerSearchResponse],
    'msg': NotRequired[str],
}, total=False)

ModelBbbscamtrackerSearchResponse = TypedDict('ModelBbbscamtrackerSearchResponse', {
    'date_from': NotRequired[str],
    'date_to': NotRequired[str],
    'max_dollars_lost': NotRequired[int],
    'min_dollars_lost': NotRequired[int],
    'page': NotRequired[int],
    'query': NotRequired[str],
    'results': NotRequired[list[ModelBbbscamtrackerScamResult]],
    'scam_type': NotRequired[str],
    'scammer_state': NotRequired[str],
    'source_url': NotRequired[str],
    'state': NotRequired[str],
    'total_results': NotRequired[int],
    'total_results_lower_bound': NotRequired[bool],
}, total=False)

ModelBbbscamtrackerScamResult = TypedDict('ModelBbbscamtrackerScamResult', {
    'business_name_used': NotRequired[str],
    'category': NotRequired[str],
    'date_reported': NotRequired[str],
    'description': NotRequired[str],
    'dollars_lost': NotRequired[str],
    'id': NotRequired[str],
    'url': NotRequired[str],
    'victim_location': NotRequired[str],
}, total=False)

ModelBbbdirectoryRegionsResponseDoc = TypedDict('ModelBbbdirectoryRegionsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelBbbdirectoryRegionsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelBbbdirectoryRegionsResponse = TypedDict('ModelBbbdirectoryRegionsResponse', {
    'countries': NotRequired[list[ModelBbbdirectoryCountryRegions]],
}, total=False)

ModelBbbdirectoryCountryRegions = TypedDict('ModelBbbdirectoryCountryRegions', {
    'code': NotRequired[str],
    'name': NotRequired[str],
    'regions': NotRequired[list[ModelBbbdirectoryRegionOption]],
}, total=False)

ModelBbbdirectoryRegionOption = TypedDict('ModelBbbdirectoryRegionOption', {
    'code': NotRequired[str],
    'name': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelBbbnewsTopicsResponse = TypedDict('ModelBbbnewsTopicsResponse', {
    'country': NotRequired[str],
    'source_url': NotRequired[str],
    'topics': NotRequired[list[ModelBbbnewsTopic]],
}, total=False)

ModelBbbnewsTopic = TypedDict('ModelBbbnewsTopic', {
    'name': NotRequired[str],
    'slug': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelBbbnewsNewsResponse = TypedDict('ModelBbbnewsNewsResponse', {
    'country': NotRequired[str],
    'items': NotRequired[list[ModelBbbnewsNewsItem]],
    'page': NotRequired[int],
    'page_size': NotRequired[int],
    'source_url': NotRequired[str],
    'topic': NotRequired[str],
    'total': NotRequired[int],
}, total=False)

ModelBbbnewsNewsItem = TypedDict('ModelBbbnewsNewsItem', {
    'event_start_date': NotRequired[str],
    'event_url': NotRequired[str],
    'id': NotRequired[str],
    'image': NotRequired[ModelBbbnewsImage],
    'modified_date': NotRequired[str],
    'summary': NotRequired[str],
    'title': NotRequired[str],
    'type': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelBbbnewsImage = TypedDict('ModelBbbnewsImage', {
    'alt_text': NotRequired[str],
    'caption': NotRequired[str],
    'credit': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelBbbdirectoryLocalBbbsResponseDoc = TypedDict('ModelBbbdirectoryLocalBbbsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelBbbdirectoryLocalBbbsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelBbbdirectoryLocalBbbsResponse = TypedDict('ModelBbbdirectoryLocalBbbsResponse', {
    'chapters': NotRequired[list[ModelBbbdirectoryLocalBbbchapter]],
    'country': NotRequired[str],
    'region': NotRequired[ModelBbbdirectoryRegionOption],
}, total=False)

ModelBbbdirectoryLocalBbbchapter = TypedDict('ModelBbbdirectoryLocalBbbchapter', {
    'id': NotRequired[str],
    'name': NotRequired[str],
    'offices': NotRequired[list[ModelBbbdirectoryOffice]],
    'open_to_public': NotRequired[bool],
    'url': NotRequired[str],
}, total=False)

ModelBbbdirectoryOffice = TypedDict('ModelBbbdirectoryOffice', {
    'address': NotRequired[ModelBbbdirectoryOfficeAddress],
    'contact': NotRequired[ModelBbbdirectoryOfficeContact],
    'formatted_address': NotRequired[str],
    'is_primary': NotRequired[bool],
    'jurisdictions': NotRequired[list[str]],
    'office_hours': NotRequired[list[str]],
    'phone_hours': NotRequired[list[str]],
    'type': NotRequired[str],
}, total=False)

ModelBbbdirectoryOfficeContact = TypedDict('ModelBbbdirectoryOfficeContact', {
    'email': NotRequired[str],
    'fax_number': NotRequired[str],
    'phone_number': NotRequired[str],
}, total=False)

ModelBbbdirectoryOfficeAddress = TypedDict('ModelBbbdirectoryOfficeAddress', {
    'city': NotRequired[str],
    'country': NotRequired[str],
    'county': NotRequired[str],
    'line1': NotRequired[str],
    'line2': NotRequired[str],
    'location_name': NotRequired[str],
    'postal_code': NotRequired[str],
    'state_province': NotRequired[str],
}, total=False)

ModelBbbdirectoryLocalBbbresponseDoc = TypedDict('ModelBbbdirectoryLocalBbbresponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelBbbdirectoryLocalBbbresponse],
    'msg': NotRequired[str],
}, total=False)

ModelBbbdirectoryLocalBbbresponse = TypedDict('ModelBbbdirectoryLocalBbbresponse', {
    'about': NotRequired[str],
    'events': NotRequired[list[ModelBbbdirectoryBbbevent]],
    'id': NotRequired[str],
    'languages': NotRequired[list[str]],
    'name': NotRequired[str],
    'offices': NotRequired[list[ModelBbbdirectoryOffice]],
    'open_to_public': NotRequired[bool],
    'service_territory': NotRequired[list[str]],
    'tagline': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelBbbdirectoryBbbevent = TypedDict('ModelBbbdirectoryBbbevent', {
    'ends_at': NotRequired[str],
    'starts_at': NotRequired[str],
    'summary': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelBbbCategoryResponseDoc = TypedDict('ModelBbbCategoryResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelBbbCategoryResponse],
    'msg': NotRequired[str],
}, total=False)

ModelBbbCategoryResponse = TypedDict('ModelBbbCategoryResponse', {
    'page': NotRequired[int],
    'results': NotRequired[list[ModelBbbBusinessSearchResult]],
    'source_url': NotRequired[str],
    'total_results': NotRequired[int],
}, total=False)

ModelBbbReviewsResponseDoc = TypedDict('ModelBbbReviewsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelBbbReviewsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelBbbReviewsResponse = TypedDict('ModelBbbReviewsResponse', {
    'average_rating': NotRequired[float],
    'page': NotRequired[int],
    'reviews': NotRequired[list[ModelBbbReviewItem]],
    'source_url': NotRequired[str],
    'total_pages': NotRequired[int],
    'total_reviews': NotRequired[int],
}, total=False)

ModelBbbReviewItem = TypedDict('ModelBbbReviewItem', {
    'author': NotRequired[str],
    'date': NotRequired[str],
    'id': NotRequired[str],
    'rating': NotRequired[int],
    'responses': NotRequired[list[ModelBbbReviewResponse]],
    'text': NotRequired[str],
}, total=False)

ModelBbbReviewResponse = TypedDict('ModelBbbReviewResponse', {
    'date': NotRequired[str],
    'is_business': NotRequired[bool],
    'text': NotRequired[str],
    'title': NotRequired[str],
}, total=False)

ModelBbbMoreInfoResponseDoc = TypedDict('ModelBbbMoreInfoResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelBbbMoreInfoResponse],
    'msg': NotRequired[str],
}, total=False)

ModelBbbMoreInfoResponse = TypedDict('ModelBbbMoreInfoResponse', {
    'business_name': NotRequired[str],
    'rating': NotRequired[str],
    'rating_reasons': NotRequired[list[str]],
    'service_areas': NotRequired[list[str]],
    'source_url': NotRequired[str],
}, total=False)

ModelBbbComplaintsResponseDoc = TypedDict('ModelBbbComplaintsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelBbbComplaintsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelBbbComplaintsResponse = TypedDict('ModelBbbComplaintsResponse', {
    'business_name': NotRequired[str],
    'closed_last_12_months': NotRequired[int],
    'complaints': NotRequired[list[ModelBbbComplaint]],
    'complaints_list_incomplete': NotRequired[bool],
    'period_text': NotRequired[str],
    'source_url': NotRequired[str],
    'submit_complaint_url': NotRequired[str],
    'total_complaints': NotRequired[int],
}, total=False)

ModelBbbComplaint = TypedDict('ModelBbbComplaint', {
    'business_responses': NotRequired[list[ModelBbbComplaintMessage]],
    'customer_answers': NotRequired[list[ModelBbbComplaintMessage]],
    'date': NotRequired[str],
    'id': NotRequired[str],
    'status': NotRequired[str],
    'text': NotRequired[str],
    'type': NotRequired[str],
}, total=False)

ModelBbbComplaintMessage = TypedDict('ModelBbbComplaintMessage', {
    'date': NotRequired[str],
    'text': NotRequired[str],
}, total=False)

ModelBbbBusinessResponseDoc = TypedDict('ModelBbbBusinessResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelBbbBusinessResponse],
    'msg': NotRequired[str],
}, total=False)

ModelBbbBusinessResponse = TypedDict('ModelBbbBusinessResponse', {
    'accredited': NotRequired[bool],
    'accredited_since': NotRequired[str],
    'additional_phone_numbers': NotRequired[list[str]],
    'additional_websites': NotRequired[list[str]],
    'address': NotRequired[str],
    'alternate_names': NotRequired[list[str]],
    'bbb_file_opened': NotRequired[str],
    'business_incorporated': NotRequired[str],
    'business_management': NotRequired[str],
    'business_started': NotRequired[str],
    'categories': NotRequired[list[str]],
    'category': NotRequired[str],
    'entity_type': NotRequired[str],
    'hours': NotRequired[list[ModelBbbBusinessHoursDay]],
    'image_url': NotRequired[str],
    'latest_reviews': NotRequired[list[ModelBbbReviewPreview]],
    'licensing_note': NotRequired[str],
    'local_bbb': NotRequired[str],
    'local_bbb_url': NotRequired[str],
    'more_info_url': NotRequired[str],
    'name': NotRequired[str],
    'phone': NotRequired[str],
    'products_and_services': NotRequired[list[str]],
    'rating': NotRequired[str],
    'rating_reasons': NotRequired[list[str]],
    'social_media': NotRequired[list[str]],
    'source_url': NotRequired[str],
    'url': NotRequired[str],
    'website': NotRequired[str],
    'years_in_business': NotRequired[str],
}, total=False)

ModelBbbReviewPreview = TypedDict('ModelBbbReviewPreview', {
    'author': NotRequired[str],
    'quote': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelBbbBusinessHoursDay = TypedDict('ModelBbbBusinessHoursDay', {
    'day': NotRequired[str],
    'hours': NotRequired[str],
}, total=False)

ModelBbbnewsArticleResponse = TypedDict('ModelBbbnewsArticleResponse', {
    'authors': NotRequired[list[ModelBbbnewsAuthor]],
    'body': NotRequired[str],
    'id': NotRequired[str],
    'image': NotRequired[ModelBbbnewsImage],
    'links': NotRequired[list[ModelBbbnewsLink]],
    'modified_at': NotRequired[str],
    'published_at': NotRequired[str],
    'source_url': NotRequired[str],
    'summary': NotRequired[str],
    'title': NotRequired[str],
    'topics': NotRequired[list[str]],
    'type': NotRequired[str],
}, total=False)

ModelBbbnewsLink = TypedDict('ModelBbbnewsLink', {
    'text': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelBbbnewsAuthor = TypedDict('ModelBbbnewsAuthor', {
    'name': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

BbbArticleResponse = Any
BbbArticleParams = TypedDict('BbbArticleParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'url': Required[str],
}, total=False)

BbbBusinessResponse = ModelBbbBusinessResponseDoc
BbbBusinessParams = TypedDict('BbbBusinessParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'url': Required[str],
}, total=False)

BbbBusinessComplaintsResponse = ModelBbbComplaintsResponseDoc
BbbBusinessComplaintsParams = TypedDict('BbbBusinessComplaintsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'url': Required[str],
}, total=False)

BbbBusinessMoreInfoResponse = ModelBbbMoreInfoResponseDoc
BbbBusinessMoreInfoParams = TypedDict('BbbBusinessMoreInfoParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'url': Required[str],
}, total=False)

BbbBusinessReviewsResponse = ModelBbbReviewsResponseDoc
BbbBusinessReviewsParams = TypedDict('BbbBusinessReviewsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'url': Required[str],
    'page': NotRequired[int],
}, total=False)

BbbCategoryResponse = ModelBbbCategoryResponseDoc
BbbCategoryParams = TypedDict('BbbCategoryParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'url': Required[str],
    'page': NotRequired[int],
    'sort': NotRequired[Literal['Relevance', 'Distance', 'Rating', 'AToZ', 'ZToA']],
    'distance': NotRequired[Literal['5', '10', '25', '50', '100']],
    'rating': NotRequired[list[Literal['A', 'B', 'C', 'D', 'F']]],
    'category_id': NotRequired[list[str]],
    'state': NotRequired[list[str]],
    'accredited': NotRequired[bool],
    'get_quote': NotRequired[bool],
    'service_area': NotRequired[bool],
}, total=False)

BbbLocalBbbResponse = ModelBbbdirectoryLocalBbbresponseDoc
BbbLocalBbbParams = TypedDict('BbbLocalBbbParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'url': Required[str],
}, total=False)

BbbLocalBbbsResponse = ModelBbbdirectoryLocalBbbsResponseDoc
BbbLocalBbbsParams = TypedDict('BbbLocalBbbsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'country': Required[Literal['us', 'ca']],
    'region': Required[str],
}, total=False)

BbbNewsResponse = Any
BbbNewsParams = TypedDict('BbbNewsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'url': Required[str],
}, total=False)

BbbNewsTopicsResponse = Any
BbbNewsTopicsParams = TypedDict('BbbNewsTopicsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'url': Required[str],
}, total=False)

BbbRegionsResponse = ModelBbbdirectoryRegionsResponseDoc
BbbRegionsParams = TypedDict('BbbRegionsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

BbbScamtrackerSearchResponse = ModelBbbscamtrackerSearchResponseDoc
BbbScamtrackerSearchParams = TypedDict('BbbScamtrackerSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'query': NotRequired[str],
    'scam_type': NotRequired[Literal['Advance Fee Loan', 'Bank/Credit Card Company Imposter', 'Business Email Compromise', 'Charity', 'Counterfeit Product', 'COVID-19', 'Credit Cards', 'Credit Repair/Debt Relief', 'CryptoCurrency', 'Debt Collections', 'Employment', 'Fake Check/Money Order', 'Fake Invoice/Supplier Bill', 'Family/Friend Emergency', 'Foreign Money Exchange', 'Government Agency Imposter', 'Government Grant', 'Healthcare/Medicaid/Medicare', 'Home Improvement', 'Identity Theft', 'Investment', 'Moving', 'Online Purchase', 'Other', 'Phishing', 'Rental', 'Retail Business', 'Romance', 'Scholarship', 'Sweepstakes/Lottery/Prizes', 'Tax Collection', 'Tech Support', 'Travel/Vacation/Timeshare', 'Utility', 'Vanity Award', 'Worthless Problem-solving Service', 'Yellow Pages/Directories']],
    'state': NotRequired[str],
    'scammer_state': NotRequired[str],
    'date_from': NotRequired[str],
    'date_to': NotRequired[str],
    'min_dollars_lost': NotRequired[int],
    'max_dollars_lost': NotRequired[int],
    'page': NotRequired[int],
}, total=False)

BbbScamtrackerStateStatsResponse = ModelBbbscamtrackerStateStatsResponseDoc
BbbScamtrackerStateStatsParams = TypedDict('BbbScamtrackerStateStatsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'period': NotRequired[Literal['30', '90', '365', 'all']],
}, total=False)

BbbScamtrackerDetailResponse = ModelBbbscamtrackerDetailResponseDoc
BbbScamtrackerDetailParams = TypedDict('BbbScamtrackerDetailParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

BbbSearchResponse = ModelBbbSearchResponseDoc
BbbSearchParams = TypedDict('BbbSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'query': Required[str],
    'location': Required[str],
    'page': NotRequired[int],
    'country': NotRequired[Literal['USA', 'CAN']],
    'sort': NotRequired[Literal['Relevance', 'Distance', 'Rating', 'AToZ', 'ZToA']],
    'distance': NotRequired[Literal['5', '10', '25', '50', '100']],
    'rating': NotRequired[list[Literal['A', 'B', 'C', 'D', 'F']]],
    'category_id': NotRequired[list[str]],
    'state': NotRequired[list[str]],
    'accredited': NotRequired[bool],
    'get_quote': NotRequired[bool],
    'service_area': NotRequired[bool],
}, total=False)

BbbSearchFiltersResponse = ModelBbbSearchFiltersResponseDoc
BbbSearchFiltersParams = TypedDict('BbbSearchFiltersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'query': NotRequired[str],
    'location': NotRequired[str],
    'category_url': NotRequired[str],
    'country': NotRequired[Literal['USA', 'CAN']],
    'page': NotRequired[int],
    'sort': NotRequired[Literal['Relevance', 'Distance', 'Rating', 'AToZ', 'ZToA']],
    'distance': NotRequired[Literal['5', '10', '25', '50', '100']],
    'rating': NotRequired[list[Literal['A', 'B', 'C', 'D', 'F']]],
    'category_id': NotRequired[list[str]],
    'state': NotRequired[list[str]],
    'accredited': NotRequired[bool],
    'get_quote': NotRequired[bool],
    'service_area': NotRequired[bool],
}, total=False)

class BbbGroup:
    @overload
    def article(self, **params: Unpack[BbbArticleStreamParams]) -> BinaryIO: ...
    @overload
    def article(self, **params: Unpack[BbbArticleTextResponseParams]) -> str: ...
    @overload
    def article(self, **params: Unpack[BbbArticleDefaultParams]) -> BbbArticleResponse: ...
    @overload
    def business(self, **params: Unpack[BbbBusinessStreamParams]) -> BinaryIO: ...
    @overload
    def business(self, **params: Unpack[BbbBusinessTextResponseParams]) -> str: ...
    @overload
    def business(self, **params: Unpack[BbbBusinessDefaultParams]) -> BbbBusinessResponse: ...
    @overload
    def business_complaints(self, **params: Unpack[BbbBusinessComplaintsStreamParams]) -> BinaryIO: ...
    @overload
    def business_complaints(self, **params: Unpack[BbbBusinessComplaintsTextResponseParams]) -> str: ...
    @overload
    def business_complaints(self, **params: Unpack[BbbBusinessComplaintsDefaultParams]) -> BbbBusinessComplaintsResponse: ...
    @overload
    def business_more_info(self, **params: Unpack[BbbBusinessMoreInfoStreamParams]) -> BinaryIO: ...
    @overload
    def business_more_info(self, **params: Unpack[BbbBusinessMoreInfoTextResponseParams]) -> str: ...
    @overload
    def business_more_info(self, **params: Unpack[BbbBusinessMoreInfoDefaultParams]) -> BbbBusinessMoreInfoResponse: ...
    @overload
    def business_reviews(self, **params: Unpack[BbbBusinessReviewsStreamParams]) -> BinaryIO: ...
    @overload
    def business_reviews(self, **params: Unpack[BbbBusinessReviewsTextResponseParams]) -> str: ...
    @overload
    def business_reviews(self, **params: Unpack[BbbBusinessReviewsDefaultParams]) -> BbbBusinessReviewsResponse: ...
    @overload
    def category(self, **params: Unpack[BbbCategoryStreamParams]) -> BinaryIO: ...
    @overload
    def category(self, **params: Unpack[BbbCategoryTextResponseParams]) -> str: ...
    @overload
    def category(self, **params: Unpack[BbbCategoryDefaultParams]) -> BbbCategoryResponse: ...
    @overload
    def local_bbb(self, **params: Unpack[BbbLocalBbbStreamParams]) -> BinaryIO: ...
    @overload
    def local_bbb(self, **params: Unpack[BbbLocalBbbTextResponseParams]) -> str: ...
    @overload
    def local_bbb(self, **params: Unpack[BbbLocalBbbDefaultParams]) -> BbbLocalBbbResponse: ...
    @overload
    def local_bbbs(self, **params: Unpack[BbbLocalBbbsStreamParams]) -> BinaryIO: ...
    @overload
    def local_bbbs(self, **params: Unpack[BbbLocalBbbsTextResponseParams]) -> str: ...
    @overload
    def local_bbbs(self, **params: Unpack[BbbLocalBbbsDefaultParams]) -> BbbLocalBbbsResponse: ...
    @overload
    def news(self, **params: Unpack[BbbNewsStreamParams]) -> BinaryIO: ...
    @overload
    def news(self, **params: Unpack[BbbNewsTextResponseParams]) -> str: ...
    @overload
    def news(self, **params: Unpack[BbbNewsDefaultParams]) -> BbbNewsResponse: ...
    @overload
    def news_topics(self, **params: Unpack[BbbNewsTopicsStreamParams]) -> BinaryIO: ...
    @overload
    def news_topics(self, **params: Unpack[BbbNewsTopicsTextResponseParams]) -> str: ...
    @overload
    def news_topics(self, **params: Unpack[BbbNewsTopicsDefaultParams]) -> BbbNewsTopicsResponse: ...
    @overload
    def regions(self, **params: Unpack[BbbRegionsStreamParams]) -> BinaryIO: ...
    @overload
    def regions(self, **params: Unpack[BbbRegionsTextResponseParams]) -> str: ...
    @overload
    def regions(self, **params: Unpack[BbbRegionsDefaultParams]) -> BbbRegionsResponse: ...
    @overload
    def scamtracker_search(self, **params: Unpack[BbbScamtrackerSearchStreamParams]) -> BinaryIO: ...
    @overload
    def scamtracker_search(self, **params: Unpack[BbbScamtrackerSearchTextResponseParams]) -> str: ...
    @overload
    def scamtracker_search(self, **params: Unpack[BbbScamtrackerSearchDefaultParams]) -> BbbScamtrackerSearchResponse: ...
    @overload
    def scamtracker_state_stats(self, **params: Unpack[BbbScamtrackerStateStatsStreamParams]) -> BinaryIO: ...
    @overload
    def scamtracker_state_stats(self, **params: Unpack[BbbScamtrackerStateStatsTextResponseParams]) -> str: ...
    @overload
    def scamtracker_state_stats(self, **params: Unpack[BbbScamtrackerStateStatsDefaultParams]) -> BbbScamtrackerStateStatsResponse: ...
    @overload
    def scamtracker_detail(self, **params: Unpack[BbbScamtrackerDetailStreamParams]) -> BinaryIO: ...
    @overload
    def scamtracker_detail(self, **params: Unpack[BbbScamtrackerDetailTextResponseParams]) -> str: ...
    @overload
    def scamtracker_detail(self, **params: Unpack[BbbScamtrackerDetailDefaultParams]) -> BbbScamtrackerDetailResponse: ...
    @overload
    def search(self, **params: Unpack[BbbSearchStreamParams]) -> BinaryIO: ...
    @overload
    def search(self, **params: Unpack[BbbSearchTextResponseParams]) -> str: ...
    @overload
    def search(self, **params: Unpack[BbbSearchDefaultParams]) -> BbbSearchResponse: ...
    @overload
    def search_filters(self, **params: Unpack[BbbSearchFiltersStreamParams]) -> BinaryIO: ...
    @overload
    def search_filters(self, **params: Unpack[BbbSearchFiltersTextResponseParams]) -> str: ...
    @overload
    def search_filters(self, **params: Unpack[BbbSearchFiltersDefaultParams]) -> BbbSearchFiltersResponse: ...

OperationId = Literal[
    'bbb-article',
    'bbb-business',
    'bbb-business-complaints',
    'bbb-business-more-info',
    'bbb-business-reviews',
    'bbb-category',
    'bbb-local-bbb',
    'bbb-local-bbbs',
    'bbb-news',
    'bbb-news-topics',
    'bbb-regions',
    'bbb-scamtracker-search',
    'bbb-scamtracker-state-stats',
    'bbb-scamtracker-detail',
    'bbb-search',
    'bbb-search-filters',
]

class CrawloraClient:
    bbb: BbbGroup
    api_key: str
    jwt_token: str
    base_url: str
    timeout: float
    retries: int
    retry_delay: float
    max_retry_delay: float
    retry_statuses: frozenset[int] | None
    retry_predicate: Callable[[int, BaseException | None], bool] | None
    on_retry: Callable[[int, BaseException, float], None] | None
    request_id: bool
    idempotency_keys: bool
    rate_limit: float | None
    max_concurrency: int | None
    logger: Callable[[Mapping[str, Any]], None] | None
    before_request: list[Callable[[dict[str, Any]], None]]
    after_response: list[Callable[[str, int, Mapping[str, str], Any], Any]]
    headers: dict[str, str]
    user_agent: str
    def _is_retryable(self, status: int, exc: BaseException | None) -> bool: ...
    def _compute_retry_delay(self, attempt: int, headers: Mapping[str, str]) -> float: ...
    def _log(self, event: Mapping[str, Any]) -> None: ...
    def __init__(
        self,
        *,
        api_key: str | None = ...,
        jwt_token: str | None = ...,
        base_url: str | None = ...,
        timeout: float = ...,
        retries: int = ...,
        retry_delay: float = ...,
        max_retry_delay: float = ...,
        retry_statuses: Iterable[int] | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
        on_retry: Callable[[int, BaseException, float], None] | None = ...,
        request_id: bool = ...,
        idempotency_keys: bool = ...,
        rate_limit: float | None = ...,
        max_concurrency: int | None = ...,
        logger: Callable[[Mapping[str, Any]], None] | None = ...,
        before_request: Callable[[dict[str, Any]], None] | Iterable[Callable[[dict[str, Any]], None]] | None = ...,
        after_response: Callable[[str, int, Mapping[str, str], Any], Any] | Iterable[Callable[[str, int, Mapping[str, str], Any], Any]] | None = ...,
        headers: Mapping[str, str] | None = ...,
        user_agent: str | None = ...,
        transport: Callable[..., Any] | None = ...,
    ) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> CrawloraClient: ...
    def __exit__(self, *exc: Any) -> None: ...
    def paginate(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    def paginate_items(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        items: Callable[[Any], Any] | None = ...,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    @overload
    def operation(
        self,
        operation_id: Literal['bbb-article'],
        params: BbbArticleParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BbbArticleResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['bbb-business'],
        params: BbbBusinessParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BbbBusinessResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['bbb-business-complaints'],
        params: BbbBusinessComplaintsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BbbBusinessComplaintsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['bbb-business-more-info'],
        params: BbbBusinessMoreInfoParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BbbBusinessMoreInfoResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['bbb-business-reviews'],
        params: BbbBusinessReviewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BbbBusinessReviewsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['bbb-category'],
        params: BbbCategoryParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BbbCategoryResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['bbb-local-bbb'],
        params: BbbLocalBbbParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BbbLocalBbbResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['bbb-local-bbbs'],
        params: BbbLocalBbbsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BbbLocalBbbsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['bbb-news'],
        params: BbbNewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BbbNewsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['bbb-news-topics'],
        params: BbbNewsTopicsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BbbNewsTopicsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['bbb-regions'],
        params: BbbRegionsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BbbRegionsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['bbb-scamtracker-search'],
        params: BbbScamtrackerSearchParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BbbScamtrackerSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['bbb-scamtracker-state-stats'],
        params: BbbScamtrackerStateStatsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BbbScamtrackerStateStatsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['bbb-scamtracker-detail'],
        params: BbbScamtrackerDetailParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BbbScamtrackerDetailResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['bbb-search'],
        params: BbbSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BbbSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['bbb-search-filters'],
        params: BbbSearchFiltersParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BbbSearchFiltersResponse: ...
    @overload
    def operation(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...
    @overload
    def request(
        self,
        operation_id: Literal['bbb-article'],
        params: BbbArticleParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BbbArticleResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['bbb-business'],
        params: BbbBusinessParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BbbBusinessResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['bbb-business-complaints'],
        params: BbbBusinessComplaintsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BbbBusinessComplaintsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['bbb-business-more-info'],
        params: BbbBusinessMoreInfoParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BbbBusinessMoreInfoResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['bbb-business-reviews'],
        params: BbbBusinessReviewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BbbBusinessReviewsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['bbb-category'],
        params: BbbCategoryParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BbbCategoryResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['bbb-local-bbb'],
        params: BbbLocalBbbParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BbbLocalBbbResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['bbb-local-bbbs'],
        params: BbbLocalBbbsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BbbLocalBbbsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['bbb-news'],
        params: BbbNewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BbbNewsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['bbb-news-topics'],
        params: BbbNewsTopicsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BbbNewsTopicsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['bbb-regions'],
        params: BbbRegionsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BbbRegionsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['bbb-scamtracker-search'],
        params: BbbScamtrackerSearchParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BbbScamtrackerSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['bbb-scamtracker-state-stats'],
        params: BbbScamtrackerStateStatsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BbbScamtrackerStateStatsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['bbb-scamtracker-detail'],
        params: BbbScamtrackerDetailParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BbbScamtrackerDetailResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['bbb-search'],
        params: BbbSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BbbSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['bbb-search-filters'],
        params: BbbSearchFiltersParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BbbSearchFiltersResponse: ...
    @overload
    def request(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...

VERSION: str

# Internal helpers reused by the async client; not part of the public API.
def _build_request(base_url: str, operation: Mapping[str, Any], params: dict[str, Any]) -> tuple[Any, Any, dict[str, str]]: ...
def _merge_headers(*sources: Mapping[str, str]) -> dict[str, str]: ...
def _auth_headers(security: list[str], api_key: str, jwt_token: str) -> dict[str, str]: ...
def _ensure_request_id(headers: dict[str, str]) -> str: ...
def _header_value(headers: Mapping[str, str], name: str) -> str: ...
def _parse_response(body: bytes, content_type: str, response_type: str) -> Any: ...
def _validate_response_type(response_type: str) -> ResponseType: ...
def _api_error_class(status: int) -> type[CrawloraError]: ...
def _run_before_request(hooks: list[Any], ctx: dict[str, Any]) -> None: ...
def _run_after_response(hooks: list[Any], operation_id: Any, status: int, headers: Mapping[str, str], body: Any) -> Any: ...
def _allowed_params(operation_id: str) -> set[str]: ...

from typing import BinaryIO

class AsyncCrawloraClient:
    def __init__(self, **kwargs: Any) -> None: ...
    async def aclose(self) -> None: ...
    async def __aenter__(self) -> AsyncCrawloraClient: ...
    async def __aexit__(self, *exc: Any) -> None: ...
    async def request(self, operation_id: str, params: Mapping[str, Any] | None = ..., *, response_type: ResponseType = ..., timeout: float | None = ..., headers: Mapping[str, str] | None = ..., retries: int | None = ..., retry_predicate: Callable[[int, BaseException | None], bool] | None = ...) -> Any: ...

class BBBClient(CrawloraClient):
    def __enter__(self) -> BBBClient: ...
    @overload
    def article(self, **params: Unpack[BbbArticleStreamParams]) -> BinaryIO: ...
    @overload
    def article(self, **params: Unpack[BbbArticleTextResponseParams]) -> str: ...
    @overload
    def article(self, **params: Unpack[BbbArticleDefaultParams]) -> BbbArticleResponse: ...
    @overload
    def business(self, **params: Unpack[BbbBusinessStreamParams]) -> BinaryIO: ...
    @overload
    def business(self, **params: Unpack[BbbBusinessTextResponseParams]) -> str: ...
    @overload
    def business(self, **params: Unpack[BbbBusinessDefaultParams]) -> BbbBusinessResponse: ...
    @overload
    def business_complaints(self, **params: Unpack[BbbBusinessComplaintsStreamParams]) -> BinaryIO: ...
    @overload
    def business_complaints(self, **params: Unpack[BbbBusinessComplaintsTextResponseParams]) -> str: ...
    @overload
    def business_complaints(self, **params: Unpack[BbbBusinessComplaintsDefaultParams]) -> BbbBusinessComplaintsResponse: ...
    @overload
    def business_more_info(self, **params: Unpack[BbbBusinessMoreInfoStreamParams]) -> BinaryIO: ...
    @overload
    def business_more_info(self, **params: Unpack[BbbBusinessMoreInfoTextResponseParams]) -> str: ...
    @overload
    def business_more_info(self, **params: Unpack[BbbBusinessMoreInfoDefaultParams]) -> BbbBusinessMoreInfoResponse: ...
    @overload
    def business_reviews(self, **params: Unpack[BbbBusinessReviewsStreamParams]) -> BinaryIO: ...
    @overload
    def business_reviews(self, **params: Unpack[BbbBusinessReviewsTextResponseParams]) -> str: ...
    @overload
    def business_reviews(self, **params: Unpack[BbbBusinessReviewsDefaultParams]) -> BbbBusinessReviewsResponse: ...
    @overload
    def category(self, **params: Unpack[BbbCategoryStreamParams]) -> BinaryIO: ...
    @overload
    def category(self, **params: Unpack[BbbCategoryTextResponseParams]) -> str: ...
    @overload
    def category(self, **params: Unpack[BbbCategoryDefaultParams]) -> BbbCategoryResponse: ...
    @overload
    def local_bbb(self, **params: Unpack[BbbLocalBbbStreamParams]) -> BinaryIO: ...
    @overload
    def local_bbb(self, **params: Unpack[BbbLocalBbbTextResponseParams]) -> str: ...
    @overload
    def local_bbb(self, **params: Unpack[BbbLocalBbbDefaultParams]) -> BbbLocalBbbResponse: ...
    @overload
    def local_bbbs(self, **params: Unpack[BbbLocalBbbsStreamParams]) -> BinaryIO: ...
    @overload
    def local_bbbs(self, **params: Unpack[BbbLocalBbbsTextResponseParams]) -> str: ...
    @overload
    def local_bbbs(self, **params: Unpack[BbbLocalBbbsDefaultParams]) -> BbbLocalBbbsResponse: ...
    @overload
    def news(self, **params: Unpack[BbbNewsStreamParams]) -> BinaryIO: ...
    @overload
    def news(self, **params: Unpack[BbbNewsTextResponseParams]) -> str: ...
    @overload
    def news(self, **params: Unpack[BbbNewsDefaultParams]) -> BbbNewsResponse: ...
    @overload
    def news_topics(self, **params: Unpack[BbbNewsTopicsStreamParams]) -> BinaryIO: ...
    @overload
    def news_topics(self, **params: Unpack[BbbNewsTopicsTextResponseParams]) -> str: ...
    @overload
    def news_topics(self, **params: Unpack[BbbNewsTopicsDefaultParams]) -> BbbNewsTopicsResponse: ...
    @overload
    def regions(self, **params: Unpack[BbbRegionsStreamParams]) -> BinaryIO: ...
    @overload
    def regions(self, **params: Unpack[BbbRegionsTextResponseParams]) -> str: ...
    @overload
    def regions(self, **params: Unpack[BbbRegionsDefaultParams]) -> BbbRegionsResponse: ...
    @overload
    def scamtracker_search(self, **params: Unpack[BbbScamtrackerSearchStreamParams]) -> BinaryIO: ...
    @overload
    def scamtracker_search(self, **params: Unpack[BbbScamtrackerSearchTextResponseParams]) -> str: ...
    @overload
    def scamtracker_search(self, **params: Unpack[BbbScamtrackerSearchDefaultParams]) -> BbbScamtrackerSearchResponse: ...
    @overload
    def scamtracker_state_stats(self, **params: Unpack[BbbScamtrackerStateStatsStreamParams]) -> BinaryIO: ...
    @overload
    def scamtracker_state_stats(self, **params: Unpack[BbbScamtrackerStateStatsTextResponseParams]) -> str: ...
    @overload
    def scamtracker_state_stats(self, **params: Unpack[BbbScamtrackerStateStatsDefaultParams]) -> BbbScamtrackerStateStatsResponse: ...
    @overload
    def scamtracker_detail(self, **params: Unpack[BbbScamtrackerDetailStreamParams]) -> BinaryIO: ...
    @overload
    def scamtracker_detail(self, **params: Unpack[BbbScamtrackerDetailTextResponseParams]) -> str: ...
    @overload
    def scamtracker_detail(self, **params: Unpack[BbbScamtrackerDetailDefaultParams]) -> BbbScamtrackerDetailResponse: ...
    @overload
    def search(self, **params: Unpack[BbbSearchStreamParams]) -> BinaryIO: ...
    @overload
    def search(self, **params: Unpack[BbbSearchTextResponseParams]) -> str: ...
    @overload
    def search(self, **params: Unpack[BbbSearchDefaultParams]) -> BbbSearchResponse: ...
    @overload
    def search_filters(self, **params: Unpack[BbbSearchFiltersStreamParams]) -> BinaryIO: ...
    @overload
    def search_filters(self, **params: Unpack[BbbSearchFiltersTextResponseParams]) -> str: ...
    @overload
    def search_filters(self, **params: Unpack[BbbSearchFiltersDefaultParams]) -> BbbSearchFiltersResponse: ...

class AsyncBBBClient(AsyncCrawloraClient):
    async def __aenter__(self) -> AsyncBBBClient: ...
    bbb: _AsyncBbbGroup
    @overload
    async def article(self, **params: Unpack[BbbArticleStreamParams]) -> BinaryIO: ...
    @overload
    async def article(self, **params: Unpack[BbbArticleTextResponseParams]) -> str: ...
    @overload
    async def article(self, **params: Unpack[BbbArticleDefaultParams]) -> BbbArticleResponse: ...
    @overload
    async def business(self, **params: Unpack[BbbBusinessStreamParams]) -> BinaryIO: ...
    @overload
    async def business(self, **params: Unpack[BbbBusinessTextResponseParams]) -> str: ...
    @overload
    async def business(self, **params: Unpack[BbbBusinessDefaultParams]) -> BbbBusinessResponse: ...
    @overload
    async def business_complaints(self, **params: Unpack[BbbBusinessComplaintsStreamParams]) -> BinaryIO: ...
    @overload
    async def business_complaints(self, **params: Unpack[BbbBusinessComplaintsTextResponseParams]) -> str: ...
    @overload
    async def business_complaints(self, **params: Unpack[BbbBusinessComplaintsDefaultParams]) -> BbbBusinessComplaintsResponse: ...
    @overload
    async def business_more_info(self, **params: Unpack[BbbBusinessMoreInfoStreamParams]) -> BinaryIO: ...
    @overload
    async def business_more_info(self, **params: Unpack[BbbBusinessMoreInfoTextResponseParams]) -> str: ...
    @overload
    async def business_more_info(self, **params: Unpack[BbbBusinessMoreInfoDefaultParams]) -> BbbBusinessMoreInfoResponse: ...
    @overload
    async def business_reviews(self, **params: Unpack[BbbBusinessReviewsStreamParams]) -> BinaryIO: ...
    @overload
    async def business_reviews(self, **params: Unpack[BbbBusinessReviewsTextResponseParams]) -> str: ...
    @overload
    async def business_reviews(self, **params: Unpack[BbbBusinessReviewsDefaultParams]) -> BbbBusinessReviewsResponse: ...
    @overload
    async def category(self, **params: Unpack[BbbCategoryStreamParams]) -> BinaryIO: ...
    @overload
    async def category(self, **params: Unpack[BbbCategoryTextResponseParams]) -> str: ...
    @overload
    async def category(self, **params: Unpack[BbbCategoryDefaultParams]) -> BbbCategoryResponse: ...
    @overload
    async def local_bbb(self, **params: Unpack[BbbLocalBbbStreamParams]) -> BinaryIO: ...
    @overload
    async def local_bbb(self, **params: Unpack[BbbLocalBbbTextResponseParams]) -> str: ...
    @overload
    async def local_bbb(self, **params: Unpack[BbbLocalBbbDefaultParams]) -> BbbLocalBbbResponse: ...
    @overload
    async def local_bbbs(self, **params: Unpack[BbbLocalBbbsStreamParams]) -> BinaryIO: ...
    @overload
    async def local_bbbs(self, **params: Unpack[BbbLocalBbbsTextResponseParams]) -> str: ...
    @overload
    async def local_bbbs(self, **params: Unpack[BbbLocalBbbsDefaultParams]) -> BbbLocalBbbsResponse: ...
    @overload
    async def news(self, **params: Unpack[BbbNewsStreamParams]) -> BinaryIO: ...
    @overload
    async def news(self, **params: Unpack[BbbNewsTextResponseParams]) -> str: ...
    @overload
    async def news(self, **params: Unpack[BbbNewsDefaultParams]) -> BbbNewsResponse: ...
    @overload
    async def news_topics(self, **params: Unpack[BbbNewsTopicsStreamParams]) -> BinaryIO: ...
    @overload
    async def news_topics(self, **params: Unpack[BbbNewsTopicsTextResponseParams]) -> str: ...
    @overload
    async def news_topics(self, **params: Unpack[BbbNewsTopicsDefaultParams]) -> BbbNewsTopicsResponse: ...
    @overload
    async def regions(self, **params: Unpack[BbbRegionsStreamParams]) -> BinaryIO: ...
    @overload
    async def regions(self, **params: Unpack[BbbRegionsTextResponseParams]) -> str: ...
    @overload
    async def regions(self, **params: Unpack[BbbRegionsDefaultParams]) -> BbbRegionsResponse: ...
    @overload
    async def scamtracker_search(self, **params: Unpack[BbbScamtrackerSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def scamtracker_search(self, **params: Unpack[BbbScamtrackerSearchTextResponseParams]) -> str: ...
    @overload
    async def scamtracker_search(self, **params: Unpack[BbbScamtrackerSearchDefaultParams]) -> BbbScamtrackerSearchResponse: ...
    @overload
    async def scamtracker_state_stats(self, **params: Unpack[BbbScamtrackerStateStatsStreamParams]) -> BinaryIO: ...
    @overload
    async def scamtracker_state_stats(self, **params: Unpack[BbbScamtrackerStateStatsTextResponseParams]) -> str: ...
    @overload
    async def scamtracker_state_stats(self, **params: Unpack[BbbScamtrackerStateStatsDefaultParams]) -> BbbScamtrackerStateStatsResponse: ...
    @overload
    async def scamtracker_detail(self, **params: Unpack[BbbScamtrackerDetailStreamParams]) -> BinaryIO: ...
    @overload
    async def scamtracker_detail(self, **params: Unpack[BbbScamtrackerDetailTextResponseParams]) -> str: ...
    @overload
    async def scamtracker_detail(self, **params: Unpack[BbbScamtrackerDetailDefaultParams]) -> BbbScamtrackerDetailResponse: ...
    @overload
    async def search(self, **params: Unpack[BbbSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def search(self, **params: Unpack[BbbSearchTextResponseParams]) -> str: ...
    @overload
    async def search(self, **params: Unpack[BbbSearchDefaultParams]) -> BbbSearchResponse: ...
    @overload
    async def search_filters(self, **params: Unpack[BbbSearchFiltersStreamParams]) -> BinaryIO: ...
    @overload
    async def search_filters(self, **params: Unpack[BbbSearchFiltersTextResponseParams]) -> str: ...
    @overload
    async def search_filters(self, **params: Unpack[BbbSearchFiltersDefaultParams]) -> BbbSearchFiltersResponse: ...

class _AsyncBbbGroup:
    @overload
    async def article(self, **params: Unpack[BbbArticleStreamParams]) -> BinaryIO: ...
    @overload
    async def article(self, **params: Unpack[BbbArticleTextResponseParams]) -> str: ...
    @overload
    async def article(self, **params: Unpack[BbbArticleDefaultParams]) -> BbbArticleResponse: ...
    @overload
    async def business(self, **params: Unpack[BbbBusinessStreamParams]) -> BinaryIO: ...
    @overload
    async def business(self, **params: Unpack[BbbBusinessTextResponseParams]) -> str: ...
    @overload
    async def business(self, **params: Unpack[BbbBusinessDefaultParams]) -> BbbBusinessResponse: ...
    @overload
    async def business_complaints(self, **params: Unpack[BbbBusinessComplaintsStreamParams]) -> BinaryIO: ...
    @overload
    async def business_complaints(self, **params: Unpack[BbbBusinessComplaintsTextResponseParams]) -> str: ...
    @overload
    async def business_complaints(self, **params: Unpack[BbbBusinessComplaintsDefaultParams]) -> BbbBusinessComplaintsResponse: ...
    @overload
    async def business_more_info(self, **params: Unpack[BbbBusinessMoreInfoStreamParams]) -> BinaryIO: ...
    @overload
    async def business_more_info(self, **params: Unpack[BbbBusinessMoreInfoTextResponseParams]) -> str: ...
    @overload
    async def business_more_info(self, **params: Unpack[BbbBusinessMoreInfoDefaultParams]) -> BbbBusinessMoreInfoResponse: ...
    @overload
    async def business_reviews(self, **params: Unpack[BbbBusinessReviewsStreamParams]) -> BinaryIO: ...
    @overload
    async def business_reviews(self, **params: Unpack[BbbBusinessReviewsTextResponseParams]) -> str: ...
    @overload
    async def business_reviews(self, **params: Unpack[BbbBusinessReviewsDefaultParams]) -> BbbBusinessReviewsResponse: ...
    @overload
    async def category(self, **params: Unpack[BbbCategoryStreamParams]) -> BinaryIO: ...
    @overload
    async def category(self, **params: Unpack[BbbCategoryTextResponseParams]) -> str: ...
    @overload
    async def category(self, **params: Unpack[BbbCategoryDefaultParams]) -> BbbCategoryResponse: ...
    @overload
    async def local_bbb(self, **params: Unpack[BbbLocalBbbStreamParams]) -> BinaryIO: ...
    @overload
    async def local_bbb(self, **params: Unpack[BbbLocalBbbTextResponseParams]) -> str: ...
    @overload
    async def local_bbb(self, **params: Unpack[BbbLocalBbbDefaultParams]) -> BbbLocalBbbResponse: ...
    @overload
    async def local_bbbs(self, **params: Unpack[BbbLocalBbbsStreamParams]) -> BinaryIO: ...
    @overload
    async def local_bbbs(self, **params: Unpack[BbbLocalBbbsTextResponseParams]) -> str: ...
    @overload
    async def local_bbbs(self, **params: Unpack[BbbLocalBbbsDefaultParams]) -> BbbLocalBbbsResponse: ...
    @overload
    async def news(self, **params: Unpack[BbbNewsStreamParams]) -> BinaryIO: ...
    @overload
    async def news(self, **params: Unpack[BbbNewsTextResponseParams]) -> str: ...
    @overload
    async def news(self, **params: Unpack[BbbNewsDefaultParams]) -> BbbNewsResponse: ...
    @overload
    async def news_topics(self, **params: Unpack[BbbNewsTopicsStreamParams]) -> BinaryIO: ...
    @overload
    async def news_topics(self, **params: Unpack[BbbNewsTopicsTextResponseParams]) -> str: ...
    @overload
    async def news_topics(self, **params: Unpack[BbbNewsTopicsDefaultParams]) -> BbbNewsTopicsResponse: ...
    @overload
    async def regions(self, **params: Unpack[BbbRegionsStreamParams]) -> BinaryIO: ...
    @overload
    async def regions(self, **params: Unpack[BbbRegionsTextResponseParams]) -> str: ...
    @overload
    async def regions(self, **params: Unpack[BbbRegionsDefaultParams]) -> BbbRegionsResponse: ...
    @overload
    async def scamtracker_search(self, **params: Unpack[BbbScamtrackerSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def scamtracker_search(self, **params: Unpack[BbbScamtrackerSearchTextResponseParams]) -> str: ...
    @overload
    async def scamtracker_search(self, **params: Unpack[BbbScamtrackerSearchDefaultParams]) -> BbbScamtrackerSearchResponse: ...
    @overload
    async def scamtracker_state_stats(self, **params: Unpack[BbbScamtrackerStateStatsStreamParams]) -> BinaryIO: ...
    @overload
    async def scamtracker_state_stats(self, **params: Unpack[BbbScamtrackerStateStatsTextResponseParams]) -> str: ...
    @overload
    async def scamtracker_state_stats(self, **params: Unpack[BbbScamtrackerStateStatsDefaultParams]) -> BbbScamtrackerStateStatsResponse: ...
    @overload
    async def scamtracker_detail(self, **params: Unpack[BbbScamtrackerDetailStreamParams]) -> BinaryIO: ...
    @overload
    async def scamtracker_detail(self, **params: Unpack[BbbScamtrackerDetailTextResponseParams]) -> str: ...
    @overload
    async def scamtracker_detail(self, **params: Unpack[BbbScamtrackerDetailDefaultParams]) -> BbbScamtrackerDetailResponse: ...
    @overload
    async def search(self, **params: Unpack[BbbSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def search(self, **params: Unpack[BbbSearchTextResponseParams]) -> str: ...
    @overload
    async def search(self, **params: Unpack[BbbSearchDefaultParams]) -> BbbSearchResponse: ...
    @overload
    async def search_filters(self, **params: Unpack[BbbSearchFiltersStreamParams]) -> BinaryIO: ...
    @overload
    async def search_filters(self, **params: Unpack[BbbSearchFiltersTextResponseParams]) -> str: ...
    @overload
    async def search_filters(self, **params: Unpack[BbbSearchFiltersDefaultParams]) -> BbbSearchFiltersResponse: ...

BbbArticleDefaultParams = TypedDict('BbbArticleDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'url': Required[str],
}, total=False)

BbbArticleTextResponseParams = TypedDict('BbbArticleTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'url': Required[str],
}, total=False)

BbbArticleStreamParams = TypedDict('BbbArticleStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'url': Required[str],
}, total=False)

BbbBusinessDefaultParams = TypedDict('BbbBusinessDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'url': Required[str],
}, total=False)

BbbBusinessTextResponseParams = TypedDict('BbbBusinessTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'url': Required[str],
}, total=False)

BbbBusinessStreamParams = TypedDict('BbbBusinessStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'url': Required[str],
}, total=False)

BbbBusinessComplaintsDefaultParams = TypedDict('BbbBusinessComplaintsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'url': Required[str],
}, total=False)

BbbBusinessComplaintsTextResponseParams = TypedDict('BbbBusinessComplaintsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'url': Required[str],
}, total=False)

BbbBusinessComplaintsStreamParams = TypedDict('BbbBusinessComplaintsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'url': Required[str],
}, total=False)

BbbBusinessMoreInfoDefaultParams = TypedDict('BbbBusinessMoreInfoDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'url': Required[str],
}, total=False)

BbbBusinessMoreInfoTextResponseParams = TypedDict('BbbBusinessMoreInfoTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'url': Required[str],
}, total=False)

BbbBusinessMoreInfoStreamParams = TypedDict('BbbBusinessMoreInfoStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'url': Required[str],
}, total=False)

BbbBusinessReviewsDefaultParams = TypedDict('BbbBusinessReviewsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'url': Required[str],
    'page': NotRequired[int],
}, total=False)

BbbBusinessReviewsTextResponseParams = TypedDict('BbbBusinessReviewsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'url': Required[str],
    'page': NotRequired[int],
}, total=False)

BbbBusinessReviewsStreamParams = TypedDict('BbbBusinessReviewsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'url': Required[str],
    'page': NotRequired[int],
}, total=False)

BbbCategoryDefaultParams = TypedDict('BbbCategoryDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'url': Required[str],
    'page': NotRequired[int],
    'sort': NotRequired[Literal['Relevance', 'Distance', 'Rating', 'AToZ', 'ZToA']],
    'distance': NotRequired[Literal['5', '10', '25', '50', '100']],
    'rating': NotRequired[list[Literal['A', 'B', 'C', 'D', 'F']]],
    'category_id': NotRequired[list[str]],
    'state': NotRequired[list[str]],
    'accredited': NotRequired[bool],
    'get_quote': NotRequired[bool],
    'service_area': NotRequired[bool],
}, total=False)

BbbCategoryTextResponseParams = TypedDict('BbbCategoryTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'url': Required[str],
    'page': NotRequired[int],
    'sort': NotRequired[Literal['Relevance', 'Distance', 'Rating', 'AToZ', 'ZToA']],
    'distance': NotRequired[Literal['5', '10', '25', '50', '100']],
    'rating': NotRequired[list[Literal['A', 'B', 'C', 'D', 'F']]],
    'category_id': NotRequired[list[str]],
    'state': NotRequired[list[str]],
    'accredited': NotRequired[bool],
    'get_quote': NotRequired[bool],
    'service_area': NotRequired[bool],
}, total=False)

BbbCategoryStreamParams = TypedDict('BbbCategoryStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'url': Required[str],
    'page': NotRequired[int],
    'sort': NotRequired[Literal['Relevance', 'Distance', 'Rating', 'AToZ', 'ZToA']],
    'distance': NotRequired[Literal['5', '10', '25', '50', '100']],
    'rating': NotRequired[list[Literal['A', 'B', 'C', 'D', 'F']]],
    'category_id': NotRequired[list[str]],
    'state': NotRequired[list[str]],
    'accredited': NotRequired[bool],
    'get_quote': NotRequired[bool],
    'service_area': NotRequired[bool],
}, total=False)

BbbLocalBbbDefaultParams = TypedDict('BbbLocalBbbDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'url': Required[str],
}, total=False)

BbbLocalBbbTextResponseParams = TypedDict('BbbLocalBbbTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'url': Required[str],
}, total=False)

BbbLocalBbbStreamParams = TypedDict('BbbLocalBbbStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'url': Required[str],
}, total=False)

BbbLocalBbbsDefaultParams = TypedDict('BbbLocalBbbsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'country': Required[Literal['us', 'ca']],
    'region': Required[str],
}, total=False)

BbbLocalBbbsTextResponseParams = TypedDict('BbbLocalBbbsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'country': Required[Literal['us', 'ca']],
    'region': Required[str],
}, total=False)

BbbLocalBbbsStreamParams = TypedDict('BbbLocalBbbsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'country': Required[Literal['us', 'ca']],
    'region': Required[str],
}, total=False)

BbbNewsDefaultParams = TypedDict('BbbNewsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'url': Required[str],
}, total=False)

BbbNewsTextResponseParams = TypedDict('BbbNewsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'url': Required[str],
}, total=False)

BbbNewsStreamParams = TypedDict('BbbNewsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'url': Required[str],
}, total=False)

BbbNewsTopicsDefaultParams = TypedDict('BbbNewsTopicsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'url': Required[str],
}, total=False)

BbbNewsTopicsTextResponseParams = TypedDict('BbbNewsTopicsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'url': Required[str],
}, total=False)

BbbNewsTopicsStreamParams = TypedDict('BbbNewsTopicsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'url': Required[str],
}, total=False)

BbbRegionsDefaultParams = TypedDict('BbbRegionsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

BbbRegionsTextResponseParams = TypedDict('BbbRegionsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

BbbRegionsStreamParams = TypedDict('BbbRegionsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

BbbScamtrackerSearchDefaultParams = TypedDict('BbbScamtrackerSearchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'query': NotRequired[str],
    'scam_type': NotRequired[Literal['Advance Fee Loan', 'Bank/Credit Card Company Imposter', 'Business Email Compromise', 'Charity', 'Counterfeit Product', 'COVID-19', 'Credit Cards', 'Credit Repair/Debt Relief', 'CryptoCurrency', 'Debt Collections', 'Employment', 'Fake Check/Money Order', 'Fake Invoice/Supplier Bill', 'Family/Friend Emergency', 'Foreign Money Exchange', 'Government Agency Imposter', 'Government Grant', 'Healthcare/Medicaid/Medicare', 'Home Improvement', 'Identity Theft', 'Investment', 'Moving', 'Online Purchase', 'Other', 'Phishing', 'Rental', 'Retail Business', 'Romance', 'Scholarship', 'Sweepstakes/Lottery/Prizes', 'Tax Collection', 'Tech Support', 'Travel/Vacation/Timeshare', 'Utility', 'Vanity Award', 'Worthless Problem-solving Service', 'Yellow Pages/Directories']],
    'state': NotRequired[str],
    'scammer_state': NotRequired[str],
    'date_from': NotRequired[str],
    'date_to': NotRequired[str],
    'min_dollars_lost': NotRequired[int],
    'max_dollars_lost': NotRequired[int],
    'page': NotRequired[int],
}, total=False)

BbbScamtrackerSearchTextResponseParams = TypedDict('BbbScamtrackerSearchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'query': NotRequired[str],
    'scam_type': NotRequired[Literal['Advance Fee Loan', 'Bank/Credit Card Company Imposter', 'Business Email Compromise', 'Charity', 'Counterfeit Product', 'COVID-19', 'Credit Cards', 'Credit Repair/Debt Relief', 'CryptoCurrency', 'Debt Collections', 'Employment', 'Fake Check/Money Order', 'Fake Invoice/Supplier Bill', 'Family/Friend Emergency', 'Foreign Money Exchange', 'Government Agency Imposter', 'Government Grant', 'Healthcare/Medicaid/Medicare', 'Home Improvement', 'Identity Theft', 'Investment', 'Moving', 'Online Purchase', 'Other', 'Phishing', 'Rental', 'Retail Business', 'Romance', 'Scholarship', 'Sweepstakes/Lottery/Prizes', 'Tax Collection', 'Tech Support', 'Travel/Vacation/Timeshare', 'Utility', 'Vanity Award', 'Worthless Problem-solving Service', 'Yellow Pages/Directories']],
    'state': NotRequired[str],
    'scammer_state': NotRequired[str],
    'date_from': NotRequired[str],
    'date_to': NotRequired[str],
    'min_dollars_lost': NotRequired[int],
    'max_dollars_lost': NotRequired[int],
    'page': NotRequired[int],
}, total=False)

BbbScamtrackerSearchStreamParams = TypedDict('BbbScamtrackerSearchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'query': NotRequired[str],
    'scam_type': NotRequired[Literal['Advance Fee Loan', 'Bank/Credit Card Company Imposter', 'Business Email Compromise', 'Charity', 'Counterfeit Product', 'COVID-19', 'Credit Cards', 'Credit Repair/Debt Relief', 'CryptoCurrency', 'Debt Collections', 'Employment', 'Fake Check/Money Order', 'Fake Invoice/Supplier Bill', 'Family/Friend Emergency', 'Foreign Money Exchange', 'Government Agency Imposter', 'Government Grant', 'Healthcare/Medicaid/Medicare', 'Home Improvement', 'Identity Theft', 'Investment', 'Moving', 'Online Purchase', 'Other', 'Phishing', 'Rental', 'Retail Business', 'Romance', 'Scholarship', 'Sweepstakes/Lottery/Prizes', 'Tax Collection', 'Tech Support', 'Travel/Vacation/Timeshare', 'Utility', 'Vanity Award', 'Worthless Problem-solving Service', 'Yellow Pages/Directories']],
    'state': NotRequired[str],
    'scammer_state': NotRequired[str],
    'date_from': NotRequired[str],
    'date_to': NotRequired[str],
    'min_dollars_lost': NotRequired[int],
    'max_dollars_lost': NotRequired[int],
    'page': NotRequired[int],
}, total=False)

BbbScamtrackerStateStatsDefaultParams = TypedDict('BbbScamtrackerStateStatsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'period': NotRequired[Literal['30', '90', '365', 'all']],
}, total=False)

BbbScamtrackerStateStatsTextResponseParams = TypedDict('BbbScamtrackerStateStatsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'period': NotRequired[Literal['30', '90', '365', 'all']],
}, total=False)

BbbScamtrackerStateStatsStreamParams = TypedDict('BbbScamtrackerStateStatsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'period': NotRequired[Literal['30', '90', '365', 'all']],
}, total=False)

BbbScamtrackerDetailDefaultParams = TypedDict('BbbScamtrackerDetailDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

BbbScamtrackerDetailTextResponseParams = TypedDict('BbbScamtrackerDetailTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

BbbScamtrackerDetailStreamParams = TypedDict('BbbScamtrackerDetailStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

BbbSearchDefaultParams = TypedDict('BbbSearchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'query': Required[str],
    'location': Required[str],
    'page': NotRequired[int],
    'country': NotRequired[Literal['USA', 'CAN']],
    'sort': NotRequired[Literal['Relevance', 'Distance', 'Rating', 'AToZ', 'ZToA']],
    'distance': NotRequired[Literal['5', '10', '25', '50', '100']],
    'rating': NotRequired[list[Literal['A', 'B', 'C', 'D', 'F']]],
    'category_id': NotRequired[list[str]],
    'state': NotRequired[list[str]],
    'accredited': NotRequired[bool],
    'get_quote': NotRequired[bool],
    'service_area': NotRequired[bool],
}, total=False)

BbbSearchTextResponseParams = TypedDict('BbbSearchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'query': Required[str],
    'location': Required[str],
    'page': NotRequired[int],
    'country': NotRequired[Literal['USA', 'CAN']],
    'sort': NotRequired[Literal['Relevance', 'Distance', 'Rating', 'AToZ', 'ZToA']],
    'distance': NotRequired[Literal['5', '10', '25', '50', '100']],
    'rating': NotRequired[list[Literal['A', 'B', 'C', 'D', 'F']]],
    'category_id': NotRequired[list[str]],
    'state': NotRequired[list[str]],
    'accredited': NotRequired[bool],
    'get_quote': NotRequired[bool],
    'service_area': NotRequired[bool],
}, total=False)

BbbSearchStreamParams = TypedDict('BbbSearchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'query': Required[str],
    'location': Required[str],
    'page': NotRequired[int],
    'country': NotRequired[Literal['USA', 'CAN']],
    'sort': NotRequired[Literal['Relevance', 'Distance', 'Rating', 'AToZ', 'ZToA']],
    'distance': NotRequired[Literal['5', '10', '25', '50', '100']],
    'rating': NotRequired[list[Literal['A', 'B', 'C', 'D', 'F']]],
    'category_id': NotRequired[list[str]],
    'state': NotRequired[list[str]],
    'accredited': NotRequired[bool],
    'get_quote': NotRequired[bool],
    'service_area': NotRequired[bool],
}, total=False)

BbbSearchFiltersDefaultParams = TypedDict('BbbSearchFiltersDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'query': NotRequired[str],
    'location': NotRequired[str],
    'category_url': NotRequired[str],
    'country': NotRequired[Literal['USA', 'CAN']],
    'page': NotRequired[int],
    'sort': NotRequired[Literal['Relevance', 'Distance', 'Rating', 'AToZ', 'ZToA']],
    'distance': NotRequired[Literal['5', '10', '25', '50', '100']],
    'rating': NotRequired[list[Literal['A', 'B', 'C', 'D', 'F']]],
    'category_id': NotRequired[list[str]],
    'state': NotRequired[list[str]],
    'accredited': NotRequired[bool],
    'get_quote': NotRequired[bool],
    'service_area': NotRequired[bool],
}, total=False)

BbbSearchFiltersTextResponseParams = TypedDict('BbbSearchFiltersTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'query': NotRequired[str],
    'location': NotRequired[str],
    'category_url': NotRequired[str],
    'country': NotRequired[Literal['USA', 'CAN']],
    'page': NotRequired[int],
    'sort': NotRequired[Literal['Relevance', 'Distance', 'Rating', 'AToZ', 'ZToA']],
    'distance': NotRequired[Literal['5', '10', '25', '50', '100']],
    'rating': NotRequired[list[Literal['A', 'B', 'C', 'D', 'F']]],
    'category_id': NotRequired[list[str]],
    'state': NotRequired[list[str]],
    'accredited': NotRequired[bool],
    'get_quote': NotRequired[bool],
    'service_area': NotRequired[bool],
}, total=False)

BbbSearchFiltersStreamParams = TypedDict('BbbSearchFiltersStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'query': NotRequired[str],
    'location': NotRequired[str],
    'category_url': NotRequired[str],
    'country': NotRequired[Literal['USA', 'CAN']],
    'page': NotRequired[int],
    'sort': NotRequired[Literal['Relevance', 'Distance', 'Rating', 'AToZ', 'ZToA']],
    'distance': NotRequired[Literal['5', '10', '25', '50', '100']],
    'rating': NotRequired[list[Literal['A', 'B', 'C', 'D', 'F']]],
    'category_id': NotRequired[list[str]],
    'state': NotRequired[list[str]],
    'accredited': NotRequired[bool],
    'get_quote': NotRequired[bool],
    'service_area': NotRequired[bool],
}, total=False)

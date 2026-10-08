import os

from crawlora_bbb import BBBClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with BBBClient(api_key=api_key) as client:
    search = client.search(query='coffee', location='New York, NY')
    print('search', search)
    business = client.business(url='https://www.bbb.org/us/tx/austin/profile/plumber/calixto-plumbing-0825-1000223803')
    print('business', business)
    scamtracker_search = client.scamtracker_search(query='package delivery', state='NY')
    print('scamtracker_search', scamtracker_search)

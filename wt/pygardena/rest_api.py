import requests
from urllib.parse import urljoin

class RestAPI(requests.Session):
    """
    Encapsulates all REST calls to the Gardena API.
    """
    
    # The base URL for all Gardena requests. Change this if you want to fire the requests against other services
    base_url = "https://smart.gardena.com/sg-1/"
    
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.headers["Accept"] = "application/json"
    
    def request(self, method, url, *args, **kw):
        return super().request(method, urljoin(self.base_url, url), *args, **kw)
    
from django.http import HttpRequest, HttpResponse
from time import time


def set_useragent_on_request_middleware(get_response):
    
    def middleware(request: HttpRequest):
        request.user_agent = request.META["HTTP_USER_AGENT"]
        response = get_response(request)
        
        return response
    
    return middleware


class CountRequestsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.requests_count = 0
        self.responses_count = 0
        self.exceptions_count = 0
        self.request_time = {}
        
    def __call__(self, request: HttpRequest):
        time_delay = 10
        ip = request.META["REMOTE_ADDR"]
        if str(ip) in self.request_time:
            if self.request_time[str(ip)] + time_delay > int(round(time(), 0)):
                return HttpResponse(f"<h1>Request time error!</h1>" \
                                    f"<h2>You can't send requests more than once every 10 second</h2>")
        self.request_time = {str(ip): int(round(time(), 0))}
        
        self.requests_count += 1
        print("Requests count:", self.requests_count)
        response = self.get_response(request)
        self.responses_count += 1
        print("Response count:", self.responses_count)
        
        return response
    
    def process_exception(self, request: HttpRequest, exception: Exception):
        self.exceptions_count += 1
        print("got", self.exceptions_count, "exceptions so far")
        
    
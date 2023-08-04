"""
Response middleware handler
"""
class ResponseMiddleware:
    """Response"""
    def process_response(self, req, resp, resource, req_succeded):
        """format response"""
        if not hasattr(resp.context, 'result'):
            return
        resp.media = resp.context.result
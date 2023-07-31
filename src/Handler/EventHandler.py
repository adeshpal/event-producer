#Handler file to route all the incoming request to service
import falcon
from src.producer import produce_event

API_VERSIONS = ['v1']
#ValidateParams
class ValidateParameter:
    def validate_version(self, req, resp, resource, params, API_VERSIONS):
        if params.get('version') not in API_VERSIONS:
            raise falcon.HTTPBadRequest(title='Invalid API Version',
            description="Please Provide valid API version to access resources")

@falcon.before(ValidateParameter.validate_version, ['v1', 'v2'])
class EventHandler:
    def on_get(self, req, resp, version):
        if version == 'v1':
            produce_event()
       

    # def on_get_book(self, req, resp, version, book_id):
    #     if version == 'v1':
    #         v1.on_get_book(req, resp, book_id)


    # def on_post(self, req, resp, version):
    #     if version == 'v1':
    #         v1.on_post(req, resp)


    # def on_put_book(self, req, resp, version, book_id):
    #     if version == 'v1':
    #         v1.on_put_book(req, resp, book_id)
 
    
    # def on_delete_book(self, req, resp, version, book_id):
    #     if version == 'v1':
    #         v1.on_delete_book(req, resp, book_id)

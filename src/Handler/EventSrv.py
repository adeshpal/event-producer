"""
Producer Event service
"""
import falcon
import src.params as param
import src.producer as producer

def publish_event(data, resp):
    """response handler"""
    response = {
        "status"  : param.SUCCESS, 
        "message" : "success", 
        "result"  : {}
        }
    output = producer.produce_event(data)
    if output != param.SUCCESS:
        response["status"] = param.FAILED
        response["message"] = "Something went wrong, event may not be processed"
    resp.media = response
    resp.status = falcon.HTTP_201

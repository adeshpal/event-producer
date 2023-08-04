"""Handler file to route all the incoming request to service"""
import logging as log
import json
import falcon
import src.params as param
import  src.Handler.EventSrv as event
from src.Handler.VersionHandler import ValidateParameter

@falcon.before(ValidateParameter.validate_version, param.API_VERSIONS)
class ProducerHandler:
    """Producer srv all exposed methods"""
    def on_post(self,
                req,
                resp,
                version):
        """ publish event message to queue"""
        try:
            body = json.loads(req.stream.read())
            log.warning("Request data to be process req= %s, resp= %s, version=:%s and data= %s",
                            req, resp, version, body)
        except ValueError as err:
            log.error("Unable to load data, error=%s", err)
        return event.publish_event(body, resp=resp)

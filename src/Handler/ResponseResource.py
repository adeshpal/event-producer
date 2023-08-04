import src.params as param

"""user defined response structure """
class ResponseResource:
    """user defined response structure """
    def __init__(self, status=param.SUCCESS, message= "success", result={}):
        """init repsonse structure with default values"""
        self.status = status
        self.message = message
        self.result = result
    # def to_dict(self):
    #     """response structure"""
    #     return {
    #         "status": self.status,
    #         "message" : self.message,
    #         "result" : self.result
    #     }

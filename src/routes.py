import falcon

from src.Middleware.AuthMiddleware import AuthMiddleware
from src.Middleware.ResponseMiddleware import ResponseMiddleware
from src.Handler.ProducerHandler import ProducerHandler

def get_app():
    app = falcon.App(middleware=[AuthMiddleware(), ResponseMiddleware()])
  
    #add message api POST and GET ALL
    app.add_route('/producersrv/{version}/message', ProducerHandler())
    #GET message by id message api ALL
    # app.add_route('/auditsrv/{version}/message/{author_id:int}', )
    
    return app
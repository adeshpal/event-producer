import falcon

from src.Middleware.AuthMiddleware import AuthMiddleware
from src.Middleware.ResponseMiddleware import ResponseMiddleware


def get_app():
    app = falcon.App(middleware=[AuthMiddleware(), ResponseMiddleware()])
    #Subscribe api
    # app.add_route('/auditsrv/{version}/subscribe', Books())
    #add message api POST and GET ALL
    app.add_route('/auditsrv/{version}/message',)
    #GET message by id message api ALL
    app.add_route('/auditsrv/{version}/message/{author_id:int}', )
    
    return app
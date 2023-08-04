""" 
All the routes for producer service 
"""
import falcon
from src.Middleware.AuthMiddleware import AuthMiddleware
from src.Middleware.ResponseMiddleware import ResponseMiddleware
from src.Handler.ProducerHandler import ProducerHandler

def get_app():
    """All producer endpoints would be defined here"""
    app = falcon.App(middleware=[AuthMiddleware(), ResponseMiddleware()])

    #Endpoint to accept all the http method requests
    app.add_route('/producersrv/{version}/message', ProducerHandler())

    return app

import jwt
import falcon
from sqlobject import SQLObjectNotFound

class AuthMiddleware:

    def process_request(self, req, resp):
        if "/login" in req.path:
            return
        token = req.get_header('Authorization')

        if token is None:
            description = ('Please provide an auth token '
                           'as part of the request.')

            raise falcon.HTTPUnauthorized(title='Auth token required',
                                          description=description,
                                          href='http://docs.example.com/auth')

        if not self._token_is_valid(token):
            description = ('The provided auth token is not valid. '
                           'Please request a new token and try again.')

            raise falcon.HTTPUnauthorized(title='Authentication required',
                                          description=description,
                                          href='http://docs.example.com/auth')

    def _token_is_valid(self, token):
        return True
        # try:
        #     payload = jwt.decode(token, "secret", algorithms="HS256")
        #     User.get(payload['user_id'])
        #     return True
        # except (jwt.DecodeError, jwt.ExpiredSignatureError, SQLObjectNotFound):
        #     return False
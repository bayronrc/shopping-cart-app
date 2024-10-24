from requests_oauthlib import OAuth2Session
from utils import Oauth

google = OAuth2Session(
    client_id=Oauth.CLIENT_ID,
    scope=Oauth.SCOPE,
    redirect_uri=Oauth.REDIRECT_URI,
)
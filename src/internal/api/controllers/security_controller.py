import jwt
from connexion.exceptions import OAuthProblem

def info_from_Bearer(api_key: str, required_scopes):
    """
    Check and retrieve authentication information from api_key.
    Returned value will be passed in 'token_info' parameter of your operation function, if there is one.
    'sub' or 'uid' will be set in 'user' parameter of your operation function, if there is one.

    :param api_key API key provided by Authorization header
    :type api_key: str
    :param required_scopes Always None. Used for other authentication method
    :type required_scopes: None
    :return: Information attached to provided api_key or None if api_key is invalid or does not allow access to called API
    :rtype: dict | None
    """
    api_key = api_key.replace("Bearer ", "")
    token = jwt.decode(api_key, "secret", algorithms=["HS256"])

    return {"uid": token["id"], "token_info": token}
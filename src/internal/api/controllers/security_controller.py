import jwt
from connexion.exceptions import OAuthProblem

config = None
user_service = None

def inject_dependencies(_config, _user_service):
    print("dep")
    global config, user_service
    config = _config
    user_service = _user_service


def info_from_Bearer(api_key: str, required_scopes):
    global config, user_service

    print("info")

    if config is None:
        print("none")
        raise ReferenceError("config not injected")
    
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
    api_key = api_key.strip()

    if api_key == "":
        return {"uid": None, "token_info": None}

    token = jwt.decode(api_key, config.daemon.jwt.secret, algorithms=["HS256"])

    user_id = token['sub']
    user = user_service.get_user(by='id', identifier=user_id)
    if user is None:
        # todo log error, should not happend
        return {"uid": None, "token_info": None}


    return {"uid": user, "token_info": token}
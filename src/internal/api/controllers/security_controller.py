import traceback

config = None
authentication_service = None

def inject_dependencies(_config, _authentication_service):
    global config, authentication_service
    config = _config
    authentication_service = _authentication_service


def info_from_Bearer(api_key: str, required_scopes):
    global config, authentication_service

    if config is None:
        e = ReferenceError("config not injected")
        traceback.print_exception(e)
        raise e
    
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
    try:
        api_key = api_key.replace("Bearer ", "")
        api_key = api_key.strip()

        if api_key == "":
            return {"uid": None, "token_info": None}

        user = authentication_service.token_to_user(api_key)

        if user is None:
            return {"uid": None, "token_info": None}
        
    except Exception as e:
        # debug log as exception is dropped silently
        traceback.print_exception(e)
        raise e

    return {"uid": user, "token_info": {}}
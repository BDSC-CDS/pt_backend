from src.pkg.user.model.user import Role

def is_admin(user):
    return is_authenticated(user) and Role("admin") in user.roles

def is_authenticated(user):
    return user is not None

def is_self(user, id):
    return user is not None and user.id == id

def is_admin_or_self(user, id):
    return is_admin(user) or is_self(user, id)
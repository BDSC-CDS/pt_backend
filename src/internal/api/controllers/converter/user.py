

from src.pkg.user.model.user import User, Status, Source
from src.internal.api.server_template.models.templatebackend_user import TemplatebackendUser


def user_to_business(user: TemplatebackendUser) -> User:
    u = User(
        username = user.username,
        email = user.email,
        password = user.password,
        firstname = user.first_name,
        lastname = user.last_name,
        status = Status.ACTIVE,
        source = Source.INTERNAL,
    )

    return u
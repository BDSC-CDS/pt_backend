"""NOTE: Autogenerated. Do not edit the manually."""

from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from server_template.models.base_model import Model
from server_template import util


class TemplatebackendUser(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, tenantid=None, first_name=None, last_name=None, username=None, email=None, password=None, status=None, roles=None, totp_enabled=None, created_at=None, updated_at=None, password_changed=None):
        """TemplatebackendUser - a model defined in OpenAPI

        :param id: The id of this TemplatebackendUser.
        :type id: int
        :param tenantid: The tenantid of this TemplatebackendUser.
        :type tenantid: int
        :param first_name: The first_name of this TemplatebackendUser.
        :type first_name: str
        :param last_name: The last_name of this TemplatebackendUser.
        :type last_name: str
        :param username: The username of this TemplatebackendUser.
        :type username: str
        :param email: The email of this TemplatebackendUser.
        :type email: str
        :param password: The password of this TemplatebackendUser.
        :type password: str
        :param status: The status of this TemplatebackendUser.
        :type status: str
        :param roles: The roles of this TemplatebackendUser.
        :type roles: List[str]
        :param totp_enabled: The totp_enabled of this TemplatebackendUser.
        :type totp_enabled: bool
        :param created_at: The created_at of this TemplatebackendUser.
        :type created_at: datetime
        :param updated_at: The updated_at of this TemplatebackendUser.
        :type updated_at: datetime
        :param password_changed: The password_changed of this TemplatebackendUser.
        :type password_changed: bool
        """
        self.openapi_types = {
            'id': int,
            'tenantid': int,
            'first_name': str,
            'last_name': str,
            'username': str,
            'email': str,
            'password': str,
            'status': str,
            'roles': List[str],
            'totp_enabled': bool,
            'created_at': datetime,
            'updated_at': datetime,
            'password_changed': bool
        }

        self.attribute_map = {
            'id': 'id',
            'tenantid': 'tenantid',
            'first_name': 'firstName',
            'last_name': 'lastName',
            'username': 'username',
            'email': 'email',
            'password': 'password',
            'status': 'status',
            'roles': 'roles',
            'totp_enabled': 'totpEnabled',
            'created_at': 'createdAt',
            'updated_at': 'updatedAt',
            'password_changed': 'passwordChanged'
        }

        self._id = id
        self._tenantid = tenantid
        self._first_name = first_name
        self._last_name = last_name
        self._username = username
        self._email = email
        self._password = password
        self._status = status
        self._roles = roles
        self._totp_enabled = totp_enabled
        self._created_at = created_at
        self._updated_at = updated_at
        self._password_changed = password_changed

    @classmethod
    def from_dict(cls, dikt) -> 'TemplatebackendUser':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The templatebackendUser of this TemplatebackendUser.
        :rtype: TemplatebackendUser
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this TemplatebackendUser.


        :return: The id of this TemplatebackendUser.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this TemplatebackendUser.


        :param id: The id of this TemplatebackendUser.
        :type id: int
        """

        self._id = id

    @property
    def tenantid(self) -> int:
        """Gets the tenantid of this TemplatebackendUser.


        :return: The tenantid of this TemplatebackendUser.
        :rtype: int
        """
        return self._tenantid

    @tenantid.setter
    def tenantid(self, tenantid: int):
        """Sets the tenantid of this TemplatebackendUser.


        :param tenantid: The tenantid of this TemplatebackendUser.
        :type tenantid: int
        """

        self._tenantid = tenantid

    @property
    def first_name(self) -> str:
        """Gets the first_name of this TemplatebackendUser.


        :return: The first_name of this TemplatebackendUser.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str):
        """Sets the first_name of this TemplatebackendUser.


        :param first_name: The first_name of this TemplatebackendUser.
        :type first_name: str
        """

        self._first_name = first_name

    @property
    def last_name(self) -> str:
        """Gets the last_name of this TemplatebackendUser.


        :return: The last_name of this TemplatebackendUser.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        """Sets the last_name of this TemplatebackendUser.


        :param last_name: The last_name of this TemplatebackendUser.
        :type last_name: str
        """

        self._last_name = last_name

    @property
    def username(self) -> str:
        """Gets the username of this TemplatebackendUser.


        :return: The username of this TemplatebackendUser.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username: str):
        """Sets the username of this TemplatebackendUser.


        :param username: The username of this TemplatebackendUser.
        :type username: str
        """

        self._username = username

    @property
    def email(self) -> str:
        """Gets the email of this TemplatebackendUser.


        :return: The email of this TemplatebackendUser.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this TemplatebackendUser.


        :param email: The email of this TemplatebackendUser.
        :type email: str
        """

        self._email = email

    @property
    def password(self) -> str:
        """Gets the password of this TemplatebackendUser.


        :return: The password of this TemplatebackendUser.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password: str):
        """Sets the password of this TemplatebackendUser.


        :param password: The password of this TemplatebackendUser.
        :type password: str
        """

        self._password = password

    @property
    def status(self) -> str:
        """Gets the status of this TemplatebackendUser.


        :return: The status of this TemplatebackendUser.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """Sets the status of this TemplatebackendUser.


        :param status: The status of this TemplatebackendUser.
        :type status: str
        """

        self._status = status

    @property
    def roles(self) -> List[str]:
        """Gets the roles of this TemplatebackendUser.


        :return: The roles of this TemplatebackendUser.
        :rtype: List[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles: List[str]):
        """Sets the roles of this TemplatebackendUser.


        :param roles: The roles of this TemplatebackendUser.
        :type roles: List[str]
        """

        self._roles = roles

    @property
    def totp_enabled(self) -> bool:
        """Gets the totp_enabled of this TemplatebackendUser.


        :return: The totp_enabled of this TemplatebackendUser.
        :rtype: bool
        """
        return self._totp_enabled

    @totp_enabled.setter
    def totp_enabled(self, totp_enabled: bool):
        """Sets the totp_enabled of this TemplatebackendUser.


        :param totp_enabled: The totp_enabled of this TemplatebackendUser.
        :type totp_enabled: bool
        """

        self._totp_enabled = totp_enabled

    @property
    def created_at(self) -> datetime:
        """Gets the created_at of this TemplatebackendUser.


        :return: The created_at of this TemplatebackendUser.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at: datetime):
        """Sets the created_at of this TemplatebackendUser.


        :param created_at: The created_at of this TemplatebackendUser.
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self) -> datetime:
        """Gets the updated_at of this TemplatebackendUser.


        :return: The updated_at of this TemplatebackendUser.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at: datetime):
        """Sets the updated_at of this TemplatebackendUser.


        :param updated_at: The updated_at of this TemplatebackendUser.
        :type updated_at: datetime
        """

        self._updated_at = updated_at

    @property
    def password_changed(self) -> bool:
        """Gets the password_changed of this TemplatebackendUser.


        :return: The password_changed of this TemplatebackendUser.
        :rtype: bool
        """
        return self._password_changed

    @password_changed.setter
    def password_changed(self, password_changed: bool):
        """Sets the password_changed of this TemplatebackendUser.


        :param password_changed: The password_changed of this TemplatebackendUser.
        :type password_changed: bool
        """

        self._password_changed = password_changed

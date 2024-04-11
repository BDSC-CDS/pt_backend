import unittest
from unittest.mock import MagicMock, patch
import sys
import os

api_dir_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(api_dir_path)

from server_template.models import TemplatebackendUser, TemplatebackendUpdatePasswordRequest
from src.internal.api.controllers.middleware.user_audit import UsersControllerAudit
from src.pkg.audit_log.service.audit_log import AuditLogService
from src.internal.api.controllers.user_controller import UsersController

class UsersControllerAuditTest(unittest.TestCase):

    def setUp(self):
        self.mock_users_controller = MagicMock(spec=UsersController)
        self.mock_audit_log_service = MagicMock(spec=AuditLogService)
        self.users_controller_audit = UsersControllerAudit(
            next=self.mock_users_controller,
            auditLogService=self.mock_audit_log_service
        )
        self.user = MagicMock()
        self.body = TemplatebackendUser(id=123)
        self.response = MagicMock()

    def test_user_service_create_user_success(self):
        self.mock_users_controller.user_service_create_user.return_value = self.response

        response = self.users_controller_audit.user_service_create_user(self.user, self.body)

        self.assertEqual(response, self.response)
        self.mock_users_controller.user_service_create_user.assert_called_once_with(self.user, self.body)
        self.mock_audit_log_service.log_event.assert_called_once()

    def test_user_service_delete_user_success(self):
        # Assuming we have a user ID to delete
        user_id = 123
        self.mock_users_controller.user_service_delete_user.return_value = self.response

        response = self.users_controller_audit.user_service_delete_user(self.user, user_id)

        self.assertEqual(response, self.response)
        self.mock_users_controller.user_service_delete_user.assert_called_once_with(self.user, user_id)
        self.mock_audit_log_service.log_event.assert_called_once()

    def test_user_service_get_user_success(self):
        user_id = 123
        self.mock_users_controller.user_service_get_user.return_value = self.response

        response = self.users_controller_audit.user_service_get_user(self.user, user_id)

        self.assertEqual(response, self.response)
        self.mock_users_controller.user_service_get_user.assert_called_once_with(self.user, user_id)
        self.mock_audit_log_service.log_event.assert_called_once()

    def test_user_service_get_user_me_success(self):
        self.mock_users_controller.user_service_get_user_me.return_value = self.response

        response = self.users_controller_audit.user_service_get_user_me(self.user)

        self.assertEqual(response, self.response)
        self.mock_users_controller.user_service_get_user_me.assert_called_once_with(self.user)
        self.mock_audit_log_service.log_event.assert_called_once()

    def test_user_service_reset_password_success(self):
        user_id = 123
        body = {}
        self.mock_users_controller.user_service_reset_password.return_value = self.response

        response = self.users_controller_audit.user_service_reset_password(self.user, user_id, body)

        self.assertEqual(response, self.response)
        self.mock_users_controller.user_service_reset_password.assert_called_once_with(self.user, user_id, body)
        self.mock_audit_log_service.log_event.assert_called_once()

    def test_user_service_update_password_success(self):
        body = TemplatebackendUpdatePasswordRequest()
        self.mock_users_controller.user_service_update_password.return_value = self.response
        response = self.users_controller_audit.user_service_update_password(self.user, body)

        self.assertEqual(response, self.response)
        self.mock_users_controller.user_service_update_password.assert_called_once_with(self.user, body)
        self.mock_audit_log_service.log_event.assert_called_once()

if __name__ == '__main__':
    unittest.main()

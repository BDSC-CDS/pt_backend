import unittest
from unittest.mock import MagicMock, patch
import sys
import os

api_dir_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../internal/api'))
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

import unittest
from unittest.mock import MagicMock, patch
from src.internal.steward.steward import Steward
from src.pkg.user.model.user import User
from src.pkg.questionnaire.model.questionnaire import Questionnaire

class TestSteward(unittest.TestCase):

    @patch('src.internal.cmd.provider.user.provide_user_service')
    @patch('src.internal.cmd.provider.questionnaire.provide_questionnaire_service')
    @patch('src.internal.cmd.provider.config.provide_config')
    def test_admin_user_creation(self, mock_provide_config, mock_provide_user_service, mock_provide_questionnaire_service):
        # Mock config
        mock_config = MagicMock()
        mock_config.enabled = True
        mock_config.user.username = "admin"
        mock_config.user.password = "password"
        mock_provide_config.return_value = mock_config

        # Mock user service
        mock_user_service = MagicMock()
        mock_user_service.get_user.return_value = None  # No existing admin user
        mock_provide_user_service.return_value = mock_user_service

        # Mock questionnaire service
        mock_questionnaire_service = MagicMock()
        mock_provide_questionnaire_service.return_value = mock_questionnaire_service

        # Initialize Steward
        steward = Steward(mock_config, mock_user_service, mock_questionnaire_service)

        # Verify admin user creation
        mock_user_service.get_user.assert_called_once_with(by="username", identifier="admin")
        mock_user_service.create_user.assert_called_once_with(user=User(username="admin", password="password"))
        mock_user_service.set_admin.assert_called_once()
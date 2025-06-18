import unittest
from unittest.mock import MagicMock
from src.pkg.user.model.user import User
from src.pkg.questionnaire.model.questionnaire import Questionnaire
from src.pkg.questionnaire.model.questionnaire_v2_0 import questionnaire_v2_0
from src.pkg.questionnaire.model.questionnaire_v2_1 import questionnaire_v2_1
from src.internal.steward.steward import Steward


class TestSteward(unittest.TestCase):
    def setUp(self):
        # Mock configuration
        self.mock_config = MagicMock()
        self.mock_config.user.enabled = False
        self.mock_config.user.username = "admin"
        self.mock_config.user.password = "password"
        self.mock_config.questionnaire.enabled = False
        self.mock_config.questionnaire.name = "Questionnaire name"

        # Mock services
        self.mock_users_service = MagicMock()
        self.mock_questionnaire_service = MagicMock()

        # Admin user mock object
        self.mock_admin_user = User(username="admin", password="admin_password")
        self.mock_admin_user.id = 1
        self.mock_admin_user.tenantid = 0

        # Questionnaire mock object
        self.mock_questionnaire = Questionnaire(
            userid=self.mock_admin_user.id,
            tenantid=self.mock_admin_user.tenantid,
            name="Questionnaire V2.1",
            versions=[questionnaire_v2_1],
        )

        # Initialize Steward with mocks
        self.steward = Steward(self.mock_config, self.mock_users_service, self.mock_questionnaire_service)

    def test_seed_database_creates_admin_user(self):
        # Enable steward
        self.mock_config.user.enabled = True

        # Configure mock to simulate admin user not existing
        self.mock_users_service.get_user.return_value = None
        self.mock_users_service.create_user.return_value = self.mock_admin_user

        # Call seed_database
        self.steward.seed_database()

        # Verify admin user creation was called
        self.mock_users_service.create_user.assert_called_once_with(
            user=User(
                username=self.mock_config.user.username,
                password=self.mock_config.user.password,
            )
        )
        self.mock_users_service.set_admin.assert_called_once_with(userid=self.mock_admin_user.id)

    def test_seed_database_does_not_create_existing_admin_user(self):
        # Enable steward
        self.mock_config.user.enabled = True

        # Configure mock to simulate admin user already exists
        self.mock_users_service.get_user.return_value = self.mock_admin_user

        # Call seed_database
        self.steward.seed_database()

        # Verify admin user creation was not called
        self.mock_users_service.create_user.assert_not_called()
        self.mock_users_service.set_admin.assert_not_called()

    def test_seed_database_creates_questionnaire(self):
        # Enable steward
        self.mock_config.questionnaire.enabled = True

        # Configure mock to simulate questionnaire not existing
        self.mock_users_service.get_user.return_value = self.mock_admin_user
        self.mock_questionnaire_service.list_questionnaires.return_value = None
        self.mock_questionnaire_service.create_questionnaire.return_value = self.mock_questionnaire

        # Call seed_database
        self.steward.seed_database()

        # Verify questionnaire creation was called
        self.mock_questionnaire_service.create_questionnaire.assert_called_once_with(
            Questionnaire(
                userid=self.mock_admin_user.id,
                tenantid=self.mock_admin_user.tenantid,
                name="Questionnaire name",
                versions=[questionnaire_v2_1],
            )
        )

    def test_seed_database_does_not_create_existing_questionnaire(self):
        # Enable steward
        self.mock_config.questionnaire.enabled = True

        # Configure mock to simulate questionnaire already exists
        self.mock_users_service.get_user.return_value = self.mock_admin_user
        self.mock_questionnaire_service.list_questionnaires.return_value = [self.mock_questionnaire]

        # Call seed_database
        self.steward.seed_database()

        # Verify questionnaire creation was not called
        self.mock_questionnaire_service.create_questionnaire.assert_not_called()

    
    def test_seed_database_skips_admin_user_creation_when_disabled(self):
        # Set user.enabled to False
        self.mock_config.user.enabled = False

        # Call seed_database
        self.steward.seed_database()

        # Verify no user-related methods are called
        self.mock_users_service.get_user.assert_not_called()
        self.mock_users_service.create_user.assert_not_called()
        self.mock_users_service.set_admin.assert_not_called()

    def test_seed_database_skips_questionnaire_creation_when_disabled(self):
        # Set questionnaire.enabled to False
        self.mock_config.questionnaire.enabled = False

        # Simulate admin user already exists
        self.mock_users_service.get_user.return_value = self.mock_admin_user

        # Call seed_database
        self.steward.seed_database()

        # Verify no questionnaire-related methods are called
        self.mock_questionnaire_service.list_questionnaires.assert_not_called()
        self.mock_questionnaire_service.create_questionnaire.assert_not_called()

    def test_seed_database_skips_all_when_both_disabled(self):
        # Set both user.enabled and questionnaire.enabled to False
        self.mock_config.user.enabled = False
        self.mock_config.questionnaire.enabled = False

        # Call seed_database
        self.steward.seed_database()

        # Verify no user-related methods are called
        self.mock_users_service.get_user.assert_not_called()
        self.mock_users_service.create_user.assert_not_called()
        self.mock_users_service.set_admin.assert_not_called()

        # Verify no questionnaire-related methods are called
        self.mock_questionnaire_service.list_questionnaires.assert_not_called()
        self.mock_questionnaire_service.create_questionnaire.assert_not_called()

    def test_seed_database_throws_exception_when_no_admin_user_for_questionnaire(self):
        # Set both user.enabled and questionnaire.enabled to False
        self.mock_config.user.enabled = False
        self.mock_config.questionnaire.enabled = True

        # Configure mock to simulate questionnaire already exists
        self.mock_users_service.get_user.return_value = None
        self.mock_questionnaire_service.list_questionnaires.return_value = None

        # Assert that an exception is raised
        with self.assertRaises(Exception) as context:
            self.steward.seed_database()

        # Optionally, check the exception message
        self.assertIn("Cannot create a questionnaire without an admin user", str(context.exception))

if __name__ == "__main__":
    unittest.main()
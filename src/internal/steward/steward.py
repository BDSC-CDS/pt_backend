from src.pkg.user.model.user import User
from src.pkg.questionnaire.model.questionnaire import Questionnaire
from src.pkg.questionnaire.model.questionnaire_v2 import questionnaire_v2
from src.pkg.questionnaire.model.questionnaire_v3 import questionnaire_v3

class Steward:
    def __init__(self, steward_config, users_service, questionnaire_service):
        # Save config
        self.config = steward_config

        # Services and stores
        self.users_service = users_service
        self.questionnaire_service = questionnaire_service

        # Internal objects
        self.admin_user = None
        self.questionnaire = None

        # Seed database
        self.seed_database()

    def seed_database(self):
        """Seed initial data into the database."""
        if self.config.user.enabled:
            self.admin_user = self._create_admin_user()

        if self.config.questionnaire.enabled:
            self._create_questionnaire()

    def _create_admin_user(self):
        """Add admin user to the database."""
        try:
            # Check if admin user already exists
            existing_user = self.users_service.get_user(by="username", identifier=self.config.user.username)
            if existing_user:
                print("Admin user already exists.")
                return existing_user

            # Create admin user & set role
            u = self.users_service.create_user(user=User(
                username=self.config.user.username,
                password=self.config.user.password,
            ))
            self.users_service.set_admin(userid=u.id)
            print("Admin user created.")
            return u
        except Exception as e:
            raise Exception(f"Failed to create admin user: {e}")

    def _create_questionnaire(self):
        """Add initial questionnaire to the admin user."""
        try:
            # Check if admin user exists
            if self.admin_user is None:
                existing_user = self.users_service.get_user(by="username", identifier=self.config.user.username)
                if existing_user is None:
                    raise Exception("Cannot create a questionnaire without an admin user. Please update the steward config.")
                else:
                    self.admin_user = existing_user

            # Check if questionnaire already exists
            existing_questionnaire = self.questionnaire_service.list_questionnaires(tenantid=self.admin_user.tenantid, userid=self.admin_user.id)
            if existing_questionnaire is None:
                # Create questionnaire
                q = self.questionnaire_service.create_questionnaire(
                    Questionnaire(
                        userid=self.admin_user.id, 
                        tenantid=self.admin_user.tenantid, 
                        name=self.config.questionnaire.name, 
                        versions=[questionnaire_v3],
                    )
                )
                print("Initial questionnaire created.")
                return q
            else:
                print("Initial questionnaire already exists.")
                return existing_questionnaire[0]
        except Exception as e:
            raise Exception(f"Failed to create initial questionnaire: {e}")
from src.pkg.user.model.user import User
from src.pkg.questionnaire.model.questionnaire import Questionnaire
from src.pkg.questionnaire.model.questionnaire_v2 import questionnaire_v2

class Steward:
    def __init__(self, steward_config, user_service, questionnaire_service):
        # Save config
        self.config = steward_config

        # Services and stores
        self.user_service = user_service
        self.questionnaire_service = questionnaire_service

        # Seed database
        self.seed_database()

    def seed_database(self):
        """Seed initial data into the database."""
        if self.config.enabled:
            self._create_admin_user()
            self._create_questionnaire()

    def _create_admin_user(self):
        """Add admin user to the database."""
        try:
            # Check if admin user already exists
            existing_user = self.user_service.get_user(by="username", identifier=self.config.user.username)
            if existing_user:
                self.admin_user = existing_user
                print("Admin user already exists.")
                print(self.admin_user)

                return

            # Create admin user & set role
            self.admin_user = self.user_service.create_user(user=User(
                username=self.config.user.username,
                password=self.config.user.password,
            ))
            self.user_service.set_admin(userid=self.admin_user.id)
            print("Admin user created.")
            print(self.admin_user)

        except Exception as e:
            print(f"Failed to create admin user: {e}")

    def _create_questionnaire(self):
        """Add initial questionnaire to the admin user."""
        try:
            # Check if questionnaire already exists
            existing_questionnaire = self.questionnaire_service.list_questionnaires(tenantid=self.admin_user.tenantid, userid=self.admin_user.id)
            if existing_questionnaire is None:
                # Create questionnaire
                self.questionnaire = self.questionnaire_service.create_questionnaire(
                    Questionnaire(
                        userid=self.admin_user.id, 
                        tenantid=self.admin_user.tenantid, 
                        name='Questionnaire V2', 
                        versions=[questionnaire_v2],
                    )
                )
                print("Initial questionnaire created.")
            else:
                self.questionnaire = existing_questionnaire[0]
                print("Initial questionnaire already exists.")

        except Exception as e:
            print(f"Failed to create initial questionnaire: {e}")

        
from sqlalchemy import Engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from src.pkg.user.model.user import User, Role


class UserStore:
    def __init__(self, db: Engine):
        self.db = db

    @contextmanager
    def session_scope(self):
        """Provide a transactional scope around a series of operations."""
        Session = sessionmaker(bind=self.db)
        session = Session()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def create_user(self, user: User):
        user_query = """
INSERT INTO users 
    (tenantid, firstname, lastname, username, password, status, totpsecret, createdat, updatedat)
VALUES 
    (:tenant_id, :first_name, :last_name, :username, :password, :status, :totp_secret, NOW(), NOW()) 
RETURNING id;
"""

        user_role_query = """
INSERT INTO user_role (userid, roleid) VALUES (:user_id, :role_id);
        """

        recovery_code_query = """
INSERT INTO totp_recovery_codes (tenantid, userid, code) VALUES (:tenant_id, :user_id, :code);
        """

        with self.session_scope() as session:
            try:
                result = session.execute(user_query, {
                    'first_name': user.firstname, 
                    'last_name': user.lastname,
                    'username': user.username, 
                    'password': user.password, 
                    'status': user.status.value, 
                    'totp_secret': user.totpsecret
                }).fetchone()
                user_id = result[0]

                roles = self.get_roles()

                for ur in user.roles:
                    found = False
                    for r in roles:
                        if ur.id == r.id:
                            session.execute(user_role_query, {'user_id': user_id, 'role_id': r.id})
                            found = True
                            break
                    if not found:
                        raise ValueError(f"unknown user role: {ur}")

                if user.totp_recovery_codes:
                    for rc in user.totp_recovery_codes:
                        session.execute(recovery_code_query, {'user_id': user_id, 'code': rc})

            except SQLAlchemyError as e:
                raise e

            return user_id

    def get_roles(self):
        query = "SELECT id FROM roles;"
        with self.session_scope() as session:
            roles = session.execute(query).fetchall()
            return [Role(id=row[0]) for row in roles]

from sqlalchemy import Engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
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

    def create_user(self, user: User) -> User:
        user_query = """
INSERT INTO users
    (tenantid, firstname, lastname, username, email, password, status, source, totpsecret, createdat, updatedat)
VALUES
    (:tenantid, :firstname, :lastname, :username, :email, :password, :status, :source, :totpsecret, NOW(), NOW())
RETURNING id;
"""

        user_role_query = """
INSERT INTO user_role (userid, roleid) VALUES (:userid, :roleid);
        """
        #TODO change
        if not user.tenantid:
            user.tenantid = 1

        with self.session_scope() as session:
            try:
                result = session.execute(text(user_query), {
                    'tenantid': user.tenantid,
                    'firstname': user.firstname,
                    'lastname': user.lastname,
                    'username': user.username,
                    'email': user.email,
                    'password': user.password,
                    'status': user.status.value,
                    'source': user.source.value,
                    'totpsecret': user.totpsecret
                }).fetchone()
                user_id = result[0]

                roles = self.get_roles()

                for ur in user.roles:
                    found = False
                    for r in roles:
                        if ur.id == r.id:
                            session.execute(text(user_role_query), {
                                'tenantid': user.tenantid,
                                'userid': user_id,
                                'roleid': r.id,
                            })
                            found = True
                            break
                    if not found:
                        raise ValueError(f"unknown user role: {ur}")

            except SQLAlchemyError as e:
                raise e

            return User(id=user_id)

    def get_roles(self):
        query = "SELECT id FROM roles;"
        with self.session_scope() as session:
            roles = session.execute(text(query)).fetchall()
            return [Role(id=row[0]) for row in roles]

    def get_user(self, by: str, identifier: str | int) -> User :
        if by not in ['id', 'username', 'email']:
            raise Exception("identifier must be one of 'id', 'username', 'email'")

        role_query = "SELECT role FROM user_role WHERE userid = :userid;"
        query = "SELECT * FROM users where " + by + " = :identifier;"
        with self.session_scope() as session:
            user = session.execute(text(query), {
                'identifier': identifier,
            }).mappings().fetchone()

            if user is None:
                return None

            u = User(
                id=user.id,
                tenantid=user.tenantid,
                username=user.username,
                email=user.email,
                password=user.password,
                firstname=user.firstname,
                lastname=user.lastname,
                status=user.status,
                source=user.source,
                createdat=user.createdat,
                updatedat=user.updatedat
            )

            roles = session.execute(text(role_query), {
                'userid': u.id,
            }).mappings().fetchall()

            roles = [Role(id=role.role) for role in roles]
            u.roles = roles

            return u

from typing import Dict, List
from src.models.settings.connection import db_connection_handler
from src.models.entities.users import Users
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound
from src.errors.error_types.http_conflict import HttpConflictError

class UsersRepository:
    def insert_user(self, usersInfo: Dict) -> Dict:
        with db_connection_handler as database:
            try:
                user = Users(
                    id=usersInfo.get("uuid"),
                    name = usersInfo.get("name"),
                    email = usersInfo.get("email"),
                    company_name = usersInfo.get("company_name"),
                )
                database.session.add(user)
                database.session.commit()

                return usersInfo
            except IntegrityError as e:
                print(user)
                print(e)
                raise HttpConflictError('Usuário ja cadastrado!')
            except Exception as exception:
                database.session.rollback()
                print(exception)
                raise exception

    def get_user_by_id(self, user_id: str) -> Users:
        with db_connection_handler as database:
            try:
                user = (
                    database.session
                        .query(Users)
                        .filter(Users.id==user_id)
                        .one()
                )
                return user
            except NoResultFound:
                return None
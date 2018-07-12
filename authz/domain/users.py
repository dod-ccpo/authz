from sqlalchemy.orm.exc import NoResultFound

from authz.database import db
from authz.models import User

from .roles import Roles
from .exceptions import NotFoundError


class Users(object):

    @classmethod
    def update(cls, user_id, atat_role_name):

        user = Users.get(user_id)
        atat_role = Roles.get(atat_role_name)
        user.atat_role = atat_role

        db.session.add(user)
        db.session.commit()

        return user

    @classmethod
    def get(cls, user_id):
        try:
            user = User.query.filter_by(id=user_id).one()
        except NoResultFound:
            raise NotFoundError("user")

        return user

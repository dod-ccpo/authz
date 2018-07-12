from sqlalchemy.orm.exc import NoResultFound

from authz.database import db
from authz.models import Role
from .exceptions import NotFoundError


class Roles(object):

    @classmethod
    def get(cls, role_name):
        try:
            role = Role.query.filter_by(name=role_name).one()
        except NoResultFound:
            raise NotFoundError("role")

        return role

from flask import Blueprint, jsonify, abort, request

from authz.models import Role
from authz.serializers.role import RoleSerializer

api = Blueprint('api', __name__)


@api.route('/roles')
def get_roles():
    roles = Role.query.all()
    return RoleSerializer().jsonify(roles, many=True)

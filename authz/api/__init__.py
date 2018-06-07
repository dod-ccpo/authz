from flask import Blueprint, jsonify, abort, request

from authz.models import Role, User, WorkspaceRole
from authz.serializers.role import RoleSerializer
from authz.serializers.user import UserSerializer


api = Blueprint('api', __name__)


@api.route('/roles')
def get_roles():
    roles = Role.query.all()
    return RoleSerializer().jsonify(roles, many=True)


@api.route('/workspaces/<uuid:workspace_id>/users')
def get_workspace_users(workspace_id):
    workspace_roles = WorkspaceRole.query.filter(
        WorkspaceRole.workspace_id == workspace_id)
    users = set(wr.user for wr in workspace_roles)
    return UserSerializer().jsonify(users, many=True)

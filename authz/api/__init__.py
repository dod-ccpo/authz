from flask import Blueprint, jsonify, abort, request, Response

from authz.serializers.role import RoleSerializer
from authz.serializers.user import UserSerializer
from authz.serializers.workspace_user import WorkspaceUserSerializer

from authz.domain.exceptions import NotFoundError, AlreadyExistsError
from authz.domain.workspace_users import WorkspaceUsers
from authz.domain.users import Users
from authz.domain.roles import Roles

api = Blueprint("api", __name__)


@api.route("/roles")
def get_roles():
    """
    Returns a list of all existing roles.

    GET /roles
    """

    roles = Roles.get_all()
    return RoleSerializer().jsonify(roles, many=True)


@api.route("/roles/<string:name>")
def get_role(name):
    """
    Returns a given role.

    GET /roles/<role name>
    """

    try:
        role = Roles.get(name)
    except NotFoundError as e:
        return (jsonify({"error": e.message}), 404)

    return RoleSerializer().jsonify(role)


@api.route("/users", methods=["POST"])
def create_user():
    """
    Creates a new atat user with the given role.

    POST /users/
    {
        id: <user id>,
        atat_role: <name of an atat role>
    }

    Returns the created user.
    """
    new_user_dict = request.json

    try:
        new_user = Users.create(new_user_dict["id"], new_user_dict["atat_role"])
    except AlreadyExistsError:
        return (jsonify({"error": "User already exists."}), 409)

    return UserSerializer().jsonify(new_user), 201


@api.route("/users/<uuid:user_id>", methods=["PUT"])
def update_user(user_id):
    """
    Update a user's atat role.

    PUT /users/<user id>
    {
        atat_role: <name of an atat role>
    }

    Returns the updated user.
    """
    atat_role_name = request.json["atat_role"]

    try:
        updated_user = Users.update(user_id, atat_role_name)
    except NotFoundError as e:
        return (jsonify({"error": e.message}), 404)

    return UserSerializer().jsonify(updated_user)


@api.route("/workspaces/<uuid:workspace_id>/users", methods=["PUT"])
def update_workspace_users(workspace_id):
    """
    Add or update users' workspace roles in a given workspace.

    PUT /workspaces/<workspace id>/users
    {
        'users': [
            {'id': '', 'workspace_role': 'developer'}
        ]
    }

    Returns a list of users who have roles in the given workspace.
    """

    workspace_users_to_update = request.json["users"]

    try:
        workspace_users = WorkspaceUsers.add_many(
            workspace_id, workspace_users_to_update
        )
    except NotFoundError as e:
        return (jsonify({"error": e.message}), 404)

    return WorkspaceUserSerializer().jsonify(workspace_users, many=True)


@api.route("/workspaces/<uuid:workspace_id>/users/<uuid:user_id>", methods=["GET"])
def get_workspace_user(workspace_id, user_id):
    """
    Get a user, along with that user's permissions in the given workspace.

    GET /workspaces/<workspace id>/users/<user id>

    Returns a workspace user.
    """
    try:
        workspace_user = WorkspaceUsers.get(workspace_id, user_id)
    except NotFoundError as e:
        return (jsonify({"error": e.message}), 404)

    return WorkspaceUserSerializer().jsonify(workspace_user)

from flask import Blueprint, jsonify, abort, request, Response
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import IntegrityError

from authz.models import Role, User, WorkspaceRole
from authz.serializers.role import RoleSerializer
from authz.serializers.user import UserSerializer
from authz.serializers.workspace_user import WorkspaceUserSerializer
from authz.database import db

from authz.domain.exceptions import NotFoundError
from authz.domain.workspace_users import WorkspaceUser

api = Blueprint("api", __name__)


@api.route("/roles")
def get_roles():
    """
    Returns a list of all existing roles.

    GET /roles
    """
    roles = Role.query.all()
    return RoleSerializer().jsonify(roles, many=True)


@api.route("/roles/<string:name>")
def get_role(name):
    try:
        role = Role.query.filter_by(name=name).one()
    except NoResultFound:
        abort(404)
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
    user_dict = request.json

    try:
        atat_role = Role.query.filter_by(name=user_dict["atat_role"]).one()
    except NoResultFound:
        abort(
            Response(
                {"error": "Role {} not found.".format(user_dict["atat_role"])}, 404
            )
        )

    try:
        user = User(id=user_dict["id"], atat_role=atat_role)
        db.session.add(user)
        db.session.commit()
    except IntegrityError:
        abort(Response({"error": "User {} already exists.".format(user.id)}, 409))

    return UserSerializer().jsonify(user), 201


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
    user_dict = request.json

    try:
        user = User.query.filter_by(id=user_id).one()
    except NoResultFound:
        abort(Response({"error": "User {} not found.".format(user_id)}, 404))

    try:
        atat_role = Role.query.filter_by(name=user_dict["atat_role"]).one()
    except NoResultFound:
        abort(
            Response(
                {"error": "Role {} not found.".format(user_dict["atat_role"])}, 404
            )
        )

    user.atat_role = atat_role
    db.session.add(user)
    db.session.commit()

    return UserSerializer().jsonify(user)


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
        workspace_users = WorkspaceUser.add_many(workspace_id, workspace_users_to_update)
    except NotFoundError as e:
        return (jsonify({"error": e.message}), 404)

    return WorkspaceUserSerializer().jsonify(workspace_users, many=True)


@api.route("/workspaces/<uuid:workspace_id>/users/<uuid:user_id>", methods=["GET"])
def get_workspace_user(workspace_id, user_id):
    """
    Get a user, along with that user's permissions in the given workspace.

    GET /workspaces/<workspace id>/users/<user id>

    Returns a user.
    """
    try:
        workspace_user = WorkspaceUser.get(workspace_id, user_id)
    except NotFoundError as e:
        return (jsonify({"error": e.message}), 404)

    return WorkspaceUserSerializer().jsonify(workspace_user)

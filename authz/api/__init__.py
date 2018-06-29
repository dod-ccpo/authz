from flask import Blueprint, jsonify, abort, request, Response
from sqlalchemy.orm.exc import NoResultFound

from authz.models import Role, User, WorkspaceRole
from authz.serializers.role import RoleSerializer
from authz.serializers.user import UserSerializer
from authz.database import db

api = Blueprint("api", __name__)


@api.route("/roles")
def get_roles():
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
    user_dict = request.json

    try:
        atat_role = Role.query.filter_by(name=user_dict["atat_role"]).one()
    except NoResultFound:
        abort(
            Response(
                {"error": "Role {} not found.".format(user_dict["atat_role"])}, 404
            )
        )

    user = User(id=user_dict["id"], atat_role=atat_role)
    db.session.add(user)
    db.session.commit()

    return UserSerializer().jsonify(user)


@api.route("/users/<uuid:user_id>", methods=["PUT"])
def update_user(user_id):
    user_dict = request.json

    try:
        user = User.query.filter_by(id=user_id).one()
    except NoResultFound:
        abort(
            Response(
                {"error": "User {} not found.".format(user_id)}, 404
            )
        )

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
    {
        'users': [
            {'id': '', 'workspace_role': 'developer'}
        ]
    }
    """

    workspace_users_to_update = request.json["users"]
    for user_dict in workspace_users_to_update:
        try:
            user = User.query.filter_by(id=user_dict["id"]).one()
        except NoResultFound:
            default_role = Role.query.filter_by(name="developer").one_or_none()
            user = User(id=user_dict["id"], atat_role=default_role)

        try:
            role = Role.query.filter_by(name=user_dict["workspace_role"]).one()
        except NoResultFound:
            abort(
                Response(
                    {"error": "Role {} not found.".format(user_dict["workspace_role"])},
                    404,
                )
            )

        user.workspace_roles.append(
            WorkspaceRole(user=user, role_id=role.id, workspace_id=workspace_id)
        )

        db.session.add(user)

    db.session.commit()

    workspace_users = User.query.join(WorkspaceRole).filter(
        WorkspaceRole.workspace_id == workspace_id
    )
    return UserSerializer().jsonify(workspace_users, many=True)


@api.route("/workspaces/<uuid:workspace_id>/users/<uuid:user_id>", methods=["GET"])
def get_workspace_user(workspace_id, user_id):
    try:
        user = User.query.filter_by(id=user_id).one()
    except NoResultFound:
        abort(Response({"error": "User {} not found.".format(user_id)}, 404))

    atat_permissions = set(user.atat_role.permissions)
    try:
        workspace_role = (
            WorkspaceRole.query.join(User)
            .filter(User.id == user_id, WorkspaceRole.workspace_id == workspace_id)
            .one()
        )
        workspace_permissions = workspace_role.role.permissions
    except NoResultFound:
        workspace_permissions = []

    user.permissions = set(workspace_permissions).union(atat_permissions)
    return UserSerializer().jsonify(user)

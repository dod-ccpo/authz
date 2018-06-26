from flask import Blueprint, jsonify, abort, request
from sqlalchemy.orm.exc import NoResultFound

from authz.models import Role, User, WorkspaceRole
from authz.serializers.role import RoleSerializer

api = Blueprint('api', __name__)


@api.route('/roles')
def get_roles():
    roles = Role.query.all()
    return RoleSerializer().jsonify(roles, many=True)


@api.route('/roles/<string:name>')
def get_role(name):
    try:
        role = Role.query.filter_by(name=name).one()
    except NoResultFound:
        return abort(404)
    return RoleSerializer().jsonify(role)


@api.route('/workspaces/<uuid:workspace_id>/users', methods=['PUT'])
def update_workspace_users(workspace_id):
    request_json = request.get_json()
    return jsonify(request_json)


@api.route('/workspaces/<uuid:workspace_id>/users')
def get_workspace_users(workspace_id):
    workspace_id = str(workspace_id)
    return jsonify({
        'users': {
            '04d27fc6-f019-4ac2-9677-5089b424f32a': { # user_id
                'roles': ['owner'],
                'atat_permissions': [
                    'request_jedi_workspace'
                ],
                'workspace_permissions': {
                    workspace_id: [
                        'view_usage_report',
                        'view_usage_dollars',
                        'spin_up_resources',
                        'pause_resources',
                        'delete_resources',
                        'modify_resources'
                    ]
                }
            },
            'c2249d0b-0ef7-42a5-a4bc-c0301603405b': {
                'roles': ['ccpo'],
                'atat_permissions': [
                    'review_jedi_workspace_request',
                    'modify_atat_role_permissions',
                    'create_csp_role',
                    'delete_csp_role',
                    'modify_csp_role_permissions'
                ],
                'workspace_permissions': {
                    workspace_id: [
                    ]
                }
            },
            'b2879be8-8497-4757-95d4-05f596f65637': {
                'roles': ['developer'],
                'atat_permissions': [],
                'workspace_permissions': {
                    workspace_id: [
                        'view_usage_report',
                        'view_application',
                        'view_application_environment'
                    ]
                },
            },
    }})

from marshmallow import fields

from . import marshmallow
from .user import UserSerializer


class WorkspaceUserSerializer(marshmallow.ModelSchema):

    workspace_id = fields.UUID()
    permissions = fields.List(fields.String)
    user = fields.Nested(UserSerializer)

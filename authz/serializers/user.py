from . import marshmallow
from marshmallow import fields
from authz.models import User


class UserSerializer(marshmallow.ModelSchema):
    class Meta:
        model = User

    permissions = fields.List(fields.String)

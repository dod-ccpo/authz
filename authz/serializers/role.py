from . import marshmallow
from authz.models import Role

class RoleSerializer(marshmallow.ModelSchema):
    class Meta:
        model = Role

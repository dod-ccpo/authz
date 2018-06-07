from . import marshmallow
from authz.models import User

class UserSerializer(marshmallow.ModelSchema):
    class Meta:
        model = User

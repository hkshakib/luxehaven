from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializers


class UserCreateSerializer(BaseUserCreateSerializers):
    class Meta(BaseUserCreateSerializers.Meta):
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']

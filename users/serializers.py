from rest_framework import serializers
from users.models import User
from users.validators import CustomEmailValidator, CustomMinimumLengthValidator, CustomNumericPasswordValidator


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}
        fields = ('username', 'email', 'password', 'birthdate')

        validators = [CustomEmailValidator(field='model'),
                      CustomNumericPasswordValidator(field='model'),
                      CustomMinimumLengthValidator(field='model')]


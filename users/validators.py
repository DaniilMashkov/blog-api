from django.contrib.auth.password_validation import MinimumLengthValidator, NumericPasswordValidator
from django.core.validators import EmailValidator
from rest_framework import serializers


class CustomEmailValidator(EmailValidator):

    def __init__(self, field):
        super().__init__(field)

    def __call__(self, value):
        domain = value.get('email').split('@')[1]
        if domain not in ['mail.ru', 'yandex.ru']:
            raise serializers.ValidationError('Only mail.ru & yandex.ru domains allowed')


class CustomMinimumLengthValidator(MinimumLengthValidator):

    def __init__(self, field):
        self.field = field
        super().__init__()

    def __call__(self, value):
        user_password = value.get('password')
        self.validate(user_password)


class CustomNumericPasswordValidator(NumericPasswordValidator):

    def __init__(self, field):
        self.field = field
        super().__init__()

    def __call__(self, value):

        user_password = value.get('password')
        self.validate(user_password)

        if user_password.isalpha():
            raise serializers.ValidationError('Your password can’t be entirely alphabet')






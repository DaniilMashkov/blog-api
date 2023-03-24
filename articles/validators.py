from rest_framework import serializers
from datetime import datetime as dt


class ArticleValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        validation_errors = []

        user_birthdate = dt.strftime(value.get('user').birthdate, '%Y, %M, %d')
        current_date = dt.strftime(dt.now(), '%Y, %M, %d')

        forbidden_words = ['ерунда', 'глупость', 'чепуха']

        time_delta = dt.strptime(current_date, '%Y, %M, %d') - dt.strptime(user_birthdate, '%Y, %M, %d')

        if time_delta.days < 6574:
            validation_errors.append('Author must be older 18')

        if any(word in value.get('title') for word in forbidden_words):
            validation_errors.append('Forbidden word in title')

        if validation_errors:
            raise serializers.ValidationError(validation_errors)




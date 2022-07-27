import datetime

from django.core.exceptions import ValidationError
from django.test import TestCase

from french_bulldog_store.auth_app.models import FrenchieUser


class FrenchieUserTest(TestCase):
    VALID_USER_DATA = {
        'username': 'testov',
        'date_joined': datetime.datetime.now(),
    }

    def test_username_min_length(self):
        username = 'test'

        user = FrenchieUser(
            username=username,
            date_joined=self.VALID_USER_DATA['date_joined'],
        )

        with self.assertRaises(ValidationError) as context:
            user.full_clean()
            user.save()

        self.assertIsNotNone(context.exception)


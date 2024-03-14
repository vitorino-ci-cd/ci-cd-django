from django.test import TestCase
from django.contrib.auth.models import User


class UserTestCase(TestCase):
    def test_user(self):
        username = 'Vitorino'
        password = 'N@Ti'
        usuario = User(username=username)
        usuario.set_password(password)
        usuario.save()
        self.assertEqual(usuario.username, username)
        self.assertTrue(usuario.check_password(password))
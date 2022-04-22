from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successfull(self):
        """Test creating a new user with email and is suceesfull"""

        email = 'rish@gmail.com'
        password = 'testpass123'

        user = get_user_model().objects.create_user(
            email = email, password = password
        )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password),password)

    def test_create_user_with_email_lower_case(self):
        """Test creating a new user with email as lower case"""

        email = 'rish@GMAIL.com'
        password = 'testpass123'

        user = get_user_model().objects.create_user(
            email = email, password = password
        )

        self.assertEqual(user.email,email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email error"""
        with self.assertRaises(ValueError):
            user = get_user_model().objects.create_user(
            email = None, password = 'mxc sa csc'
        )

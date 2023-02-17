from django.test import TestCase

from django.contrib.auth import get_user_model


class ModelTest(TestCase):
    def test_create_user_with_email_successful(self):
        email="example@gmail.com"
        password="root"
        user=get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))

    def test_user_email_normalized(self):
        sample_email = [
            ['test1@EXAMPLE.com','test1@example.com'],
            ['Test2@Example.com','Test2@example.com'],
            ['test3@example.COM','test3@example.com']
        ]
        for email, expected in sample_email:
            user = get_user_model().objects.create_user(email,'pass123')
            self.assertEqual(user.email,expected)

    def test_raise_value_error_on_not_providing_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('','pass123')

    def test_create_superuser(self):
        user = get_user_model().objects.create_superuser(
            'root@gmail.com',
            'root'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
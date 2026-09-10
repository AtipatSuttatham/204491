import pytest
from django.contrib.auth import get_user_model
from django.db import IntegrityError

from accounts.models import Role

User = get_user_model()


@pytest.mark.django_db
def test_create_user_defaults_to_student():
    user = User.objects.create_user(email="stu@example.com", password="x")
    assert user.role == Role.STUDENT
    assert user.is_email_verified is False
    assert user.is_staff is False
    assert user.check_password("x")


@pytest.mark.django_db
def test_create_superuser_is_admin_and_verified():
    admin = User.objects.create_superuser(email="admin@example.com", password="x")
    assert admin.role == Role.ADMIN
    assert admin.is_staff and admin.is_superuser
    assert admin.is_email_verified is True


@pytest.mark.django_db
def test_email_is_unique():
    User.objects.create_user(email="dup@example.com", password="x")
    with pytest.raises(IntegrityError):
        User.objects.create_user(email="dup@example.com", password="y")

"""
Accounts — User (custom) + EmailVerificationToken
ดู docs/database.md §3 · CLAUDE.md "Authentication"
"""

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from common.models import Auditable, TimeStampedModel


class Role(models.TextChoices):
    ADMIN = "admin", _("Administrator")
    TEACHER = "teacher", _("Teacher")
    STUDENT = "student", _("Student")


class UserManager(BaseUserManager):
    """
    ไม่มี username — identifier คือ email (สมัครเอง) หรือ student_or_staff_id (Admin สร้าง)
    """

    use_in_migrations = True

    def _create_user(self, email, password, **extra):
        if not email:
            raise ValueError("ต้องมี email")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra):
        extra.setdefault("role", Role.STUDENT)
        extra.setdefault("is_staff", False)
        extra.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra)

    def create_superuser(self, email, password=None, **extra):
        extra.setdefault("role", Role.ADMIN)
        extra["is_staff"] = True
        extra["is_superuser"] = True
        extra["is_email_verified"] = True
        return self._create_user(email, password, **extra)


class User(AbstractBaseUser, PermissionsMixin, Auditable, TimeStampedModel):
    email = models.EmailField(_("email address"), unique=True)
    student_or_staff_id = models.CharField(
        _("student / staff ID"), max_length=32, unique=True, null=True, blank=True
    )

    role = models.CharField(max_length=16, choices=Role.choices, default=Role.STUDENT)

    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    first_name_en = models.CharField(_("first name (EN)"), max_length=150, blank=True)
    last_name_en = models.CharField(_("last name (EN)"), max_length=150, blank=True)

    is_email_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    avatar_url = models.URLField(blank=True)

    created_by = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.SET_NULL, related_name="created_users"
    )
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "accounts_user"

    def __str__(self):
        return self.student_or_staff_id or self.email

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip()


class TokenPurpose(models.TextChoices):
    VERIFY_EMAIL = "verify_email", _("Verify email")
    RESET_PASSWORD = "reset_password", _("Reset password")


class EmailVerificationToken(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="verification_tokens")
    token = models.CharField(max_length=64, unique=True)
    purpose = models.CharField(max_length=16, choices=TokenPurpose.choices)
    expires_at = models.DateTimeField()
    used_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "accounts_email_verification_token"
        indexes = [models.Index(fields=["token", "purpose"])]

    def __str__(self):
        return f"{self.get_purpose_display()} · {self.user}"

    @property
    def is_valid(self):
        return self.used_at is None and self.expires_at > timezone.now()

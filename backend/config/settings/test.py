"""Test settings — ใช้โดย pytest (ดู pyproject.toml [tool.pytest.ini_options])."""

from .base import *  # noqa: F403

DEBUG = False

# hash เร็วขึ้นตอนรันเทสต์
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

# CI ไม่มี Postgres เสมอไป — อนุญาตให้ override ผ่าน DATABASE_URL,
# ค่า default ตรงกับ service ใน GitHub Actions

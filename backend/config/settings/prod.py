"""
Production settings — ยังไม่ผูกกับ hosting provider ใด (ดู CLAUDE.md "Hosting")
ค่าทั้งหมดมาจาก environment variables เท่านั้น
"""

from .base import *  # noqa: F403

DEBUG = False

# ต้องกำหนดผ่าน env เสมอ — ไม่มี default ที่ปลอดภัย
SECRET_KEY = env("DJANGO_SECRET_KEY")  # noqa: F405
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS")  # noqa: F405

# HTTPS / security headers — เปิดเมื่อ deploy หลัง reverse proxy ที่มี TLS
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = env.bool("DJANGO_SECURE_SSL_REDIRECT", default=True)  # noqa: F405
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = env.int("DJANGO_SECURE_HSTS_SECONDS", default=0)  # noqa: F405

"""Development settings."""

from .base import *  # noqa: F403

DEBUG = True

INSTALLED_APPS += []  # noqa: F405  (เผื่อ debug toolbar ในอนาคต)

# dev: อนุญาต localhost ทุกพอร์ต
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "0.0.0.0"]

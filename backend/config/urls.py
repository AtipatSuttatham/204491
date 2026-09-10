from django.contrib import admin
from django.http import JsonResponse
from django.urls import path


def health(_request):
    """Health check — ใช้โดย CI / uptime monitor."""
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/health/", health, name="health"),
    # path("api/auth/", include("accounts.urls")),   # slice: Authentication
]

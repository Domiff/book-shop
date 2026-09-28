from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import BookViewSet

app_name = "api"

router = DefaultRouter()
router.register(r"book", BookViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

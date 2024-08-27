from .views import AuthViewSet

# from .views import LoginViewSet, LogoutViewSet, RegisterViewSet
from rest_framework.routers import DefaultRouter

app_name = "accounts"

router = DefaultRouter()
router.register("auth", AuthViewSet, basename="auth")



urlpatterns = router.urls
from rest_framework import routers

from . import views

router = routers.DefaultRouter()

router.register(prefix='profile', viewset=views.ProfileViewSet, basename='profile')

urlpatterns = router.urls
from rest_framework_nested import routers

from . import views

router = routers.DefaultRouter()

router.register(prefix='profile', viewset=views.ProfileViewSet, basename='profile')
router.register(prefix='education', viewset=views.EducationViewSet, basename='education')
router.register(prefix='experience', viewset=views.ExperienceViewSet, basename='experience')


# education_router = routers.NestedDefaultRouter(router, parent_prefix='profile', lookup='profile')
# education_router.register('education', views.EducationViewSet, 'education')


# experience_router = routers.NestedDefaultRouter(router, parent_prefix='profile', lookup='profile')
# experience_router.register('experience', views.ExperienceViewSet, 'experience')

urlpatterns = router.urls
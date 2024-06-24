from rest_framework_nested import routers

from . import views

router = routers.DefaultRouter()

router.register(prefix='profile', viewset=views.ProfileViewSet, basename='profile')

education_router = routers.NestedDefaultRouter(router, parent_prefix='profile', lookup='profile')
education_router.register('education', views.EducationViewSet, 'education')


experience_router = routers.NestedDefaultRouter(router, parent_prefix='profile', lookup='profile')
experience_router.register('experience', views.ExperienceViewSet, 'experience')

urlpatterns = router.urls + education_router.urls + experience_router.urls
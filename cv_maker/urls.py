from rest_framework_nested import routers
from django.urls import include, path
from . import views

router = routers.DefaultRouter()

router.register(prefix='cv', viewset=views.ProfileViewSet, basename='cv')
# router.register(prefix='education', viewset=views.EducationViewSet, basename='education')
# router.register(prefix='experience', viewset=views.ExperienceViewSet, basename='experience')


# education_router = routers.NestedDefaultRouter(router, parent_prefix='profile', lookup='profile')
# education_router.register('education', views.EducationViewSet, 'education')


# experience_router = routers.NestedDefaultRouter(router, parent_prefix='profile', lookup='profile')
# experience_router.register('experience', views.ExperienceViewSet, 'experience')

urlpatterns = [
    path('degree-choices/', views.DegreeChoicesAPIView.as_view(), name='degree-choice')
]

urlpatterns += router.urls
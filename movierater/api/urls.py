from django.urls import include, re_path
from rest_framework import routers
from movierater.api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'movies', views.MovieViewSet)


urlpatterns = [
    re_path(r'^', include(router.urls)),
    re_path(r'^authenticate', views.CustomObtainAuthToken.as_view()),
]

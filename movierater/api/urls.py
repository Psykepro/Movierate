from django.urls import include, re_path
from rest_framework import routers
from movierater.api import views

ROUTER = routers.DefaultRouter()
ROUTER.register(r'users', views.UserViewSet)
ROUTER.register(r'movies', views.MovieViewSet)
ROUTER.register(r'ratings', views.RatingViewSet)


urlpatterns = [
    re_path(r'^', include(ROUTER.urls)),
    re_path(r'^authenticate', views.CustomObtainAuthToken.as_view()),
]

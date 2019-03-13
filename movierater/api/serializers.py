from django.contrib.auth.models import User
from movierater.api.models import Movie, Rating
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email')


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', 'description')

class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ('stars', 'movie', 'user')

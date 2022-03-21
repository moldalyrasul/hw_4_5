from rest_framework import serializers
from movie_app.models import Director, Movie, Review
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name '.split()


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = 'id title description duration director_id reviews rating'.split()


class DirectorCountSerializer(serializers.ModelSerializer):
    movie_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = 'movie_count'.split()

    def get_movie_count(self, movie):
        return movie.all().count()



class DirectorCreatUpdateSerializer(serializers.Serializer):
    name = serializers.CharField()

    def velidate_director_id(self, director_id):
        if Director.objects.filter(id=director_id).count() == 0:
            raise ValidationError(f'Director with id={director_id} not found!')
        return director_id


class MovieCreateUpdateSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    duration = serializers.IntegerField()
    director = serializers.IntegerField()

    def validate_movie_id(self, movie_id):
        if Movie.objects.filter(id=movie_id).count() == 0:
            raise ValidationError(f'Movie with id={movie_id} not found!')
        return movie_id


class ReviewCreateUpdateSerializer(serializers.Serializer):
    text = serializers.CharField()
    movie = serializers.IntegerField()
    stars = serializers.IntegerField()

    def validate_reviews_id(self, reviews_id):
        if Review.objects.filter(id=reviews_id).count() == 0:
            raise ValidationError(f'Reviews with id={reviews_id} not found!')
        return reviews_id

class UserValidateSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate_username(self, username):
        if User.objects.filter(username=username):
            raise ValidationError('User already exists!!!')
        return username


class UserAuthorizationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


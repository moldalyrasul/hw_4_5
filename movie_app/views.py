from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.serializers import *
from movie_app.models import *
from rest_framework import status


@api_view(['GET'])
def directors_list_view(request):
    if request.method == 'GET':
        director = Director.objects.all()
        data = DirectorSerializer(director, many=True).data
        return Response(data=data)


@api_view(['GET'])
def directors_detail_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'massage': 'Director not found'})
    data = DirectorSerializer(director).data
    return Response(data=data)



@api_view(['GET'])
def movie_list_view(request):
    if request.method == 'GET':
        movie = Movie.objects.all()
        data = MovieSerializer(movie, many=True).data
        return Response(data=data)


@api_view(['GET'])
def movie_detail_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'massage': 'Movie not found'})
    data = MovieSerializer(movie).data
    return Response(data=data)


@api_view(['GET'])
def review_list_view(request):
    if request.method == 'GET':
        review = Review.objects.all()
        data = ReviewSerializer(review, many=True).data
        return Response(data=data)



@api_view(['GET'])
def review_detail_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'massage': 'Movie not found'})
    data = ReviewSerializer(review).data
    return Response(data=data)


@api_view(['GET'])
def movies_reviews_view(request):
    movie_reviews = Movie.objects.all()
    data = MovieSerializer(movie_reviews, many=True).data
    return Response(data=data)


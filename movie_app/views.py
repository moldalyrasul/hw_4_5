from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.serializers import *
from movie_app.models import *
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView



# @api_view(['GET', 'POST'])
# def directors_list_create_view(request):
#     if request.method == 'GET':
#         director = Director.objects.all()
#         data = DirectorSerializer(director, many=True).data
#         return Response(data=data)
#     elif request.method == 'POST':
#         serializer = DirectorCreatUpdateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(data={'errors': serializer.errors},
#                             status=status.HTTP_406_NOT_ACCEPTABLE)
#         name = request.data.get('name')
#         director = Director.objects.create(name=name)
#         return Response(data=DirectorSerializer(director).data,
#                         status=status.HTTP_201_CREATED)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def directors_detail_view(request, id):
#     try:
#         director = Director.objects.get(id=id)
#     except Director.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND, data={'massage': 'Director not found'})
#     # data = DirectorSerializer(director).data
#     # return Response(data=data)
#     if request.method == 'GET':
#         data = DirectorSerializer(director).data
#         return Response(data=data)
#     elif request.method == 'DELETE':
#         director.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     elif request.method == 'PUT':
#         director.name = request.data.get('name')
#         director.save()
#         return Response(data=DirectorSerializer(director).data)
#
#
# @api_view(['GET', 'POST'])
# def movie_list_view(request):
#     if request.method == 'GET':
#         movie = Movie.objects.all()
#         data = MovieSerializer(movie, many=True).data
#         return Response(data=data)
#     elif request.method == 'POST':
#         print(request.data)
#         title = request.data.get('title')
#         description = request.data.get('description')
#         duration = request.data.get('duration')
#         director = request.data.get('director')
#         movie = Movie.objects.create(title=title, description=description, duration=duration, director=director)
#         return Response(data=MovieSerializer(movie).data,
#                         status=status.HTTP_201_CREATED)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_detail_view(request, id):
#     try:
#         movie = Movie.objects.get(id=id)
#     except Movie.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND, data={'massage': 'Movie not found'})
#     if request.method == 'GET':
#         data = MovieSerializer(movie).data
#         return Response(data=data)
#     elif request.method == 'DELETE':
#         Movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     elif request.method == 'PUT':
#         movie.text = request.data.get('text')
#         movie.description = request.data.get('description')
#         movie.duration = request.data.get('duration')
#         movie.director = request.data.get('director')
#         movie.save()
#         return Response(data=MovieSerializer(movie).data)
#
#
# @api_view(['GET', 'POST'])
# def review_list_view(request):
#     if request.method == 'GET':
#         review = Review.objects.all()
#         data = ReviewSerializer(review, many=True).data
#         return Response(data=data)
#     elif request.method == 'POST':
#         print(request.data)
#         text = request.data.get('text')
#         movie = request.data.get('movie')
#         stars = request.data.get('stars')
#         review = Review.objects.create(text=text, movie=movie, stars=stars)
#         return Response(data=ReviewSerializer(review).data,
#                         status=status.HTTP_201_CREATED)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def review_detail_view(request, id):
#     try:
#         review = Review.objects.get(id=id)
#     except Review.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND, data={'massage': 'Movie not found'})
#
#     if request.method == 'GET':
#         data = ReviewSerializer(review).data
#         return Response(data=data)
#     elif request.method == 'DELETE':
#         review.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     elif request.method == 'PUT':
#         review.text = request.data.get('text')
#         review.movie = request.data.get('movie')
#         review.stars = request.data.get('stars')
#         review.save()
#         return Response(data=MovieSerializer(review).data)
#
#
# @api_view(['GET'])
# def movies_reviews_view(request):
#     movie_reviews = Movie.objects.all()
#     data = MovieSerializer(movie_reviews, many=True).data
#     return Response(data=data)
# #
# @api_view(['POST'])
# def registration(request):
#     serializer = UserValidateSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     User.objects.create_user(**serializer.validated_data)
#     return Response(data={'message': 'User created'})
#
#
# @api_view(['POST'])
# def authorization(request):
#     serializer = UserAuthorizationSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     username = request.data.get('username')
#     password = request.data.get('password')
#     user = authenticate(username=username, password=password)
#     if user:
#         try:
#             token = Token.objects.get(user=user)
#         except Token.DoesNotExist:
#             token = Token.objects.create(user=user)
#         return Response(data={'key': token.key})
#     return Response(data={'message': 'User not found'},
#                     status=404)


class DirectorListCreateAPIView(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    pagination_class = PageNumberPagination



class DirectorItemAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorCreatUpdateSerializer



class MovieListView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = PageNumberPagination


class MovieItemAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieCreateUpdateSerializer



class ReviewListAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewItemAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewCreateUpdateSerializer


class MovieCountAPIView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = DirectorCountSerializer
    pagination_class = PageNumberPagination


class RegisterAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        User.objects.create_user(**serializer.validated_data)
        return Response(data={'message': 'User created'})


class AuthAPIView(APIView):
    def post(self, request):
        serializer = UserAuthorizationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            try:
                token = Token.objects.get(user=user)
            except Token.DoesNotExist:
                token = Token.objects.create(user=user)
            return Response(data={'key': token.key})
        return Response(data={'message': 'User not found'},
                        status=404)


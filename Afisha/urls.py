from django.contrib import admin
from django.urls import path
from movie_app import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/v1/directors/', views.DirectorListCreateAPIView.as_view()),
    path('api/v1/directors/<int:pk>/', views.DirectorItemAPIView.as_view()),
    path('api/v1/movies/', views. MovieListView.as_view()),
    path('api/v1/movies/<int:pk>/', views.MovieItemAPIView.as_view()),
    path('api/v1/reviews/', views.ReviewListAPIView.as_view()),
    path('api/v1/reviews/<int:pk>/', views.ReviewItemAPIView.as_view()),
    path('api/v1/movies/reviews/', views.MovieCountAPIView.as_view()),
    path('api/v1/register/', views.RegisterAPIView.as_view()),
    path('api/v1/login/', views.AuthAPIView.as_view())

]




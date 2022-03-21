from django.contrib import admin
from django.urls import path
from movie_app import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/v1/directors/', views.directors_list_create_view),
    path('api/v1/directors/<int:id>/', views.directors_detail_view),
    path('api/v1/movies/', views.movie_list_view),
    path('api/v1/movies/<int:id>/', views.movie_detail_view),
    path('api/v1/reviews/', views.review_list_view),
    path('api/v1/reviews/<int:id>/', views.review_detail_view),
    path('api/v1/movies/reviews/', views.movies_reviews_view),
    path('api/v1/register/', views.registration),
    path('api/v1/login/', views.authorization)

]


from django.urls import path
from e_commerce.marvel_views import *
from django.contrib.auth.views import LoginView

#from e_commerce.views import LoginView

# Importamos las API_VIEWS:
from e_commerce.api.views import *


urlpatterns = [
    # Comic Function API View:
    path('login/', LoginView.as_view(), name='login'),
    path('comic-list/', comic_list_api_view),
    path('comic-retrieve/', comic_retrieve_api_view),
    path('comic-create/', comic_create_api_view),
    # Comic Class API View:
    path('comics/list/', GetComicAPIView.as_view()),
    path('comics/<int:pk>/', GetOneComicAPIView.as_view()),
    path(
        'comics/comic/<int:marvel_id>/',
        GetOneMarvelComicAPIView.as_view()
    ),
    path('comics/create/', PostComicAPIView.as_view()),
    path('comics/list-create/', ListCreateComicAPIView.as_view()),
    path('comics/update/<int:marvel_id>/', UpdateComicAPIView.as_view()),
    path(
        'comics/retrieve-update/<int:pk>/',
        RetrieveUpdateComicAPIView.as_view()
    ),
    path('comics/delete/<int:pk>/', DestroyComicAPIView.as_view()),

    # **Rutas nuevas para WishList:**
    # Obtener un solo WishList por su ID
    path('wishlist/<int:pk>/', GetWishListAPIView.as_view(), name='get_wishlist_api_view'),
    
    # Crear un nuevo WishList
    path('wishlist/create/', PostWishListAPIView.as_view(), name='post_wishlist_api_view'),
    
    # Actualizar un WishList existente
    path('wishlist/update/<int:pk>/', UpdateWishListAPIView.as_view(), name='update_wishlist_api_view'),
    
    # Eliminar un WishList
    path('wishlist/delete/<int:pk>/', DeleteWishListAPIView.as_view(), name='delete_wishlist_api_view'),


]

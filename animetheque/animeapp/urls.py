from django.urls import path
from . import views, anime_views, studio_views

urlpatterns = [
    path('', views.home),
    path('anime/', anime_views.home),
    path('anime/show/<int:id>/', anime_views.show_anime),
    path('anime/add/', anime_views.add_anime),
    path('anime/processing/', anime_views.processing),
    path('anime/update/<int:id>/', anime_views.update_anime),
    path('anime/processing_update/<int:id>/', anime_views.processing_update),
    path('anime/delete/<int:id>/', anime_views.delete_anime),
    path('studio/', studio_views.home),
    path('studio/add/', studio_views.add_studio),
    path('studio/processing/', studio_views.processing),
    path('studio/show/<int:id>/', studio_views.show_studio),
    path('studio/update/<int:id>/', studio_views.update_studio),
    path('studio/processing_update/<int:id>/', studio_views.processing_update),
    path('studio/delete/<int:id>/', studio_views.delete_studio),
]
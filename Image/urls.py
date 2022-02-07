
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'home'),
    path('image/<str:pk>/', views.viewImage, name = 'image'),
    path('category/<int:category>', views.category, name = 'category'),    
    path('search', views.search, name = 'search'),
    path("upload/", views.upload, name= "upload"),
    path("thanks/", views.thanks, name= "thanks"),
    path("privacy/", views.privacy, name= "privacy"),
    path("licence/", views.licence, name= "licence"),
    path("terms/", views.terms, name= "terms"),
]

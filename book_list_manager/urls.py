from django.urls import path, include
from . import views

urlpatterns = [    
    path('', views.HomeView.as_view(), name="home" ),
    # CRUD views for events and users
    path('books/',views.BookListCreateView.as_view(),name="list-create-books"),
    path('books/<int:pk>/',views.RetrieveUpdateDeleteView.as_view(),name="retrieve-update-delete-books"),
]
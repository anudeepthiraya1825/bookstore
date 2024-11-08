from django.urls import path
from .views import BookListCreate, BookDetail


urlpatterns =[
    path('bookis/',BookListCreate.as_view(), name='book-list-create'),
    path('books/<int:pk>/',BookDetail.as_view(),name='book-detail'),
]
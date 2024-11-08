from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
 

class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
class BookDetail(generics.RetrueveUpdateDestroyAPIView):
    queryset =Book.objects.all()
    serializer_class = BookSerializer
    
# Create your views here.

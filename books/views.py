from rest_framework import generics
from .models import Book
from .serializers import BookSerializer, BookLendSerializer, BookReturnSerializer


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_url_kwarg = 'id'


class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_url_kwarg = 'id'


class BookLendView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookLendSerializer


class BookReturnView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookReturnSerializer

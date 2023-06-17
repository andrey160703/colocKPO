from django.urls import path
from .views import BookListCreateView, BookDetailView, BookListView, BookCreateView, BookUpdateView, BookDeleteView, \
    BookLendView, BookReturnView

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:id>/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:id>/', BookDeleteView.as_view(), name='book-delete'),
    path('lend/<int:bookId>/', BookLendView.as_view(), name='book-lend'),
    path('return/<int:bookId>/', BookReturnView.as_view(), name='book-return'),

]

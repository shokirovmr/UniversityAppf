from django.urls import path
from bookshop.views import (
    HomePageView, PublisherView, StoreListView, StoreDetialView, StoreCreateView,
    AuthorListView, AuthorDetailView, AuthorCreateView, AuthorUpdateView, AuthorDeleteView,
    BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView
)

app_name = "bookshop"
urlpatterns = [
    path("", HomePageView.as_view(), name="home-page"),
    path("publisher/", PublisherView.as_view(), name="publisher-page"),
    path("stores/", StoreListView.as_view(), name="store-list"),
    path("stores/create", StoreCreateView.as_view(), name="store-create"),
    path("stores/<int:pk>", StoreDetialView.as_view(), name="store-detail"),

    # URLs for Author views
    path("authors/", AuthorListView.as_view(), name="author-list"),
    path("authors/<int:pk>", AuthorDetailView.as_view(), name="author-detail"),
    path("authors/create", AuthorCreateView.as_view(), name="author-create"),
    path("authors/<int:pk>/update", AuthorUpdateView.as_view(), name="author-update"),
    path("authors/<int:pk>/delete", AuthorDeleteView.as_view(), name="author-delete"),

    # URLs for Book views
    path("books/", BookListView.as_view(), name="book-list"),
    path("books/<int:pk>", BookDetailView.as_view(), name="book-detail"),
    path("books/create", BookCreateView.as_view(), name="book-create"),
    path("books/<int:pk>/update", BookUpdateView.as_view(), name="book-update"),
    path("books/<int:pk>/delete", BookDeleteView.as_view(), name="book-delete"),
]

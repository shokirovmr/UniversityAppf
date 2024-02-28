from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from bookshop.forms import PublisherCreateForm
from bookshop.models import Publisher, Store, Author, Book


class HomePageView(View):
    def get(self, request):
        return render(request, "bookshop/home.html")


class PublisherView(View):
    def get(self, request):
        publishers = Publisher.objects.all().order_by("-created_at")[:5]
        form = PublisherCreateForm()
        context = {
            "publishers": publishers,
            "form": form
        }
        return render(request, "bookshop/publisher.html", context=context)

    def post(self, request):
        publishers = Publisher.objects.all().order_by("-created_at")[:5]
        form = PublisherCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("bookshop:publisher-page")
        else:
            return render(request, "bookshop/publisher.html", context={
                "publishers": publishers,
                "form": form
            })


class StoreListView(ListView):
    model = Store
    context_object_name = "stores"
    template_name = "bookshop/store_list.html"


class StoreDetialView(DetailView):
    model = Store
    template_name = "bookshop/store_detail.html"
    context_object_name = "store"


class StoreCreateView(CreateView):
    model = Store
    fields = ["name", "books"]
    template_name = "bookshop/store_create.html"


class AuthorListView(ListView):
    model = Author
    context_object_name = "authors"
    template_name = "bookshop/author_list.html"


class AuthorDetailView(DetailView):
    model = Author
    context_object_name = "author"
    template_name = "bookshop/author_detail.html"


class AuthorCreateView(CreateView):
    model = Author
    fields = ["username", "age", "address", "gender"]
    template_name = "bookshop/author_create.html"


class AuthorUpdateView(UpdateView):
    model = Author
    fields = ["username", "age", "address", "gender"]
    template_name = "bookshop/author_update.html"


class AuthorDeleteView(DeleteView):
    model = Author
    context_object_name = "author"
    template_name = "bookshop/author_delete.html"
    success_url = reverse_lazy("bookshop:author-list")


class BookListView(ListView):
    model = Book
    context_object_name = "books"
    template_name = "bookshop/book_list.html"


class BookDetailView(DetailView):
    model = Book
    context_object_name = "book"
    template_name = "bookshop/book_detail.html"


class BookCreateView(CreateView):
    model = Book
    fields = ["name", "pages", "price", "rating", "authors", "publisher", "pubdate"]
    template_name = "bookshop/book_create.html"


class BookUpdateView(UpdateView):
    model = Book
    fields = ["name", "pages", "price", "rating", "authors", "publisher", "pubdate"]
    template_name = "bookshop/book_update.html"


class BookDeleteView(DeleteView):
    model = Book
    context_object_name = "book"
    template_name = "bookshop/book_delete.html"
    success_url = reverse_lazy("bookshop:book-list")

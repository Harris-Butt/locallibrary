from django.shortcuts import render

from catalog.models import Book, Author, BookInstance, Genre, Language
# Create your views here.

def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_genres = Genre.objects.all().count()
    books_with_a = Book.objects.filter(title__icontains='a').count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()
    title = "This is page title"
    context = {
        'num_genres': num_genres,
        "books_with_a": books_with_a,
        'title' : title,
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }
    return render(request,'index.html', context=context)
    


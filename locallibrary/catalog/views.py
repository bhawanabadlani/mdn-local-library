from django.shortcuts import render
from catalog.models import Author, Book, BookInstance, Genre
from django.views import generic
# Create your views here.

class BookListView(generic.ListView):
    model = Book
    paginate_by = 10

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10

class AuthorDetailView(generic.DetailView):
    model = Author

def index(request):
    """View function for the homepage site"""

    # Generate count for some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available book status(status = a)
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The all() is implied by default.
    num_authors = Author.objects.count()
    
    # Genres and Books that contain a particular word(case insensitive)
    num_books_title_like = Book.objects.filter(title__icontains="self").count()
    num_genres_like = Genre.objects.filter(name__icontains="fanta").count()

    context = {
        'num_books': num_books, 
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_books_title_like': num_books_title_like,
        'num_genres_like': num_genres_like,
    }

    # Render the HTML template with the data in the context variable
    return render(request, 'catalog/index.html', context=context)
from django.shortcuts import get_object_or_404,  render
from .models import Book
from django.http import Http404



def index(request):
    books = Book.objects.all()
    return render(request, "book_outlet/index.html", {
        "books": books
    })
    
def book_detail(request, slug):
    try:
        book =get_object_or_404(Book, slug=slug)
    except:
        raise Http404()
    return render(request, "book_outlet/book_detail.html", {
              "title" :book.title,
              "author" : book.author,
              "rating" : book.rating,
              "is_bestseller" : book.is_bestseller,
          })  

          
    
    

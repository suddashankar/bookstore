from django.http import HttpResponse
from django.shortcuts import render
from bookapp.models import Book
from django.db.models import Q
from django.core.paginator import Paginator, Page, PageNotAnInteger, EmptyPage


def home(request):
    books = Book.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(books, 10)
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'books': books})

def details(request):
    #books=Book.objects.get()

    return render(request,'listing.html')

def search(request):
    print("inside search")
    if request.method == 'POST':
        author = request.POST['author']
        category = request.POST['category']
        print("author:", author, "category:", category)
        if category:
            print("inside if category:", category)
            book = Book.objects.filter(Q(category__name=category))
            return render(request, 'search.html', {'books': book, 'author': author})
        elif author:
            print("inside if author:", author)
            book = Book.objects.filter(Q(author=author))
            return render(request, 'search.html', {'books': book, 'author': author})
    else:
        pass
    return render(request, 'search.html')

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    name = request.GET.get("name") or "world!"
    return render(request, "bookmodule/index.html", {"name" : name})

def index2(request, val1 = 0):
    return HttpResponse("value1 = " + str(val1))

def viewbook(request, bookId):
    # assume that we have the following books somewhere (e.g. database)
    book1 = {'id': 123, 'title': 'Continuous Delivery', 'author': 'J. Humble and D. Farley'}
    book2 = {'id': 456, 'title': 'Secrets of Reverse Engineering', 'author': 'E. Eilam'}

    targetBook = None

    if book1['id'] == bookId:
        targetBook = book1

    if book2['id'] == bookId:
        targetBook = book2

    context = {'book': targetBook}

    return render(request, 'bookmodule/show.html', context)
# ==========================================
# Lab 4 - HTML and CSS Pages
# ==========================================

# Display the home page
def lab4_index(request):
    return render(request, 'bookmodule/lab4_index.html')


# Display the list of books
def lab4_list_books(request):
    return render(request, 'bookmodule/list_books.html')


# Display one book details
def lab4_viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')


# Display the About Us page
def lab4_aboutus(request):
    return render(request, 'bookmodule/aboutus.html')
# Lab 5 - Task 1: HTML Links
def lab5_links(request):
    return render(request, 'bookmodule/lab5_links.html')
# Lab 5 - Task 2: Text Formatting
def lab5_formatting(request):
    return render(request, 'bookmodule/lab5_formatting.html')
# Lab 5 - Task 3: Nested Lists
def lab5_listing(request):
    return render(request, 'bookmodule/lab5_listing.html')
# Lab 5 - Task 4: HTML Tables
def lab5_tables(request):
    return render(request, 'bookmodule/lab5_tables.html')
# Lab 6 - Handle Search Form
def search_books(request):
    if request.method == "POST":
        string = request.POST.get('keyword', '').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')

        books = __getBooksList()
        newBooks = []

        for item in books:
            contained = False

            if isTitle and string in item['title'].lower():
                contained = True

            if not contained and isAuthor and string in item['author'].lower():
                contained = True

            if contained:
                newBooks.append(item)

        return render(request, 'bookmodule/bookList.html', {'books': newBooks})

    return render(request, 'bookmodule/search.html')
# Lab 6 - Task 2: Books List
def __getBooksList():
    book1 = {'id': 12344321, 'title': 'Continuous Delivery', 'author': 'J.Humble and D. Farley'}
    book2 = {'id': 56788765, 'title': 'Reversing: Secrets of Reverse Engineering', 'author': 'E. Eilam'}
    book3 = {'id': 43211234, 'title': 'The Hundred-Page Machine Learning Book', 'author': 'Andriy Burkov'}
    return [book1, book2, book3]

import django
from django.conf import settings

settings.configure(
    DEBUG=True,
    SECRET_KEY='library123',
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=['*'],
    MIDDLEWARE=[],
    INSTALLED_APPS=['django.contrib.contenttypes']
)

django.setup()

from django.http import HttpResponse
from django.urls import path

books = []

def home(request):
    html = """
    <h1>Library Management</h1>
    <form method="post" action="/add/">
        Book Name: <input name="name"><br><br>
        Author: <input name="author"><br><br>
        Price: <input name="price"><br><br>
        <button>Add Book</button>
    </form>
    <h2>Book List</h2>
    """
    for i, b in enumerate(books):
        html += f"""
        <p>{b['name']} - {b['author']} -
        Rs.{b['price']}
        <a href="/delete/{i}/">Delete</a>
        <a href="/detail/{i}/">View</a></p>
        """
    return HttpResponse(html)

def add(request):
    if request.method == "POST":
        books.append({
            "name": request.POST.get("name"),
            "author": request.POST.get("author"),
            "price": request.POST.get("price")
        })
    return home(request)

def detail(request, id):
    b = books[id]
    return HttpResponse(
        f"<h1>{b['name']}</h1>"
        f"<p>Author: {b['author']}</p>"
        f"<p>Price: Rs.{b['price']}</p>"
        '<a href="/">Back</a>'
    )

def delete(request, id):
    books.pop(id)
    return home(request)

urlpatterns = [
    path('', home),
    path('add/', add),
    path('detail/<int:id>/', detail),
    path('delete/<int:id>/', delete),
]

from django.core.management import execute_from_command_line

if __name__ == "__main__":
    execute_from_command_line([
        "program11.py", "runserver", "127.0.0.1:8000"
    ])
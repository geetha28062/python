from django.conf import settings

settings.configure(
    DEBUG=True, SECRET_KEY="123",
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=["*"], MIDDLEWARE=[]
)

import django
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
    </form><hr>
    """

    for i, b in enumerate(books):
        html += f"""
        <p>{b['name']} - {b['author']} - Rs.{b['price']}
        <a href="/edit/{i}/">Edit</a>
        <a href="/delete/{i}/">Delete</a></p>
        """

    return HttpResponse(html)

def add(request):
    if request.method == "POST":
        books.append({
            "name": request.POST["name"],
            "author": request.POST["author"],
            "price": request.POST["price"]
        })
    return home(request)

def edit(request, id):
    b = books[id]

    if request.method == "POST":
        b["name"] = request.POST["name"]
        b["author"] = request.POST["author"]
        b["price"] = request.POST["price"]
        return home(request)

    return HttpResponse(f"""
    <form method="post">
    Book Name: <input name="name" value="{b['name']}"><br><br>
    Author: <input name="author" value="{b['author']}"><br><br>
    Price: <input name="price" value="{b['price']}"><br><br>
    <button>Update</button>
    </form>
    """)

def delete(request, id):
    books.pop(id)
    return home(request)

urlpatterns = [
    path("", home),
    path("add/", add),
    path("edit/<int:id>/", edit),
    path("delete/<int:id>/", delete)
]

from django.core.management import execute_from_command_line
execute_from_command_line([
    "program3.py", "runserver", "0.0.0.0:8003"
])
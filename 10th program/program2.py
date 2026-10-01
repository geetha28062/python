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

students = []

def home(request):
    html = """
    <h1>Student Management</h1>
    <form method="post" action="/add/">
    Name: <input name="name"><br><br>
    Age: <input name="age"><br><br>
    Course: <input name="course"><br><br>
    <button>Add Student</button>
    </form><hr>
    """

    for i, s in enumerate(students):
        html += f"""
        <p>{s['name']} - {s['age']} - {s['course']}
        <a href="/edit/{i}/">Edit</a>
        <a href="/delete/{i}/">Delete</a></p>
        """

    return HttpResponse(html)

def add(request):
    if request.method == "POST":
        students.append({
            "name": request.POST["name"],
            "age": request.POST["age"],
            "course": request.POST["course"]
        })
    return home(request)

def edit(request, id):
    s = students[id]

    if request.method == "POST":
        s["name"] = request.POST["name"]
        s["age"] = request.POST["age"]
        s["course"] = request.POST["course"]
        return home(request)

    return HttpResponse(f"""
    <form method="post">
    Name: <input name="name" value="{s['name']}"><br><br>
    Age: <input name="age" value="{s['age']}"><br><br>
    Course: <input name="course" value="{s['course']}"><br><br>
    <button>Update</button>
    </form>
    """)

def delete(request, id):
    students.pop(id)
    return home(request)

urlpatterns = [
    path("", home),
    path("add/", add),
    path("edit/<int:id>/", edit),
    path("delete/<int:id>/", delete)
]

from django.core.management import execute_from_command_line
execute_from_command_line([
    "program1.py", "runserver", "0.0.0.0:8001"
])
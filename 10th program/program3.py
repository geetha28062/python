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

employees = []

def home(request):
    html = """
    <h1>Employee Management</h1>
    <form method="post" action="/add/">
    Name: <input name="name"><br><br>
    Salary: <input name="salary"><br><br>
    Department: <input name="dept"><br><br>
    <button>Add Employee</button>
    </form><hr>
    """

    for i, e in enumerate(employees):
        html += f"""
        <p>{e['name']} - {e['salary']} - {e['dept']}
        <a href="/edit/{i}/">Edit</a>
        <a href="/delete/{i}/">Delete</a></p>
        """

    return HttpResponse(html)

def add(request):
    if request.method == "POST":
        employees.append({
            "name": request.POST["name"],
            "salary": request.POST["salary"],
            "dept": request.POST["dept"]
        })
    return home(request)

def edit(request, id):
    e = employees[id]

    if request.method == "POST":
        e["name"] = request.POST["name"]
        e["salary"] = request.POST["salary"]
        e["dept"] = request.POST["dept"]
        return home(request)

    return HttpResponse(f"""
    <form method="post">
    Name: <input name="name" value="{e['name']}"><br><br>
    Salary: <input name="salary" value="{e['salary']}"><br><br>
    Department: <input name="dept" value="{e['dept']}"><br><br>
    <button>Update</button>
    </form>
    """)

def delete(request, id):
    employees.pop(id)
    return home(request)

urlpatterns = [
    path("", home),
    path("add/", add),
    path("edit/<int:id>/", edit),
    path("delete/<int:id>/", delete)
]

from django.core.management import execute_from_command_line
execute_from_command_line([
    "program2.py", "runserver", "0.0.0.0:8002"
])
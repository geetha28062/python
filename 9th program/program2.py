import django
from django.conf import settings

settings.configure(
    DEBUG=True,
    SECRET_KEY='employee123',
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=['*'],
    MIDDLEWARE=[],
    INSTALLED_APPS=['django.contrib.contenttypes']
)

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
    </form>
    <h2>Employee List</h2>
    """
    for i, e in enumerate(employees):
        html += f"""
        <p>{e['name']} - {e['salary']} -
        {e['dept']}
        <a href="/delete/{i}/">Delete</a>
        <a href="/detail/{i}/">View</a></p>
        """
    return HttpResponse(html)

def add(request):
    if request.method == "POST":
        employees.append({
            "name": request.POST.get("name"),
            "salary": request.POST.get("salary"),
            "dept": request.POST.get("dept")
        })
    return home(request)

def detail(request, id):
    e = employees[id]
    return HttpResponse(
        f"<h1>{e['name']}</h1>"
        f"<p>Salary: {e['salary']}</p>"
        f"<p>Department: {e['dept']}</p>"
        '<a href="/">Back</a>'
    )

def delete(request, id):
    employees.pop(id)
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
        "program10.py", "runserver", "127.0.0.1:8000"
    ])
import django
from django.conf import settings

settings.configure(
    DEBUG=True,
    SECRET_KEY='product123',
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=['*'],
    MIDDLEWARE=[],
    INSTALLED_APPS=['django.contrib.contenttypes']
)

django.setup()

from django.http import HttpResponse
from django.urls import path

products = []

def home(request):
    html = """
    <h1>Product Management</h1>
    <form method="post" action="/add/">
        Product: <input name="name"><br><br>
        Price: <input name="price"><br><br>
        Quantity: <input name="qty"><br><br>
        <button>Add Product</button>
    </form>
    <h2>Product List</h2>
    """
    for i, p in enumerate(products):
        html += f"""
        <p>{p['name']} - Rs.{p['price']} -
        Qty: {p['qty']}
        <a href="/delete/{i}/">Delete</a>
        <a href="/detail/{i}/">View</a></p>
        """
    return HttpResponse(html)

def add(request):
    if request.method == "POST":
        products.append({
            "name": request.POST.get("name"),
            "price": request.POST.get("price"),
            "qty": request.POST.get("qty")
        })
    return home(request)

def detail(request, id):
    p = products[id]
    return HttpResponse(
        f"<h1>{p['name']}</h1>"
        f"<p>Price: Rs.{p['price']}</p>"
        f"<p>Quantity: {p['qty']}</p>"
        '<a href="/">Back</a>'
    )

def delete(request, id):
    products.pop(id)
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
        "program12.py", "runserver", "127.0.0.1:8000"
    ])
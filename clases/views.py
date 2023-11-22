from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")

def ClasesListView(request):
    return render(request, "lista-clases.html")

def ClasesCreateView(request):
    return render(request, "crear-clase.html")

def ClasesEditView(request):
    return render(request, "editar-clase.html")

def ClasesDeleteView(request):
    return render(request, "eliminar-clase.html")

def login(request):
    return render(request, "login.html")
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def MenuItemView(request):
    pass

def SingleItemMenuView(request):
    pass
from django.shortcuts import render

# Usually a model is used instead
dogs = [
  {'name': 'biggie', 'breed': 'golden retriever', 'description': 'good family dog', 'age': 2},
  {'name': 'sophie', 'breed': 'poodle', 'description': 'gentle and loving', 'age': 1},
]


# Create your views here.
def home(request):
    # Include an .html file extension  
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    return render(request, 'dogs/index.html', {
        'dogs': dogs
    })
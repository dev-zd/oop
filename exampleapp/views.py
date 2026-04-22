from django.shortcuts import render

# Create your views here.

# views.py = business logic

def add_department(request):
    if request.method == 'POST':
        name = request.POST['name']
        department = Department(name=name)
        department.save()
        return redirect('index')
    return render(request, 'add_department.html')


def index(request):
    return render(request, 'index.html')


print("Hello, World!")

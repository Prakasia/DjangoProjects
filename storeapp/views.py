from django.shortcuts import render

# Create your views here.
def home(request):
    data = {
        'msg' : 'Welcome to COZY BOOKSTORE.'
    }
    return render(request, 'storeapp/home.html', context=data)

def about(request):
    return render(request, 'storeapp/about.html')

def bookinfo(request):
    my_dict = {
        'The Great Gatsby' : 'F. Scott Fitzgerald Jesmyn Ward',
        'To Kill a Mockingbird' : 'Harper Lee',
        'Pride and Prejudice' : 'Jane Austen',
        '1984' : 'George Orwell'
    }
    return render(request, 'storeapp/bookinfo.html', {'books':my_dict})
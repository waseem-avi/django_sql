from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World!</h1>")
    return render(request, "home.html", {})

def context_view(request , *args, **kwargs):
    my_context = {
        "my_text"   : "This is context text which will be rendered",
        "my_number" : 54
    }
    return render(request, "context.html" , my_context)
def forloop_view(request, *args , **kwargs):
    my_context = {
        "my_list":['list item', 2 , 3, 4, 'another string']
        
    }
    return render(request, "forloop.html", my_context)

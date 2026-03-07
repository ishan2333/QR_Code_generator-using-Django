from django.shortcuts import render

# Create your views here.
def home(req):
    li = {"name" : "Ishan"}
    return render(req , "index.html" ,li)
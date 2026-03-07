from django.shortcuts import render
import qrcode
# Create your views here.
def home(req):
    data = 
    img = qrcode.make(data)
    li = {"name" : "Ishan"}
    return render(req , "index.html" ,li)
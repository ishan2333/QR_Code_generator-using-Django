from django.shortcuts import render ,HttpResponse
import qrcode
# Create your views here.
def process_form_view(request):
    if request.method == 'POST':
        user_input_data = request.POST.get('user_input')
        print(user_input_data)
        qrimg = qrcode.make(user_input_data)
        
    return render(request , "index.html")
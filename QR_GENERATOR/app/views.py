from django.shortcuts import render ,HttpResponse
import qrcode
from io import BytesIO
import base64

# Create your views here.
def process_form_view(request):
    qr_code = None
    if request.method == 'POST':
        data = request.POST.get('user_input')
        print(data)
        qr = qrcode.make(data)
        buffer = BytesIO()
        qr.save(buffer, format="PNG")
        qr_code = base64.b64encode(buffer.getvalue()).decode()

    return render(request, "index.html",{"qr_code" : qr_code})
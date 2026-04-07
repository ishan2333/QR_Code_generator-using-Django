from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.process_form_view),
    # path('process/', views.process_form_view, name='process_form_view')
]

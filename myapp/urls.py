from django.urls import path
from . import views

urlpatterns = [
    # Add the URL pattern for the QR code generator view
    path('', views.generate_qr_code, name='generate_qr_code'),
    # Add the URL pattern for the QR code scanner view
    path('qr-scanner/', views.qr_code_scanner, name='qr_code_scanner'),
    
    path('verified/', views.qr_code_verified.as_view(), name='qr_code_verified'),
    # path("change/", views.Change.as_view(), name="change"),

]

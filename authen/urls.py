from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static 
urlpatterns=[
    path('',login_,name='login_'),
    path('register/',register,name='register'),
    path('profile/',profile,name='profile'),
    path('logout/',logout_ ,name='logout_'),
    path('updatedetails/<int:pk>/', updatedetails, name='updatedetails'),
    path('change-password/', change_password, name='change_password'),
    path('forgot-password/', forgot_password, name='forgot_password'),

]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 
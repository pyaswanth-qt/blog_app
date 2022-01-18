from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
path('',views.home,name='home'),
path('upload/',views.upload,name='upload'),
path('login/',views.login,name='login'),
path('register/',views.register,name='register'),
path('blog/<slug:url>',views.post,name='post')
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
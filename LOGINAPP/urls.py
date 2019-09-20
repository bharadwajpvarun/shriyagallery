from django.urls import path
from LOGINAPP import views as signup_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns= [path("",signup_view.populate, name='gallery'),
              path('superuser/valli/upload/images', signup_view.upload, name='upload'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
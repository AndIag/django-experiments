from django.conf.urls import url
from django.contrib import admin

from imageApp.views import UploadImagesView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^images/', UploadImagesView, name='images')
]

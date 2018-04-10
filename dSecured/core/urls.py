from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "AI Administration"
admin.site.site_title = "AI Administration"

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('secret/', admin.site.urls),
]

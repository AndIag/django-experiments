from django.contrib import admin
from django.urls import path, include
from oauth2_provider.views import AuthorizationView, TokenView, RevokeTokenView, IntrospectTokenView

admin.site.site_header = "AI Administration"
admin.site.site_title = "AI Administration"

auth_urls = [
    path("authorize/", AuthorizationView.as_view(), name="authorize"),
    path("token/", TokenView.as_view(), name="token"),
    path("revoke_token/", RevokeTokenView.as_view(), name="revoke-token"),
    path("introspect/", IntrospectTokenView.as_view(), name="introspect"),
]

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('secret/', admin.site.urls),
    path('o/', include(auth_urls, namespace='oauth2_provider')),
]

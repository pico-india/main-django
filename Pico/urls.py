from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static


admin.site.site_header = "Pico Admin"
admin.site.site_title = "Pico Portal"
admin.site.index_title = "Welcome to Pico"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Image.urls')),
    path('accounts/', include('Accounts.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

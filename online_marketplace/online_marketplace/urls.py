from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('core.urls')), # to connect with urls.py in core app
    path('items/', include('item.urls')), # to connect with urls.py in item app
    path('dashboard/', include('dashboard.urls')), # to connect with urls.py in dashboard app
    path('inbox/', include('conversation.urls')), # to connect with urls.py in conversation app
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

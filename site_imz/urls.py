from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("prose/", include("prose.urls")),
    # apps
    path('', include('main.urls')),
    path('news/', include('blog.urls')),
    path('units/', include('units.urls')),
    path('announcements/', include('announcements.urls')),
    path('articles/', include('articles.urls')),
]

if settings.DEBUG:
    urlpatterns += [path("__debug__/", include("debug_toolbar.urls"))]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = 'Институт мерзлотоведения'
admin.site.site_title = 'Институт мерзлотоведения'

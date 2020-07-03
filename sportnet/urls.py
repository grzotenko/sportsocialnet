from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url, re_path
from django.conf.urls.static import static  #media+static
from django.conf import settings            #media+static
urlpatterns = [
    url(r'^admin_tools/', include('admin_tools.urls')),
    path('admin/', admin.site.urls),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
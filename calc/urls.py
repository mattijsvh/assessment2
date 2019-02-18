from django.conf.urls import url
from django.views.generic import TemplateView
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from calc.calculations import views as calc_views
from calc.stats import views as stats_views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^calculations/$', calc_views.overview, name='overview'),
    url(r'^stats/$', stats_views.file_upload, name='file_upload')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)

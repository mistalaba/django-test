from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.views import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^webhooks/', include('trello_webhooks.urls')),
]

urlpatterns += staticfiles_urlpatterns()

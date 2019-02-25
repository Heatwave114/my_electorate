from django.conf.urls import url
from presidential.views import index


app_name = 'presidential'
urlpatterns = [
    url(r'^$', index, name='index')
]

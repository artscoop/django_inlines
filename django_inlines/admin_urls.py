try:
    from django.conf.urls.defaults import *
except:
    from django.conf.urls import *

from django_inlines.views import js_inline_config, get_inline_form


urlpatterns = [
    url(r'^inline_config\.js$', js_inline_config, name='js_inline_config'),
    url(r'^get_inline_form/$', get_inline_form, name='get_inline_form'),
]

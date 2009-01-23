from django.conf.urls.defaults import *

from loginreg.views import start_page, logout_page 

urlpatterns = patterns('',
                       (r'^$', start_page),
                       (r'logout/$', logout_page),
                       (r'^login/$', 'django.contrib.auth.views.login'),
                       )

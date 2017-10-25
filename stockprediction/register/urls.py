from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.conf.urls import url, include, patterns
import django.contrib.auth.urls
import User.views
from stockapp import views
urlpatterns = patterns('',
    url(r'home','User.views.register',name='User_home'),
    url('register/', CreateView.as_view(
            template_name='register.html',
            form_class=UserCreationForm,
            success_url='/'
    )),
    url('^accounts/', include('django.contrib.auth.urls')),

    # rest of your URLs as normal
)
#url('register/','stockapp.views.register',name='register'),
#url(r'^$', 'stockapp.views.index', name='index'),

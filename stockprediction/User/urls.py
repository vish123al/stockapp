from django.conf.urls import patterns, include
from django.conf.urls import url,patterns,include
import User.views

urlpatterns= [
	
	url(r'home',User.views.home_User,name='User_home'),

		]

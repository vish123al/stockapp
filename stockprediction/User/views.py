from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
#from django.shortcuts import render
#from django.http import HttpResponse
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

# Create your views here.
def home_User(request):
	return render(request, 'User/index.html')

from django.shortcuts import render
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

# Create your views here.
def register(request):
	if request.method == 'POST':
		form = MyRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('../register_success.html')
		else:
			return HttpResponseRedirect('../invalid_register.html')
	args = {}
	args.update(csrf(request))
	
	args['form'] = MyRegistrationForm()
	return render_to_response('register.html', args)
	
def register_success(request):
	return render_to_response('register_success.html')
	
def invalid_register(request):
	return render_to_response('invalid_register.html')

from django.shortcuts import render

def index(request):
	template_name = 'index.html'
	context={}
	context['title'] = 'Test Project'
	return render(request, template_name, context)
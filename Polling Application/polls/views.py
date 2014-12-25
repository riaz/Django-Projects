from django.http import HttpResponse
from django.template import RequestContext,loader
from django.shortcuts import render

from polls.models import Question

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5] 
	
	context = { 'latest_question_list': latest_question_list}

	return render(request,'polls/index.html',context)

	""""
	# Templating without using shortcuts

	template = loader.get_template('polls/index.html')
	context = RequestContext(request,{
		'latest_question_list': latest_question_list,
	})

	return HttpResponse(template.render(context))	
	"""
	#output = ', '.join([p.question_text for p in latest_question_list])
	#return HttpResponse(output)
	
        #return HttpResponse("Hello World! You are at the poll index.")
	
	
def detail(request,question_id):
	return HttpResponse("You are looking at question: %s" % question_id)

def results(request,question_id):
	result = "You're looking at results of question: %s"
	return HttpResponse( result % question_id)

def vote(request,question_id):
	return HttpResponse("You are voting for question %s " % question_id)



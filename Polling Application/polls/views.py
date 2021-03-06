from django.http import HttpResponse,Http404, HttpResponseRedirect
from django.template import RequestContext,loader
from django.shortcuts import render,get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic

from polls.models import Question,Choice

"""
class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		returns the last 5 published questions
		return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'

"""
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
	#Handling 404 with shortcuts
	question = get_object_or_404(Question,pk=question_id)
	return render(request,'polls/detail.html',{ 'question': question })
		
	
	# Handling 404 the generic way
	"""	
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404
	return render(request,'polls/detail.html',{ 'question': question })

	"""

	#return HttpResponse("You are looking at question: %s" % question_id)
	

def results(request,question_id):
	question = get_object_or_404(Question,pk=question_id)
	return render(request,'polls/results.html',{'question': question })
	
	#result = "You're looking at results of question: %s"
	#return HttpResponse( result % question_id)

def vote(request,question_id):
	p = get_object_or_404(Question,pk=question_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		#Redisplay the question voting form
		return render(request,"polls/detail.html",{
			'question': p,
			'error_message': "You didn't select a valid choice"
		})

	selected_choice.votes += 1
	selected_choice.save()

	#Always  run a HttpResponseRedirect after successfully dealing with POST data.
	#This prevents the data from being posted twice , if the user hits the back button.

	return HttpResponseRedirect(reverse('polls:results',args=(p.id,)))
		
	#return HttpResponse("You are voting for question %s " % question_id)




from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic

from .models import Choice, Question

class IndexView(generic.ListView):
    template_name = 'Polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'Polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'Polls/results.html'


def vote(request, question_id):
    ... # same as above, no changes needed.

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'Polls/results.html', {'question': question})

# ...
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'Polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('Polls:results', args=(question.id,)))

from .models import Question

# . . .
def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'Polls/detail.html', {'question': question})
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")
	return render(request, 'Polls/detail.html', {'question': question})

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	template = loader.get_template('Polls/index.html')
	context = {'latest_question_list': latest_question_list,}
	return render(request, 'Polls/index.html', context)

	return HttpResponse(template.render(context, request))

	output = ', '.join([q.question_text for q in latest_question_list])
	return HttpResponse(output)
	return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
	return HttpResponse("You're looking at question %s." % question_id) 

def results(request, question_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % question_id)

def vote(request, question_id):
		return HttpResponse("You're voting on question %s." % question_id)   
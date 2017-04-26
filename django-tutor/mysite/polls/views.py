from django.shortcuts import render
from django.shortcuts import get_object_or_404

# Create your views here.

from django.http import HttpResponse
from django.http import HttpResponseRedirect
# from django.http import Http404
from django.template import loader

from django.urls import reverse

from .models import Question
from .models import Choice

def index(request): # display the lastest few question
    lastest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html') # direct load from polls/templates/
    context = {
        'latest_question_list': lastest_question_list,
    } # context transfer to polls/index.html then show the index page in polls/
    # output = ', '.join([q.question_text for q in lastest_question_list])
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)

def detail(request, question_id): # displays a question text, without results but with a form to vote
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Sorry, Question does not exist!")
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'polls/detail.html', context)
    
def results(request, question_id): # displays results for a particular question
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id): # handles voting for a particular choice in a particular question
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
                'question': question, 
                'error_message': "You didn't select a choice.", 
                    })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a 
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
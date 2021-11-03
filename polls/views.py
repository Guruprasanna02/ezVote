from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Question, Choice
import json

# Show specific question and choices


def detail(request, question_id):
    with open('status.json', 'r') as openfile:
        status = json.load(openfile)
    try:
        if status[f"{request.user}"] == 0:
            st = True
            try:
                question = Question.objects.get(pk=question_id)
            except Question.DoesNotExist:
                raise Http404("Question does not exist")
            return render(request, 'polls/detail.html', {'question': question,'st':st})
        else :
            st = False
            try:
                question = Question.objects.get(pk=question_id)
            except Question.DoesNotExist:
                raise Http404("Question does not exist")
            return render(request, 'polls/detail.html', {'question': question, 'st':st})
    except:
        st = True
        try:
            question = Question.objects.get(pk=question_id)
        except Question.DoesNotExist:
            raise Http404("Question does not exist")
        return render(request, 'polls/detail.html', {'question': question,'st':st})
        
# Get question and display results


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

# Vote for a question choice

def vote(request, question_id):
    # print(request.POST['choice'])
    question = get_object_or_404(Question, pk=question_id)
    try:
        global selected_choice
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        current_user = request.user
        selected_choice.votes += 1
        selected_choice.save()
        status = {f"{current_user}": selected_choice.votes}
        with open('status.json', 'r+') as openfile:
            status = json.load(openfile)
            status[f"{current_user}"] = selected_choice.votes
            openfile.seek(0)  # rewind
            json.dump(status, openfile)
            openfile.truncate()

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

# Get questions and display them

def index(request):
    latest_question_list = Question.objects.order_by('-when')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

from django.shortcuts import render
from .models import Question, Choice
# Create your views here.
#get questions and display items
#the below url is being requested
def index(request):
    latest_question_list = Question.objects.all()
    print(len(latest_question_list),"this is the lenght")
    context = {"latest_question_list":latest_question_list}
    return render(request,'polls/index.html',context)

#show specific question and choices

def detail(request,question_id):
    try:
        question = Question.objects.get(pk = question_id)
    except Question.DoesNotExist :
        #raise an http error
        raise Http404("question does not exist")
    return render(request,'polls/detail.html',{"question":question})

#get questions and display results 

def results(request,question_id):
    question = get_object_or_404(Question,pk = question_id)
    return render(request,'polls/results.html',{'question':question})

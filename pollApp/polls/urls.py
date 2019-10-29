from django.urls import path
from . import views 
#here we are giving this a namepace
#because we can also have other apps
app_name = 'polls'
urlpatterns = [
    path('',views.index,name = "index"),
    #the angle brackets are for the parameter
    #'' means just /polls if we did path("results",..)
    #that would mean/polls/results
    #also this would look in ./templates/index.html
    #but we are using global templates after changing the settings
    path('<int:question_id>',views.detail,name = "detail"),       
    #the above is only the question            
    path('<int:question_id>/results',views.results,name = "results")
    #the above is the details of the question
]
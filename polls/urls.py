
from django.urls import path
from polls.views import index, hello, detail,vote,response
urlpatterns = [

    path("", index.index, name="index"),
    path("hello/", hello.hello, name="hello"),
    path('details/<int:question_id>/', detail.detail, name='detail'),
    path('<int:question_id>/results/', response.results, name='results'),
    path('vote/<int:question_id>/vote/', vote.vote, name='vote'),
]
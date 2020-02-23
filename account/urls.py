from django.urls import path

from account.views import EmailCodeView, SessionView, UserView

urlpatterns = [

    path('email_code', EmailCodeView.as_view()),
    path('session', SessionView.as_view()),
    path('user', UserView.as_view()),

]

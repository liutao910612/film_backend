from django.urls import path

from account.views import EmailCodeView

urlpatterns = [

    path('email_code', EmailCodeView.as_view()),

]

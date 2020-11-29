from django.urls import path

from chatbot_unicatolica.chatbot.views import (
    Teste
)

app_name = "chatbot"
urlpatterns = [
    path("milho/asdasdasd/<slug>", view=Teste.as_view(), name="milho-teste"),
]

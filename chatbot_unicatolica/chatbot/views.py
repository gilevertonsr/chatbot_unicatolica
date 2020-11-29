from django.shortcuts import render
from django.views import generic, View


class Teste(generic.TemplateView):
    template_name = "chatbot/teste.html"


class OlaMundo(View):

    def post(self, request):
        return render("chatbot/teste.html", context={"mensagem": "Ola mundo"})

    def get(self, request):
        return render("chatbot/teste.html", context={"mensagem": "Adeus mundo"})

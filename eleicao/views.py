from django.shortcuts import render
from django.http import HttpResponse
from eleicao.models import *
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from eleicao.serializers import *

# Create your views here.
class CandidatoViewSet(viewsets.ModelViewSet):
    queryset = Candidato.objects.all()
    serializer_class = CandidatoSerializer

class VotoViewSet(viewsets.ModelViewSet):
    queryset = Voto.objects.all()
    serializer_class = VotoSerializer

class VotoBrancoViewSet(viewsets.ModelViewSet):
    queryset = VotoBranco.objects.all()
    serializer_class = VotoBrancoSerializer

class EleicaoViewSet(viewsets.ModelViewSet):
    queryset = Eleicao.objects.all()
    serializer_class = EleicaoSerializer

class EleitorViewSet(viewsets.ModelViewSet):
    queryset = Eleitor.objects.all()
    serializer_class = EleitorSerializer

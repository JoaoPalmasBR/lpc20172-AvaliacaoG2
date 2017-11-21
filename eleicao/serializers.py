from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from eleicao.models import *

class CandidatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidato
        fields = ('pk','url','nome','votos',)
    def create(self, validated_data):
        Candidato_data = Candidato.objects.create(**validated_data)
        return Candidato_data

class VotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voto
        fields = ('pk','url','candidato',)
    def create(self, validated_data):
        Voto_data = Voto.objects.create(**validated_data)
        return Voto_data

class VotoBrancoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VotoBranco
        fields = ('pk','url','branco',)
    def create(self, validated_data):
        VotoBranco_data = VotoBranco.objects.create(**validated_data)
        return VotoBranco_data

class EleicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eleicao
        fields = ('pk','url','nome','data','vencedor','candidatos',)
    def create(self, validated_data):
        Eleicao_data = Eleicao.objects.create(**validated_data)
        return Eleicao_data

class EleitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eleitor
        fields = ('pk','url','nome','token','votou',)
    def create(self, validated_data):
        Eleitor_data = Eleitor.objects.create(**validated_data)
        return Eleitor_data
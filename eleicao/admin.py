from django.contrib import admin
from eleicao.models import *
# Register your models here.

admin.site.register(Candidato)
admin.site.register(Voto)
admin.site.register(VotoBranco)
admin.site.register(Eleicao)
admin.site.register(Eleitor)
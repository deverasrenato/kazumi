from django.contrib import admin
from .models import Empresa, Candidato, ProgramaEmpresa, Programa, ProgramaCandidato, ProgramaFinal


# class ProgramasAdmin(admin.ModelAdmin):
#     list_display = ('nomePrograma', 'nomeEmpresa')
#     search_fields = ('nomePrograma',)
#     list_per_page = int = 2
#     model = Empresa


admin.site.register(Empresa)
admin.site.register(Candidato)
admin.site.register(ProgramaEmpresa)
admin.site.register(Programa)
admin.site.register(ProgramaCandidato)
admin.site.register(ProgramaFinal)


# Register your models here.

from django.db import models


# Create your models here.
class Empresa(models.Model):
    nomeEmpresa = models.CharField(max_length=50)

    # setorEmpresa = models.CharField(max_length=50)
    # codigoSetorEmpresa = models.CharField(max_length=10)

    def __str__(self):
        return self.nomeEmpresa


class Candidato(models.Model):
    nomeCandidato = models.CharField(max_length=50)
    idadeCandidato = models.FloatField()

    def __str__(self):
        return self.nomeCandidato


class Programa(models.Model):
    nomePrograma = models.CharField(max_length=50, default='some_value')

    def __str__(self):
        return self.nomePrograma


class ProgramaEmpresa(models.Model):
    # nomePrograma = models.CharField(max_length=50)
    listaProgramaEmpresa = models.CharField(max_length=50, null=True)
    empresaProgramaEmpresa = models.ManyToManyField(Empresa)

    # nomeProgramaPrograma = models.OneToOneField(NomePrograma)

    def __str__(self):
        return [empresa_atual.nomePrograma for empresa_atual in self.empresaProgramaEmpresa.all()].__str__()


class ProgramaCandidato(models.Model):
    listaProgramaCandidato = models.CharField(max_length=50, null=True)
    candidatoProgramaCandidato = models.ManyToManyField(Candidato)

    def __str__(self):
        return [candidato_atual.nomePrograma for candidato_atual in self.candidatoProgramaCandidato.all()].__str__()


class ProgramaFinal(models.Model):
    dataInicio = models.DateTimeField()
    programa = models.ForeignKey(Programa, on_delete=models.PROTECT, related_name='programa')
    empresas = models.ForeignKey(ProgramaEmpresa, on_delete=models.PROTECT, related_name='empresas')
    candidatos = models.ForeignKey(ProgramaCandidato, on_delete=models.PROTECT, related_name='candidatos')

    def __str__(self):
        return f'Programa: {self.programa} | Empresa(s): {self.empresas} | Candidato(s): {self.candidatos}'

# class VerPrograma(models.Model):
#     data= models.DateTimeField9()

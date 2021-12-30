from django.db import models

class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True) #data de criação
    atualizacao = models.DateTimeField(auto_now=True) #data de atualização
    ativo = models.BooleanField(default=True) #se está ativo ou não

    class Meta:
        abstract = True

class Curso(Base):
    titulo = models.CharField(max_length=255)
    url = models.URLField(unique=True)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['id'] #ordenar na paginação

    def __str__(self):
        return self.titulo

class Avaliacao(Base):
    curso = models.ForeignKey(Curso, related_name='avaliacoes', on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    comentario = models.TextField(blank=True, default='')
    avaliacao = models.DecimalField(max_digits=2, decimal_places=1) #notas float

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        unique_together = ['email', 'curso'] #pessoa com o email só avalia o curso uma única vez
        ordering = ['id'] #ordenar na paginação

    def __str__(self):
        return f'{self.nome} avaliou o curso {self.curso} com nota {self.avaliacao}'
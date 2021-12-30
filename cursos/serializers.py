from rest_framework import serializers

from .models import Curso, Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': { 'write_only': True} #Não será apresentado quando as avaliações forem consultadas
        }
        model = Avaliacao
        #irá mostrar quando for acessado a API
        fields = (
            'id',
            'curso',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo'
        )


class CursoSerializer(serializers.ModelSerializer):
    #Nested Relationship
    #passa informações completas (muito pesado)
    #avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    #hyperLinked Related Field
    #recomendação para API REST
    #passa os links para acessar cada avaliação (interessante)
    #avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='avaliacao-detail')

    #Primary Key Related Field
    #passa apenas o id de cada avaliação (mais leve)
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes'
        )
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer

class CursoAPIView(APIView):
    """
    API de cursos [ESCOLA]
    """
    def get(self, request):
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CursoSerializer(data=request.data) #pegando dados que estão vindo na requisição
        serializer.is_valid(raise_exception=True) #verifica se estão válidos
        serializer.save() #salvar
        return Response(serializer.data, status=status.HTTP_201_CREATED) #resposta dos status salvo e uma resposta http
        #{"id": serializer.data['id'], "titulo": serializer.data['titulo']}

class AvaliacaoAPIView(APIView):
    """
    API de avaliações [ESCOLA]
    """
    def get(self,request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AvaliacaoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
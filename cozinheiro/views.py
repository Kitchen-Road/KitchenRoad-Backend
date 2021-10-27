from rest_framework import viewsets, generics, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import login
from knox.auth import AuthToken
from knox.views import LoginView as KnoxLoginView
from rest_framework.views import APIView
from .serializers import CozinheiroSerializer, ResgisterSerializer
from .models import Cozinheiro
from receita.serializers import ReceitaConcluidaSerializer, ReceitaSerializer
from receita.models import Receita
from django.http import JsonResponse


class CozinheiroViewSet(viewsets.ModelViewSet):
    serializer_class = CozinheiroSerializer
    queryset = Cozinheiro.objects.all()


class RegisterCozinheiroView(generics.GenericAPIView):
    serializer_class = ResgisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": CozinheiroSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class LoginCozinheiroView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginCozinheiroView, self).post(request, format=None)


class ReceitaCompletadaView(generics.UpdateAPIView, generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ReceitaConcluidaSerializer

    def get_object(self):
        return Cozinheiro.objects.get(email=self.request.user)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            receita = Receita.objects.get(
                nome_receita=serializer.data.get('nome_receita'))
            instance.receitas_completadas.add(receita)
            receita.save()
            return Response("Receita concluída!")
        except:
            return Response("Receita não encontrada!", status=status.HTTP_404_NOT_FOUND)


class ReceitaListViewSet(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ReceitaSerializer

    def get_object(self):
        return Cozinheiro.objects.get(email=self.request.user)

    def get(self, *args, **kwargs):
        instance = self.get_object()
        queryset = instance.receitas_completadas.all()
        serializer = ReceitaSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

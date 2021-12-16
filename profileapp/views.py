from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import permissions, authentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveUpdateAPIView
from profileapp.models import Profile
from profileapp.permissions import IsProfileOwner
from profileapp.serializers import ProfileSerializer

class ProfileCreateTemplateView(TemplateView):
    template_name = 'profileapp/create.html'

class ProfileCreateAPIView(CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ProfileUpdateTemplateView(TemplateView):
    template_name = 'profileapp/update.html'

class ProfileRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsProfileOwner]
    authentication_classes = [TokenAuthentication]
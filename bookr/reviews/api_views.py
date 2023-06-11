from rest_framework import generics

from .models import Book, Contributor
from .serializers import BookSerializer, ContributorSerializer

class ContributorView(generics.ListAPIView):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer

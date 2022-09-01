from rest_framework import generics
from .serializer import ThingSerializer
from .models import Tree
from .permissions import IsOwnerOrReadOnly


class TreeList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Tree.objects.all()
    serializer_class = ThingSerializer


class TreeDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Tree.objects.all()
    serializer_class = ThingSerializer

from rest_framework import generics
from .serializer import CarSerializer
from .models import Car
from .permissions import IsOwnerOrReadOnly


class CarList(generics.ListAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Car.objects.all()
    serializer_class = CarSerializer

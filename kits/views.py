from rest_framework import viewsets
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import IsAuthenticated

from .models import Kit, Medicine
from .serializers import KitSerializer, MedicineSerializer, KitCreateSerializer, MedicineCreateSerializer


class KitView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Kit.objects.all()
    serializer_class = KitSerializer

    def get_queryset(self):
        return Kit.objects.filter(user=self.request.user)


class KitCreateView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Kit.objects.none()
    serializer_class = KitCreateSerializer


class KitRemoveView(DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = KitSerializer
    lookup_field = "id"

    def get_queryset(self):
        return Kit.objects.filter(user=self.request.user, id=self.kwargs["id"])


class KitUpdateView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = KitSerializer
    lookup_field = "id"

    def get_queryset(self):
        return Kit.objects.filter(user=self.request.user, id=self.kwargs["id"])


class MedicineView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer

    def get_queryset(self):
        return Medicine.objects.filter(kit__user=self.request.user, kit_id=self.kwargs.get("kit_id"))


class MedicineCreateView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Medicine.objects.none()
    serializer_class = MedicineCreateSerializer


class MedicineRemoveView(DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = MedicineSerializer
    lookup_field = "id"
    allowed_methods = ["patch", "delete"]

    def get_queryset(self):
        return Medicine.objects.filter(kit__user=self.request.user, id=self.kwargs["id"])


class MedicineUpdateView(UpdateAPIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = MedicineSerializer
    lookup_field = "id"

    def get_queryset(self):
        return Medicine.objects.filter(kit__user=self.request.user, id=self.kwargs["id"])




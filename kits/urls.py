from django.urls import path, include
from rest_framework import routers
# from .views import KitViewSet, MedicineViewSet
from .views import KitView, KitCreateView, MedicineView, MedicineCreateView, KitRemoveView, KitUpdateView, MedicineRemoveView, MedicineUpdateView

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('kits', KitView.as_view(), name='kits'),
    path('kit', KitCreateView.as_view(), name='kit'),
    path('medicines/<int:kit_id>', MedicineView.as_view(), name='medicines'),
    path('medicine', MedicineCreateView.as_view(), name='medicine'),
    path('kit/delete/<int:id>', KitRemoveView.as_view(), name='kit_remove'),
    path('kit/update/<int:id>', KitUpdateView.as_view(), name='kit_update'),
    path('medicine/delete/<int:id>', MedicineRemoveView.as_view(), name="medicine_remove"),
    path('medicine/update/<int:id>', MedicineUpdateView.as_view(), name="medicine_update"),
]

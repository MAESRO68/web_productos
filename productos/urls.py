from django.urls import path
from . import views

urlpatterns = [
    # Productos
    path('', views.producto_listado, name="producto_listado"),
    path('producto/<int:pk>/', views.producto_detalle, name="producto_detalle"),
    path('producto/crear/', views.producto_crear, name="producto_crear"),
    path('producto/<int:pk>/editar/', views.producto_editar, name="producto_editar"),
    path('producto/<int:pk>/borrar/', views.producto_borrar, name="producto_borrar"),

    # Pedidos
    path('pedidos/', views.pedido_listado, name="pedido_listado"),
    path('pedido/<int:pk>/', views.pedido_detalle, name="pedido_detalle"),
    path('pedido/crear/', views.pedido_crear, name="pedido_crear"),
    path('pedido/<int:pk>/borrar/', views.pedido_borrar, name="pedido_borrar"),

    # Detalles de pedido
    path('pedido/<int:pedido_id>/agregar/', views.detalle_crear, name="detalle_crear"),
]

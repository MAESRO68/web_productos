from django.contrib import admin
from .models import Categoria, Producto, Pedido, DetallePedido

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre",)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio", "stock", "categoria")
    list_filter = ("categoria",)
    search_fields = ("nombre",)


class DetallePedidoInline(admin.TabularInline):
    model = DetallePedido
    extra = 1


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ("id", "cliente", "email", "fecha")
    inlines = [DetallePedidoInline]

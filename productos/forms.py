from django import forms
from .models import Producto, Pedido, DetallePedido

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ["nombre", "descripcion", "precio", "stock", "categoria", "imagen"]


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ["cliente", "email", "direccion"]


class DetallePedidoForm(forms.ModelForm):
    class Meta:
        model = DetallePedido
        fields = ["producto", "cantidad"]

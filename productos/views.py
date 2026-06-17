from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Pedido, DetallePedido
from .forms import ProductoForm, PedidoForm, DetallePedidoForm

# -------------------------
# PRODUCTOS
# -------------------------

def producto_listado(request):
    productos = Producto.objects.all()
    return render(request, "catalog/producto_listado.html", {"productos": productos})


def producto_detalle(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, "catalog/producto_detalle.html", {"producto": producto})


def producto_crear(request):
    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("producto_listado")
    else:
        form = ProductoForm()
    return render(request, "catalog/producto_form.html", {"form": form, "titulo": "Crear producto"})


def producto_editar(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect("producto_detalle", pk=producto.pk)
    else:
        form = ProductoForm(instance=producto)
    return render(request, "catalog/producto_form.html", {"form": form, "titulo": "Editar producto"})


def producto_borrar(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        producto.delete()
        return redirect("producto_listado")
    return render(request, "catalog/producto_confirmar_borrado.html", {"producto": producto})


# -------------------------
# PEDIDOS
# -------------------------

def pedido_listado(request):
    pedidos = Pedido.objects.all()
    return render(request, "catalog/pedido_listado.html", {"pedidos": pedidos})


def pedido_detalle(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    return render(request, "catalog/pedido_detalle.html", {"pedido": pedido})


def pedido_crear(request):
    if request.method == "POST":
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save()
            return redirect("pedido_detalle", pk=pedido.pk)
    else:
        form = PedidoForm()
    return render(request, "catalog/pedido_form.html", {"form": form, "titulo": "Crear pedido"})


def pedido_borrar(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == "POST":
        pedido.delete()
        return redirect("pedido_listado")
    return render(request, "catalog/pedido_confirmar_borrado.html", {"pedido": pedido})


# -------------------------
# DETALLES DE PEDIDO
# -------------------------

def detalle_crear(request, pedido_id):
    pedido = get_object_or_404(Pedido, pk=pedido_id)

    if request.method == "POST":
        form = DetallePedidoForm(request.POST)
        if form.is_valid():
            detalle = form.save(commit=False)
            detalle.pedido = pedido
            detalle.save()
            return redirect("pedido_detalle", pk=pedido.pk)
    else:
        form = DetallePedidoForm()

    return render(request, "catalog/pedido_form.html", {"form": form, "titulo": "Añadir producto al pedido"})

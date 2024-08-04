from django.shortcuts import render, redirect
from .models import Productos
from .forms import productoForm
from django.http import HttpResponse
from django.contrib import messages
import cv2
from pyzbar.pyzbar import decode
from django.http import JsonResponse
import json
import numpy as np
import base64

def index(request):
    productos = Productos.objects.filter(producto__contains=request.GET.get('search', ''))
    
    context = {
        'productos': productos
    }
    return render(request, 'productos/index.html', context)

def view(request, id):
    producto = Productos.objects.get(id=id)
    
    context = {
        'producto': producto
    }
    return render(request, 'productos/detail.html', context)

# Vista para editar productos  
def edit(request, id):
    producto = Productos.objects.get(id=id)
    
    if (request.method == "GET"):
        form = productoForm(instance=producto)
        context = {
          'form': form,
          'id': id
        }
        return render(request, 'productos/edit.html', context)
    
    if (request.method =='POST'):
        form = productoForm(request.POST, instance=producto)
        form.save()
        
        context = {
            'form': form,
            'id': id
        }
        messages.success(request, "¡Producto actualizado!")
        return render(request, 'productos/edit.html', context)
    
# Vista para escanear códigos de barras
def scan_barcode(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        image_data = data['image'].split(',')[1]
        image_data = base64.b64decode(image_data)
        np_arr = np.frombuffer(image_data, np.uint8)
        img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        for barcode in decode(img):
            barcode_data = barcode.data.decode('utf-8')
            try:
                product = Productos.objects.get(codigo_barras=barcode_data)
                product_info = {
                    'nombre': product.producto,
                    'venta': product.venta,
                    'cantidad': product.cantidad,
                }
                return JsonResponse({'product_info': product_info})
            except Productos.DoesNotExist:
                return JsonResponse({'product_info': None})

        return JsonResponse({'product_info': None})
    else:
        return render(request, 'productos/barcode_scanner.html')
    
    
# Vista para añadir productos
def create(request):
    if (request.method == 'GET'):
        form = productoForm()
        context = {
            'form': form
        }
        return render(request, 'productos/create.html', context)
    if request.method == 'POST':
        form = productoForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('productos')

# Vista para eliminar productos
def delete(request, id):
    producto = Productos.objects.get(id=id)
    producto.delete()
    messages.success(request, "Producto Eliminado")
    return redirect('productos')
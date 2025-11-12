from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_perfumeria, name='inicio_perfumeria'),

    # Cliente
    path('cliente/', views.ver_cliente, name='ver_cliente'),
    path('cliente/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('cliente/actualizar/<int:cliente_id>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('cliente/borrar/<int:cliente_id>/', views.borrar_cliente, name='borrar_cliente'),

    # Empleado
    path('empleado/', views.ver_empleado, name='ver_empleado'),
    path('empleado/agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('empleado/actualizar/<int:empleado_id>/', views.actualizar_empleado, name='actualizar_empleado'),
    path('empleado/borrar/<int:empleado_id>/', views.borrar_empleado, name='borrar_empleado'),

    # Venta Producto
    path('venta_producto/', views.ver_venta_producto, name='ver_venta_producto'),
    path('venta_producto/agregar/', views.agregar_venta_producto, name='agregar_venta_producto'),
    path('venta_producto/actualizar/<int:venta_id>/', views.actualizar_venta_producto, name='actualizar_venta_producto'),
    path('venta_producto/borrar/<int:venta_id>/', views.borrar_venta_producto, name='borrar_venta_producto'),
]

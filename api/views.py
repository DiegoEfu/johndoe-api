from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Fetch
def consulta_personas(request):
    try:
        return JsonResponse({'res': list(Persona.objects.all().values())})
    except Exception as e:
        print(str(e))

def consulta_vehiculos(request):
    return JsonResponse({'res': list(Vehiculo.objects.all().values())})

def consulta_mantenimiento(request):
    return JsonResponse({'res': list(Mantenimiento.objects.all().values())})

# Crear
@csrf_exempt
def crear_persona(request):
    try:
        body = request.POST

        Persona.objects.create(
            nombre = body['nombre'],
            apellido = body['apellido'],
            tipo = body['tipo'],
            cedula = body['cedula'],
            genero = body['genero']
        )

        return JsonResponse({'res': 200})
    except Exception as e:
        return JsonResponse({'res': 400, 'error': str(e)})

@csrf_exempt
def crear_vehiculo(request):
    try:
        body = request.POST

        Vehiculo.objects.create(
            dueno = Persona.objects.get(tipo = body['tipo'], cedula = body['cedula']),
            placa = body['placa'],
            marca = body['marca'],
            modelo = body['modelo'],
            color = body['color'],
        )

        return JsonResponse({'res': 200})
    except Exception as e:
        return JsonResponse({'res': 400, 'error': str(e)})
    
@csrf_exempt
def crear_mantenimiento(request):
    try:
        body = request.POST

        Mantenimiento.objects.create(
            vehiculo = Vehiculo.objects.get(placa=body['vehiculo']),
            fecha = body['fecha'],
            tipo = body['tipo']
        )

        return JsonResponse({'res': 200})
    except Exception as e:
        return JsonResponse({'res': 400, 'error': str(e)})

# Modificar
@csrf_exempt
def modificar_persona(request, pk):
    try:
        persona = Persona.objects.get(pk = pk)
        body = request.POST

        persona.nombre = body['nombre']
        persona.apellido = body['apellido']
        persona.genero = body['genero']

        persona.save()

        return JsonResponse({'res': 200})
    except Exception as e:
        return JsonResponse({'res': 400, 'error': str(e)})

@csrf_exempt
def modificar_vehiculo(request, pk):
    try:
        vehiculo = Vehiculo.objects.get(pk = pk)
        body = request.POST

        vehiculo.dueno = Persona.objects.get(tipo=body['tipo'],cedula=body['cedula'])
        vehiculo.marca = body['marca']
        vehiculo.modelo = body['modelo']
        vehiculo.color = body['color']

        vehiculo.save()

        return JsonResponse({'res': 200})
    except Exception as e:
        return JsonResponse({'res': 400, 'error': str(e)})

@csrf_exempt
def modificar_mantenimiento(request, pk):
    try:
        mantenimiento = Mantenimiento.objects.get(pk = pk)
        body = request.POST

        print(body['tipo'])

        mantenimiento.vehiculo = Vehiculo.objects.get(placa=body['vehiculo'])
        mantenimiento.tipo = body['tipo']
        mantenimiento.estado = body['estado']
        mantenimiento.fecha = body['fecha']
        mantenimiento.resultados = body.get('resultados')

        mantenimiento.save()

        return JsonResponse({'res': 200})
    except Exception as e:
        print(str(e))
        return JsonResponse({'res': 400, 'error': str(e)})

# Eliminar
@csrf_exempt
def eliminar_persona(request, pk):
    try:
        persona = Persona.objects.get(pk = pk)
        persona.delete()

        return JsonResponse({'res': 200})
    except Exception as e:
        return JsonResponse({'res': 400, 'error': str(e)})

@csrf_exempt
def eliminar_vehiculo(request, pk):
    try:
        vehiculo = Vehiculo.objects.get(pk = pk)
        vehiculo.delete()

        return JsonResponse({'res': 200})
    except Exception as e:
        return JsonResponse({'res': 400, 'error': str(e)})

@csrf_exempt
def eliminar_mantenimiento(request, pk):
    try:
        mantenimiento = Mantenimiento.objects.get(pk = pk)
        mantenimiento.delete()

        return JsonResponse({'res': 200})
    except Exception as e:
        return JsonResponse({'res': 400, 'error': str(e)})
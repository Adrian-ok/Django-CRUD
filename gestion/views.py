from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import datetime ,timedelta, date
from django.contrib import messages
from .fecha import *
from .models import *


#-----------------------------------------------------------------------------------------------------------------------#
#INICIO APP
@login_required(redirect_field_name='/')
def home(request):
    data = persona.objects.all()
    hoy = datetime.today()
    cont = 0
    for i in data.iterator():
        venc = i.venc_libreta
        dia = i.recordar
        x = timedelta(days = dia)
        fecha = hoy + x

        aux = venc.strftime("%Y-%d-%m %H:%M:%S")
        vencimiento = datetime.strptime(aux, "%Y-%d-%m %H:%M:%S")

        if fecha >= vencimiento:
            cont = cont + 1

    if cont > 0:
        messages.warning(request, message=f'Se detectaron {cont} vencimientos')
        return render(request, 'home.html')
    else:
        return render(request, 'home.html')
#-----------------------------------------------------------------------------------------------------------------------#
#AÑADIR UN NUEVO REGISTRO
@login_required(redirect_field_name='/')
def nuevo_personal(request):
    if request.method == 'GET':
        sangre_list = grup_sangre.objects.all()
        estado_list = estado.objects.all()
        loc_list = localidad.objects.all()
        sector_list = sector.objects.all()

        return render(request, 'nuevo_personal.html', {
            'sangre': sangre_list,
            'estado': estado_list,
            'localidad': loc_list,
            'sector': sector_list
        })
    else:
        apellido = request.POST['apellido']
        nombre = request.POST['nombre']
        dni = request.POST['dni']
        direccion = request.POST['direccion']
        telefono = request.POST['telefono']
        cant_hijos = request.POST['cant_hijos']
        nro_legajo = request.POST['nro_legajo']
        instruccion = request.POST['instruccion']
        titulo = request.POST['titulo']
        renovacion = request.POST['renovacion']
        venc_libreta = request.POST['venc_libreta']
        fe_nac = request.POST['fn']
        fe_ing = request.POST['fi']
        
        valor = request.POST.getlist('casa')
        if valor==['yes']:
            casa=1
        else:
            casa=0

        personaa = persona.objects.create(apellido=apellido, nombre=nombre, dni=dni, direccion=direccion, 
                                          telefono=telefono, cant_hijos=cant_hijos, nro_legajo=nro_legajo,
                                          instruccion=instruccion, titulo=titulo, renovacion=renovacion,
                                          venc_libreta=venc_libreta, casa=casa, fn=fe_nac, fi=fe_ing,
                                          localidad=localidad.objects.get(id_localidad = request.POST['localidadd']),
                                          estado_civil=estado.objects.get(id_estado = request.POST['estadoC']),
                                          grup_sangre=grup_sangre.objects.get(id_sangre = request.POST['grup_sangree']),
                                          sector=sector.objects.get(id_sector = request.POST['sectorr']))
        
        personaa.save()
        messages.success(request, 'Agregado Correctamente')
        return redirect('nuevo_personal')
#-----------------------------------------------------------------------------------------------------------------------#
#FILTRA TODOS LOS EMPLEADOS 
@login_required(redirect_field_name='/')
def filtrar_personal(request):
    if request.method == 'GET':
        lista_personal = persona.objects.all()
        return render(request, 'filtrar_personal.html', {
            'personal': lista_personal,
        })
    else:
        nro = request.POST.get('nro')
        apellido = request.POST.get('apellido')
        if nro == '' and apellido == '':
            lista_personal = persona.objects.all()
        elif nro != '' and apellido == '':
            lista_personal = persona.objects.filter(nro_legajo=nro)
        elif nro == '' and apellido != '':
            lista_personal = persona.objects.filter(apellido=apellido)
        else:
            lista_personal = persona.objects.filter(apellido=apellido, nro_legajo=nro)


        return render(request, 'filtrar_personal.html', {
            'personal': lista_personal
        })

#-----------------------------------------------------------------------------------------------------------------------#
#VER LA INFORMACION COMPLEATA DE LOS EMPLEADOS
@login_required(redirect_field_name='/')
def ver_completo(request, nro_legajo):
    if request.method == 'GET':
        lista_personal = persona.objects.filter(nro_legajo=nro_legajo)
        return render(request, 'ver_completo.html', {
            'personal': lista_personal,
        })

#-----------------------------------------------------------------------------------------------------------------------#
#ELIMINAR UN REGISTRO
@login_required(redirect_field_name='/')
def eliminar(request, id):
    eliminar = persona.objects.get(id=id)
    eliminar.delete()
    return redirect('filtrar_personal')

#-----------------------------------------------------------------------------------------------------------------------#
#SELECCIONAR EDITAR
@login_required(redirect_field_name='/')
def selectEdicion(request, id):
    edicion = persona.objects.get(id=id)
    list_sangre = grup_sangre.objects.all()
    list_estado = estado.objects.all()
    list_localidad = localidad.objects.all()
    list_sector = sector.objects.all()

    return render(request, 'selectEdicion.html', {
            'edicion': edicion,
            'sangre': list_sangre,
            'estado': list_estado,
            'localidad': list_localidad,
            'sector': list_sector,
        })
#-----------------------------------------------------------------------------------------------------------------------#
#EDITAR
@login_required(redirect_field_name='/')
def editar_pesonal(request):
        id_=request.POST['id']
        nro_legajo = request.POST['nro_legajo']
        apellido = request.POST['apellido']
        nombre = request.POST['nombre']
        dni = request.POST['dni']
        telefono = request.POST['telefono']
        direccion = request.POST['direccion']
        cant_hijos = request.POST['cant_hijos']
        instruccion = request.POST['instruccion']
        titulo = request.POST['titulo']
        fe_nac = request.POST['fn']
        fe_ing = request.POST['fi']
        renovacion = request.POST['renovacion']
        venc_libreta = request.POST['venc_libreta']
        localidadd=localidad.objects.get(id_localidad = request.POST['localidadd'])
        estado_civill=estado.objects.get(id_estado = request.POST['estadoC'])
        grup_sangree=grup_sangre.objects.get(id_sangre = request.POST['grup_sangree'])
        sectorr=sector.objects.get(id_sector = request.POST['sectorr'])
        valor = request.POST.getlist('casa')
        if valor==['yes']:
            casa=1
        else:
            casa=0

        edicion = persona.objects.get(id=id_)
        edicion.nro_legajo=nro_legajo
        edicion.apellido=apellido
        edicion.nombre=nombre
        edicion.dni=dni
        edicion.telefono=telefono
        edicion.direccion=direccion
        edicion.cant_hijos=cant_hijos
        edicion.instruccion=instruccion
        edicion.titulo=titulo
        edicion.fn=fe_nac
        edicion.fi=fe_ing
        edicion.renovacion=renovacion
        edicion.venc_libreta=venc_libreta
        edicion.localidad=localidadd
        edicion.estado_civil=estado_civill
        edicion.grup_sangre=grup_sangree
        edicion.sector=sectorr
        edicion.casa=casa

        edicion.save()
        messages.success(request, 'Modificado Correctamente')
        return redirect('home')



#-----------------------------------------------------------------------------------------------------------------------#
#MUESTRA SOLAMENTE LOS REGISTROS CON LIBRETA VENCIDA
@login_required(redirect_field_name='/')
def vencidos(request):
    hoy = date.today()
    x = timedelta(days = 15)
    fecha = hoy + x

    if request.method == 'GET':
        venci = persona.objects.filter(venc_libreta__lte= fecha)
        return render(request, 'vencidos.html',{'venci': venci})
    else:
        nro = request.POST.get('nro')
        apellido = request.POST.get('apellido')
        if nro == '' and apellido == '':
            venci = persona.objects.filter(venc_libreta__lte= fecha)
        elif nro != '' and apellido == '':
            venci = persona.objects.filter(nro_legajo=nro).filter(venc_libreta__lte= fecha)
        elif nro == '' and apellido != '':
            venci = persona.objects.filter(apellido=apellido).filter(venc_libreta__lte= fecha)
        else:
            venci = persona.objects.filter(nro_legajo=nro, apellido=apellido).filter(venc_libreta__lte= fecha)

        return render(request, 'vencidos.html', {
            'venci': venci
        })

#-----------------------------------------------------------------------------------------------------------------------#
#CREAR EL REPORTE DE TODOS LOS EMPLEADOS 
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

@login_required(redirect_field_name='/')
def reportepdf(request):
    template = get_template('reporte.html')
    persona_list = persona.objects.all()
    context = {'persona': persona_list}
    html = template.render(context)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reportPersonal.pdf"'

    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
#-----------------------------------------------------------------------------------------------------------------------#
#REPORTE VENCIMIENTOS

@login_required(redirect_field_name='/')
def vencipdf(request):

    hoy = date.today()
    x = timedelta(days = 15)
    fecha = hoy + x
    venci = persona.objects.filter(venc_libreta__lte= fecha)

    template = get_template('vencipdf.html')
    context = {'venci': venci}
    html = template.render(context)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reportLibVenc.pdf"'

    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
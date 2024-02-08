
from django.shortcuts import render, redirect
from django.http import HttpResponse
from optica.models import Lentes, Usuario

def mostrarIni(request):
    return render (request,'Login.html')


def Inisesion(request):
    if request.method == 'POST':
        nom = request.POST["txtusu"]
        pas = request.POST["txtpas"]

        comprobarLogin = Usuario.objects.filter(nombre_usuario=nom,password_usuario=pas).values()

        if comprobarLogin:
            request.session['estadoSesion'] = True
            request.session['idUsuario'] = comprobarLogin[0]['id']
            request.session['nomUsuario'] = nom.upper()

            datos = {'nomUsuario':nom.upper()}

            if nom.upper() == 'ADMIN':
                return render(request,'Formulario.html', datos)
            else:
                return render(request,'Formulario.html',datos)
        else:
            datos = {'r2': 'error de usuario/contraseña'}  
            return render(request, 'Login.html', datos)
    
    else:
        datos = {'r2': 'Errorerror404'}
        return render(request, 'Login.html', datos)

def cerrarSesion(request):
    try:
        del request.session['estadosesion']
        del request.session['nomUsuario']
        del request.session['idUsuario']

        return render(request,'Login.html')
    except:
        return render(request,'Login.html')


def mostrarForm(request):
    return render(request, 'formulario.html')

def formulario(request):
    if request.method == 'POST':
        laboratorio = request.POST['laboratorio']
        producto = request.POST['producto']
        codigo = request.POST['codigo']
        indice = float(request.POST['indice'])
        precio = float(request.POST['precio'])
        antireflejo = request.POST['antireflejo']
        filtro_azul = request.POST['filtro_azul']
        fotocromatica = request.POST['fotocromatica']
        polarizado = request.POST['polarizado']
        esfera = float(request.POST['esfera'])
        cilindro = float(request.POST['cilindro'])
        material = request.POST['material']

        lentes = Lentes(
            laboratorio=laboratorio,
            producto=producto,
            codigo=codigo,
            indice=indice,
            precio=precio,
            antireflejo=antireflejo,
            filtro_azul=filtro_azul,
            fotocromatica=fotocromatica,
            polarizado=polarizado,
            esfera=esfera,
            cilindro=cilindro,
            material=material,
        )
        lentes.save()

        datos = {
            'nomUsuario': request.session["nomUsuario"],

            'r' : 'Producto Agregado correctamente'
        }

        return render(request,'Formulario.html',datos)  

    return render(request, 'Formulario.html')
def mostrarListar(request):
    query = request.GET.get('buscar', '')
    if query:
        lentes = Lentes.objects.filter(producto__icontains=query).values().order_by("producto")
    else:
        lentes = Lentes.objects.all().order_by("producto")

    antireflejo = request.GET.getlist('antireflejo')
    filtro_azul = request.GET.getlist('filtro_azul')
    polarizado = request.GET.getlist('polarizado')
    fotocromatica = request.GET.getlist('fotocromatica')
    #material = request.GET.getlist('material')

    if 'si' in antireflejo:
        lentes = lentes.filter(antireflejo='si')
    if 'no' in antireflejo:
        lentes = lentes.exclude(antireflejo='si')

    if 'si' in filtro_azul:
        lentes = lentes.filter(filtro_azul='si')
    if 'no' in filtro_azul:
        lentes = lentes.exclude(filtro_azul='si')

    if 'si' in polarizado:
        lentes = lentes.filter(polarizado='si')
    if 'no' in polarizado:
        lentes = lentes.exclude(polarizado='si')

    if 'si' in fotocromatica:
        lentes = lentes.filter(fotocromatica='si')
    if 'no' in fotocromatica:
        lentes = lentes.exclude(fotocromatica='si')

    #if 'policarbonato' in policarbonato:
        #lentes = lentes.filter(material='policarbonato')
    #if 'mineral' in mineral:
        #lentes = lentes.filter(material='mineral')
    #if 'organico' in organico:
        #lentes = lentes.filter(material='organico')


    nomUsuario = request.session.get("nomUsuario", "")

    return render(request, "listar.html", {'producto': lentes, 'query': query, 'nomUsuario': nomUsuario})



def eliminarProducto(request, id):
    try:
        producto = Lentes.objects.get(id=id)
        nombre_producto = producto.producto
        producto.delete()
        return redirect('listar')  
    except Lentes.DoesNotExist:
        return HttpResponse('El producto no existe', status=404)

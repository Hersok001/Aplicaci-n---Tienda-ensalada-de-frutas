from django.shortcuts import redirect, render
from .forms import FormularioContacto
from django.core.mail import EmailMessage

# Create your views here.

def contacto(request):
    formulario_contacto=FormularioContacto


    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")
            
            #Metodo que envia el formulario a nuestro correo
            email=EmailMessage("Mensaje desde App Django",
            "El usuario con el nombre {},con la dirección de correo {}, escribe lo siguiente:\n\n {}".format(nombre,email,contenido),"",
            ["acá_ira_el_correo_deldueño@gmail.com"],reply_to=[email])

            try:
                email.send()                
                #codigo para recargar la pagina al llenar el formulario del contacto
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")





    return render(request, 'contacto/contacto.html',{'miFormulario':formulario_contacto})
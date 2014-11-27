from django.shortcuts import render, render_to_response
from django.template import RequestContext

from .forms import *


def registro_view(request):
    formulario_registro=fusuario()
    return render_to_response("usuario/registro_user.html",{'formulario':formulario_registro},context_instance=RequestContext(request))
from __future__ import unicode_literals

from django.utils import timezone
from django.db import models

#from usuario.models import Perfil, OpcionesPerfil, Departamento
#from empresa.models import Empresa, EmpresaEstado, CorrelativoTipo
#from factura.models import FacturaEstado, TipoFactura
#from finanzas.models import TipoCierre, TipoMoneda, Moneda

#from productos.models import Productos, ProductoRegistrado, UnidadMedida

from django.contrib.auth.models import User

def poblar():
### AUTH / SUPER USER ###
    User.objects.create_superuser('admin', 'ing.marcelo.sanabria@gmail.com', 'SanabriA')
    print("super user ----> Creado!")
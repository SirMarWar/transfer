from __future__ import unicode_literals

from django.utils import timezone
from django.db import models

#from usuario.models import Perfil, OpcionesPerfil, Departamento
#from empresa.models import Empresa, EmpresaEstado, CorrelativoTipo
#from factura.models import FacturaEstado, TipoFactura
#from finanzas.models import TipoCierre, TipoMoneda, Moneda

#from productos.models import Productos, ProductoRegistrado, UnidadMedida

from django.contrib.auth.models import User


def InitDB():
    #CREATE DATABASE
    '''
    CREANDO LA BASE DE DATOS
    '''
    print("Creando base de datos")
    import psycopg2
    from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
    # Connect to PostgreSQL DBMS
    con = psycopg2.connect("user=postgres password='SanabriA'")
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    # Obtain a DB Cursor
    cursor          = con.cursor()
    name_Database   = "moneytransfer"
    # Create table statement
    sqlCreateDatabase = "create database "+name_Database+";"
    # Create a table in PostgreSQL database
    cursor.execute(sqlCreateDatabase);
    print("Database ----> Creada!")

    '''
    MIGRAR TABLAS A LA BASE DE DATOS
    '''
    print("Migrando tablas a la BD...!")
    from django.core.management import execute_from_command_line
    execute_from_command_line(["manage.py", "migrate"])
    print("Migracion ----> Terminada!")

    '''
    POBLAR TABLAS
    '''
    print("Iniciando poblacion de datos")



    ### AUTH / SUPER USER ###
    User.objects.create_superuser('admin', 'ing.marcelo.sanabria@gmail.com', 'SanabriA')
    print("super user ----> Creado!")
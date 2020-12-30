from __future__ import unicode_literals
import sys
import subprocess

from django.utils import timezone
from django.db import models

from django.contrib.auth.models import User


def InstallEnvironment(self):
    self.apt = "apt "
    self.ins = "install "
    self.packages = (
        "install python3 python3-pip python3-dev postgresql postgresql-contrib"
    )
    self.color.print_green("[+] Installation of the environment startint:")
    for self.items in self.package.split():
        self.command = str(self.apt) + str(self.ins) + str(self.items)

        subprocess.run(self.command.split())
        self.color.print_yellow("\t[+] Package [{}] Installed".format(str(self.items)))


def InitDB():
    # CREATE DATABASE
    """
    CREANDO LA BASE DE DATOS
    """
    print("Creando base de datos")
    import psycopg2
    from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

    # Connect to PostgreSQL DBMS
    con = psycopg2.connect("user=postgres password='SanabriA'")
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    # Obtain a DB Cursor
    cursor = con.cursor()
    name_Database = "moneytransfer"
    # Create table statement
    sqlCreateDatabase = "create database " + name_Database + ";"
    # Create a table in PostgreSQL database
    cursor.execute(sqlCreateDatabase)
    print("Database ----> Creada!")

    """
    MIGRAR TABLAS A LA BASE DE DATOS
    """
    print("Migrando tablas a la BD...!")
    from django.core.management import execute_from_command_line

    execute_from_command_line(["manage.py", "makemigrations"])
    print("MakeMigrations ----> Terminada!")
    execute_from_command_line(["manage.py", "migrate"])
    print("Migracion ----> Terminada!")

    """
    POBLAR TABLAS
    """
    print("Iniciando poblacion de datos")

    ### AUTH / SUPER USER ###
    User.objects.create_superuser("admin", "ing.marcelo.sanabria@gmail.com", "SanabriA")
    print("super user ----> Creado!")

    customer1 = User.objects.create_user("customer1", "customer1@gmail.com", "SanabriA")
    customer1.is_superuser = False
    customer1.is_staff = False
    customer1.save()
    print("customer1 ----> Creado!")
# ==============================
# IMPORTACIONES
# ==============================

from fastapi import FastAPI  # Import propio del framework FastAPI
from typing import List      # Import estandar de Python para tipado


# ==============================
# CREACION DE LA APLICACION
# ==============================

app = FastAPI()  # Objeto principal de la API (instancia del framework)


# ==============================
# BASE DE DATOS SIMULADA
# ==============================

clientes = []  # Variable global tipo lista para almacenar clientes en memoria


@app.get("/")  # Decorador propio de FastAPI para metodo GET
def home():
    return {"mensaje": "API del Banco funcionando"}


@app.post("/clientes")  # Decorador para metodo POST
def crear_cliente(nombre: str):  # Parametro recibido por query
    cliente = {
        "id": len(clientes) + 1,  # Generacion simple de ID
        "nombre": nombre
    }

    clientes.append(cliente)  # Agrega cliente a lista global

    return cliente  # Devuelve cliente creado


@app.get("/clientes", response_model=List[dict])  # Define tipo de respuesta
def listar_clientes():
    return clientes  # Devuelve lista completa


@app.get("/clientes/{cliente_id}")  # Ruta con parametro dinamico
def obtener_cliente(cliente_id: int):  # Tipo parametro entero
    for cliente in clientes:  # Recorre lista
        if cliente["id"] == cliente_id:
            return cliente  # Retorna si encuentra

    return {"error": "Cliente no encontrado"}  # Manejo basico de error
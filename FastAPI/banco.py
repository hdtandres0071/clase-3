# ==============================
# IMPORTACIONES
# ==============================

from fastapi import FastAPI
from typing import List
import asyncio   # Para simular delay asincrono

# ==============================
# CREACION DE LA APLICACION
# ==============================

app = FastAPI()

# ==============================
# BASE DE DATOS SIMULADA
# ==============================

clientes = []                # lista de clientes
contador_clientes = 0        # contador global de clientes creados


# ==============================
# ENDPOINT PRINCIPAL
# ==============================

@app.get("/")
def home():
    return {"mensaje": "API del Banco funcionando"}


# ==============================
# CREAR CLIENTE (POST)
# ==============================

@app.post("/clientes")
async def crear_cliente(nombre: str):

    global contador_clientes

    # Validacion
    if nombre.strip() == "":
        return {"error": "El nombre no puede estar vacío"}

    # Simulacion de delay de 3 segundos
    await asyncio.sleep(3)

    cliente = {
        "id": len(clientes) + 1,
        "nombre": nombre
    }

    clientes.append(cliente)

    contador_clientes += 1

    return {
        "cliente_creado": cliente,
        "total_clientes_creados": contador_clientes
    }


# ==============================
# LISTAR CLIENTES
# ==============================

@app.get("/clientes", response_model=List[dict])
def listar_clientes():
    return clientes


# ==============================
# OBTENER CLIENTE POR ID
# ==============================

@app.get("/clientes/{cliente_id}")
def obtener_cliente(cliente_id: int):

    for cliente in clientes:
        if cliente["id"] == cliente_id:
            return cliente

    return {"error": "Cliente no encontrado"}


# ==============================
# ACTUALIZAR CLIENTE (PUT)
# ==============================

@app.put("/clientes/{cliente_id}")
def actualizar_cliente(cliente_id: int, nombre: str):

    if nombre.strip() == "":
        return {"error": "El nombre no puede estar vacío"}

    for cliente in clientes:
        if cliente["id"] == cliente_id:
            cliente["nombre"] = nombre
            return {"mensaje": "Cliente actualizado", "cliente": cliente}

    return {"error": "Cliente no encontrado"}


# ==============================
# ELIMINAR CLIENTE (DELETE)
# ==============================

@app.delete("/clientes/{cliente_id}")
def eliminar_cliente(cliente_id: int):

    for cliente in clientes:
        if cliente["id"] == cliente_id:
            clientes.remove(cliente)
            return {"mensaje": "Cliente eliminado"}

    return {"error": "Cliente no encontrado"}
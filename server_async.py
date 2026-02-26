import asyncio  # importa la librería para programación asíncrona

# Función que maneja cada cliente (coroutine)
async def handle_client(reader, writer):
    # Espera datos del cliente (Máximo 1024 bytes)
    data = await reader.read(1024)

    name = data.decode()

    response = f"Hola {name}"

    writer.write(response.encode())

    await writer.drain()

    writer.close()
    await writer.wait_closed()  # recomendable agregar esto


async def main():
    server = await asyncio.start_server(
        handle_client, "0.0.0.0", 5000
    )

    async with server:
        await server.serve_forever()


asyncio.run(main())
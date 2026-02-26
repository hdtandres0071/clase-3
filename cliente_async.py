import asyncio
import time

async def main():

	reader, writer = await asyncio.open_connection(
		"127.0.0.1", 5000
	)

	name = input("Ingresa tu nombre: ")

	start_time = time.time()

	writer.write(name.encode())

	await writer.drain()

	data = await reader.read(1024)

	end_time = time.time()

	print(data.decode())

	print(f"Tiempo de atencion: {round(end_time - start_time, 2)} segundos")


	writer.close()
	await writer.wait_closed()

asyncio.run(main())
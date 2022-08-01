import logging
import asyncio
import uvicorn
from uvicorn.loops.asyncio import asyncio_setup
from mifaker.main import app

# Set some basic logging
logging.basicConfig(
    level=3,
    format="%(asctime)-15s %(levelname)-8s %(message)s"
)

# async def start_uvicorn():
#     config = uvicorn.config.Config(app, host='0.0.0.0', port=8000)
#     server = uvicorn.server.Server(config)
#     await server.serve()


# async def main(loop):
#     await asyncio.create_task(start_uvicorn())
#     # await asyncio.wait([
#     #     asyncio.create_task(start_uvicorn()),
#     # ], return_when=asyncio.FIRST_COMPLETED)


# if __name__ == '__main__':
#     asyncio_setup()
#     loop = asyncio.get_event_loop()
#     asyncio.run(main(loop))


def main():
    asyncio.run(
        uvicorn.run(
            "mifaker.main:app",
            host="localhost",
            port=8000,
            reload=True
        )
    )


if __name__ == "__main__":
    main()

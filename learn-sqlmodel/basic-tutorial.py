import asyncio
from hero.models import Hero
from hero.db import init_db

async def main():
    await init_db()

if __name__ == "__main__":
    asyncio.run(main())
    print("Done")
    
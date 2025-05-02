import asyncio
import time


async def play():
    print("enter play")
    for _ in range(5):
        # time.sleep(1)
        await asyncio.sleep(1)
        for _ in range(1000):
            pass


async def main():
    print("enter main")
    start = time.time()
    tasks = []
    for _ in range(10):
        play_coro = play()
        tasks.append(asyncio.create_task(play_coro))
    # for t in tasks:
    #     await t
    print(await asyncio.gather(*tasks))
    print(f"total time: {time.time() - start} seconds")


main_coro = main()
asyncio.run(main_coro)

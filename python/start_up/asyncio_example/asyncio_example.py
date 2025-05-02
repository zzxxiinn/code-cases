import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)
    return f"{what} - {delay}"


async def con():
    print(1)


async def main():
    print(f"1 started at {time.strftime('%X')}")

    await say_after(1, "hello")
    await say_after(2, "world")
    print(f"1 finished at {time.strftime('%X')}")

    print(f"2 started at {time.strftime('%X')}")

    task1 = asyncio.create_task(say_after(1, "hello"))
    task2 = asyncio.create_task(say_after(2, "world"))

    ret1 = await task1  # hello - 1
    ret2 = await task2  # world - 2
    print(ret1)
    print(ret2)

    print(f"2 finished at {time.strftime('%X')}")
    print(f"3 started at {time.strftime('%X')}")

    ret = await asyncio.gather(task1, task2)
    print(ret)  # ['hello - 1', 'world - 2']
    print(f"3 finished at {time.strftime('%X')}")

    print(f"4 started at {time.strftime('%X')}")

    ret = await asyncio.gather(say_after(1, "hello"), say_after(2, "world"))
    print(ret)  # ['hello - 1', 'world - 2']
    print(f"4 finished at {time.strftime('%X')}")


asyncio.run(main())

"""
asyncio 不是新的运行机制，本质上 asyncio 还是一个 python 运行的单进程单线程的程序，并不能提升运算速度。他比较适合处理需要等待的任务，如网络的通讯。其核心是 event-loop。
coroutine - task
- coroutine function 和 coroutine object
    - 所有 async 开头的函数都叫 co-function, 定义了一个调用过程
    - 所有 co-function 调用后会生产 co-object, 与生成器类似
- 使用 await , 会有如下操作
    - 生成一个 future 对象返回
    - 通知 event-loop 当前 task 需要等到前一个 task 执行完之后才能执行
    - 会已类似 生成器 yield 方式，通知 event 先执行其他的 task。

- asyncio 的 eventloop 无法主动选择（强行）从task中拿回控制权，需要 task 主动把控制权交回去

- eventloop 调度的最小单位是 task，不能直接调度 coroutine object
"""

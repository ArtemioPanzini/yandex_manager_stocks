from modules.Beauty_light3.main_st_bl3 import main as st_bl3
from modules.Nebesniy_svet.main_st_ns import main as st_ns
import asyncio
import threading


def async_in_thread(coro):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(coro())


if __name__ == "__main__":
    thread1 = threading.Thread(target=async_in_thread, args=(st_ns,))
    thread2 = threading.Thread(target=async_in_thread, args=(st_bl3,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

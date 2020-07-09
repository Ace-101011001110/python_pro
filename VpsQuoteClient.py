import asyncio
import time
import logging
from threading import Thread
from nats.aio.client import Client as NATS
from nats.aio.errors import ErrConnectionClosed, ErrTimeout

class Component:
    component = None

    def __init__(self):
        self.nc = NATS()
        self.loop = asyncio.new_event_loop()
        if not Component.component:
            Component.component = Component.__Component(self.nc, self.loop)
        self.connect(["nats://192.168.20.185:4222"])

    def request(self, subject, data):
        # Required to be able to run the coroutine in the proper thread.
        task = self.loop.create_task(Component.component.request(subject, data))
        self.loop.run_until_complete(task)
        return task.result()

    def connect(self, servers):
        self.loop.run_until_complete(Component.component.connect(servers))

    class __Component:

        def __init__(self, nc, loop):
            self.nc = nc
            self.loop = loop
            
        async def publish(self, subject, data):
            await self.nc.publish(subject, data)

        async def request(self, subject, data):
            msg = await self.nc.request(subject, data.encode("utf-8"))
            return msg

        async def msg_handler(self, msg):
            print(f"--- Received: {msg.subject} {msg.data} {msg.reply}")
            await self.nc.publish(msg.reply, b'I can help!')

        async def connect(self, servers):
            await self.nc.connect(servers=servers, loop=self.loop)

        async def receive(self, cb):
            await self.nc.subscribe("*", cb=cb)
            await self.nc.flush()

        async def run(self):
            await self.nc.subscribe("help", cb=self.msg_handler)
            await self.nc.flush()

if __name__ == '__main__':
    # go()
    component = Component()
    msg = component.request("eb.qt.ltqtick.fut.us.get", "eb.qt.ltqtick.fut.us.NDX20200900")
    print(msg.data)
    while True:
        time.sleep(10)

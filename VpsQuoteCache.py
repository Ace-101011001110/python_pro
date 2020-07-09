import asyncio
import time
import logging
from threading import Thread
from nats.aio.client import Client as NATS
from nats.aio.errors import ErrConnectionClosed, ErrTimeout

class VpsQuoteCache():
    component = None

    def __init__(self):
        self.nc = NATS()
        self.loop = asyncio.new_event_loop()
        if not VpsQuoteCache.component:
            VpsQuoteCache.component = VpsQuoteCache.__Component(self.nc, self.loop)
        self.connect(["nats://127.0.0.1:4222"])
        self.revMsg = {}

    def publish(self, subject, data):
        # Required to be able to run the coroutine in the proper thread.
        asyncio.run_coroutine_threadsafe(
            VpsQuoteCache.component.publish(subject,data),
            loop=self.loop)

    def request(self, subject, data):
        # Required to be able to run the coroutine in the proper thread.
        future = asyncio.run_coroutine_threadsafe(
            VpsQuoteCache.component.request(subject, data),
            loop=self.loop)
        return future.result()

    def connect(self, servers):
        self.loop.run_until_complete(VpsQuoteCache.component.connect(servers))

    def run(self):
        asyncio.run_coroutine_threadsafe(VpsQuoteCache.component.run(), loop=self.loop)

        # Without this the ping interval will fail
        self.loop.run_forever()

    def subscribe(self):
        asyncio.run_coroutine_threadsafe(VpsQuoteCache.component.subscribe(self.receiveCb), loop=self.loop)
        self.loop.run_forever()

    def receiveCb(self, msg):
        if msg.subject == "get":
            replyMsg = b'no data'
            if msg.data.decode("utf-8") in self.revMsg:
                replyMsg = self.revMsg[msg.data.decode("utf-8")]
            self.publish(msg.reply, replyMsg)
        else:
            self.revMsg[msg.subject] = msg.data
        print("receiveCb:", msg, msg.data, self.revMsg )

    class __Component:

        def __init__(self, nc, loop):
            self.nc = nc
            self.loop = loop
            
        async def publish(self, subject, data):
            await self.nc.publish(subject, data)

        async def request(self, subject, data):
            msg = await self.nc.request(subject, data)
            return msg

        async def connect(self, servers):
            await self.nc.connect(servers=servers, loop=self.loop)

        async def subscribe(self, cb):
            await self.nc.subscribe("*", cb=cb)
            await self.nc.flush()



if __name__ == '__main__':
    # go()
    vpsQuoteCache = VpsQuoteCache()
    # component.receive()
    while True:
        vpsQuoteCache.subscribe()
        time.sleep(1)

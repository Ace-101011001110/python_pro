from nats.aio.client import Client as NATS

class NatsComponent:
    def __init__(self, loop):
        self.nc = NATS()
        self.loop = loop
    
    async def connect(self, servers):
        await self.nc.connect(servers=servers, loop=self.loop, error_cb=self.error_cb, disconnected_cb=self.disconnected_cb, closed_cb=self.closed_cb,discovered_server_cb=self.discovered_server_cb)

    async def publish(self, subject, data):
        await self.nc.publish(subject, data)

    async def request(self, subject, data):
        msg = await self.nc.request(subject, data)
        return msg

    async def subscribe(self, subject, cb):
        await self.nc.subscribe(subject, cb=cb)
        await self.nc.flush()

    async def subscribeQuery(self, querySubject, cb):
        await self.nc.subscribe(querySubject, cb=cb)
        await self.nc.flush()
    
    def error_cb(self, msg):
        print("ERROR:NatsComponent:", msg)

    def disconnected_cb(self, msg):
        print("DISCONNECTED:NatsComponent:", msg)

    def closed_cb(self, msg):
        print("CLOSE:NatsComponent:", msg)

    def discovered_server_cb(self, msg):
        print("DISCOVERED:NatsComponent:", msg)
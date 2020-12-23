from hubris import Hub


hub = Hub()
channel = hub['example']
subscription = channel.subscribe(lambda s, v: print(v))

input('Press any key to quit...\n')

#subscription.cancel()
hub.close()
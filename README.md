# Hubris
Hubris is a simple library for implementing inter-process communication (IPC)
between separate Python processes. It's based on named pipes created by the
POSIX `mkfifo` system call.

Hubris uses the "channel" metaphor. You can send and receive data on a with
simple send and receive commands. Alternatively, you can have multiple
processes subscribe to the a single channel on which data is published
asynchronously or at a regular interval.

## Sending Data
```python
hub = Hub()
channel = hub['example']

# send data (which is serialized internally)
channel.send({'foo': 'bar'})

hub.close()
```

## Receiving Data
Receiving data can be done synchronously or asynchronously.
```python
hub = Hub()
channel = hub['example']

# block until we receive the data
data = channel.receive()

# ...or immediately return a future object
future = channel.receive(wait=False)
data = future.result(timeout=1)

hub.close()
```

## Publishing Data
Data can be published at a regular interval.
```python
hub = Hub()
channel = hub['example']

# send data (which is serialized internally)
channel.publish({'foo': 'bar'}, interval=timedelta(seconds=1))

# ...or generate data with a callback
channel.publish(generate, interval=timedelta(seconds=1))

# ...or just send data as normally to have it published to subscribers
channel.send({'foo': 'bar'})

hub.close()
```

## Subscribing to Channels
You can subscribe a callback to receive and respond to data published on a channel.
```python
hub = Hub()
channel = hub['example']

# subscribe this thread to the channel, triggering
# callback upon receipt of data
channel.subscribe(lambda: subscription, data: print(data))

hub.close()
```

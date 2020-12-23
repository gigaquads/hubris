import sys
import signal

from time import sleep
from datetime import datetime, timedelta

from hubris import Hub


def pub(channel):
    """
    Start publishing a data payload at regular 1-second intervals.

    """
    def fetch():
        """
        Example function that simulates fetching data from some source.
        """
        return {
            'time': datetime.now(),
            'message': 'Hello, world!',
        }

    channel.publish(fetch, interval=timedelta(seconds=1))

    input('Press any key to quit...\n')

    hub.close()


def sub(channel):
    """
    Subscribe to the channel to which we are publishing.
    """
    subscription = channel.subscribe(lambda s, v: print(v))

    input('Press any key to stop...\n')

    #subscription.cancel()
    hub.close()


if __name__ == "__main__":
    mode = sys.argv[1].lower()
    main = { 'pub': pub, 'sub': sub }[mode]

    hub = Hub()
    channel = hub['example']

    signal.signal(signal.SIGINT, lambda *args: hub.close())

    main(channel)
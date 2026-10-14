class Blog:
    def __init__(self,name):
        self.name=name
        self._sub=[]   #initial subscribers
        self._latestPost=None

    def subscriber(self,subscriber):
        if subscriber not in self._sub:
            print(f"{subscriber.email}subscribed to {self.name}")

    def unsubscribe(self,subscriber):
        if subscriber in self._sub:
            self._sub.remove(subscriber)
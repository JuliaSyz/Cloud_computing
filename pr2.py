class Enent_bus(object):
    def __init__(self):
        self.subs = {}

    def subscribe(self, event_name, callback):
        if event_name not in self.subs.keys():
            self.subs[event_name] = [callback]
        else:
            self.subs[event_name].append(callback)

    def publish(self, event_name, data):
        if event_name in self.subs.keys():
            for callback in self.subs[event_name]:
                callback(data)

    def unsubscribe(self, event_name, callback):
        if event_name in self.subs.keys():
            self.subs[event_name].remove(callback)
            if len(self.subs[event_name]) == 0:
                del self.subs[event_name]

bus = Enent_bus()

callback = lambda x: print("call1: "+x)
callback2 = lambda x: print("call2: "+x)

bus.subscribe("enent1", callback)
bus.subscribe("enent1", callback2)

bus.publish("enent1", "event 1")

bus.unsubscribe("enent1", callback)
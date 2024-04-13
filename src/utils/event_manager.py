# Product event types
PRODUCT_ADDED = 'product_added'
PRODUCT_DELETED = 'product_deleted'

# User event types
USER_REGISTERED = 'user_registered'
USER_LOGGED_IN = 'user_logged_in'

class EventManager:
    def __init__(self):
        self.listeners = dict()

    def subscribe(self, event_type, listener):
        if event_type not in self.listeners:
            self.listeners[event_type] = []
        self.listeners[event_type].append(listener)

    def publish(self, event_type, data=None):
        if event_type in self.listeners:
            for listener in self.listeners[event_type]:
                listener(data)
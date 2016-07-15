from __future__ import unicode_literals

class Event(object):
    """A simple signals based observer pattern event class with overload sugar
    
    Example:
        def my_handler():
            print("Handled")

        def my_other_handler():
            print("Other Handler")

        my_signal = Event()
        my_signal += my_handler

        #also valid:
        my_signal += [my_handler, my_other_handler]

        my_signal()
    
    """

    def __init__(self):
        super(Event, self).__init__()

        self._signals = list()

    def add(self, handler):
        """Adds a callback handler"""

        if handler is not None:
            if isinstance(handler, list):
                self._signals.extend(handler)
            else:
                self._signals.append(handler)

    def remove(self, handler):
        """Removes a callback handler"""
        if not isinstance(handler, list):
            handler = [handler]

        for h in handler:
            if h in self._signals:
                self._signals.remove(h)

    def __call__(self, *args, **kwargs):
        """Syntax sugar, allows calling instance as a method"""

        for handler in self._signals:
            if handler is not None:
                handler(*args, **kwargs)

    def __contains__(self, item):
        """Returns true if item was already added as a handler"""

        return item in self._signals

    def __iadd__(self, other):
        """Syntax sugar, short hand for add(callback)"""

        self.add(other)
        return self

    def __isub__(self, other):
        """Syntax sugar, short hand for remove(callback)"""

        self.remove(other)
        return self

if __name__ == "__main__":
    # example usage
    def handler1(e):
        print(" - Handler1: %s" % e)

    def handler2(e):
        print(" - Handler2: %s" % e)


    # create signal/slot
    signal = Event()
    
    # add event handler
    signal += handler1

    # call event
    print("- First Call")
    signal("First Call")

    # add second handler
    signal += handler2

    # call event
    print("\n- Second Call")
    signal("Second Call")

    # remove all handlers
    signal -= handler1
    signal -= handler2

    #event call
    print("\n- Third Call(no handlers)")

    # add multiple handlers at once
    signal += [handler1, handler2]

    #event call
    print("\n- Fourth Call")
    signal("Fourth Call")

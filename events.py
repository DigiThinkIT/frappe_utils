from __future__ import unicode_literals

class Event(object):
    """A simple signals based observer pattern event class with overload sugar
    
    Example:
        def my_handler():
            print("Handled")

        my_signal = Event()
        my_signal += my_handler

        my_signal()
    
    """

    def __init__(self):
        super(Event, self).__init__()

        self._signals = list()

    def add(self, handler):
        """Adds a callback handler"""

        if handler is not None:
            self._signals.append(handler)

    def remove(self, handler):
        """Removes a callback handler"""
        if handler in self._signals:
            self._signals.remove(handler)

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


# Copyright (c) Jifeng Wu
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.
import threading

SENTINEL = object()


class MessageBoard(object):
    __slots__ = ('lock', 'condition', 'value')

    def __init__(self):
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)
        self.value = SENTINEL

    def set(self, value):
        with self.condition:
            self.value = value
            self.condition.notify_all()

    def peek(self):
        with self.condition:
            while self.value is SENTINEL:
                self.condition.wait()

            return self.value

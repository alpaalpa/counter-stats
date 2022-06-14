import pytest

from stats import CounterEvent

NAME = "a-name"

class TestCounterEvent():
    def setup(self):
        self.stats = CounterEvent(name=NAME)

    def test_name(self):
        assert self.stats.name == NAME
        d = self.stats.snapshot()
        assert d.name == NAME

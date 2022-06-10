import json
from time import sleep, time

from stats import CounterEvent

stats = CounterEvent(name="ThingsCounter")

# the following loops automatically creates 3 counts split up into 2 different
# groups.
for i in range(0, 10):
    stats.increment('counter1', 'group1', increment=1)
    stats.increment('counter1', 'group1', increment=1)
    stats.increment('counter2', 'group1', increment=1)
    stats.increment('counter2', 'group1', increment=1)
    stats.increment('counter3', 'group2', increment=1)
    sleep(1)

# Get a snapshot of the counters and the group aggregates

# stop_ts needs to be specified as you might have multiple CounterEvent() objects
# that you want to use the same stop timestamp
stop_ts = time()
# Gets a dictionary (munch)
stats_snapshot = stats.snapshot(update_stats=True, stop_ts=stop_ts)
# pretty print the dict
print(json.dumps(stats_snapshot, indent=4))
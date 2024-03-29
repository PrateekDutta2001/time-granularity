import time
from datetime import datetime, timedelta

class TimeGranularity:
    def __init__(self, granularity):
        self.granularity = granularity

    def run(self, func):
        if self.granularity == 'minute':
            self._run_every_minute(func)
        elif self.granularity == 'hour':
            self._run_every_hour(func)
        elif self.granularity == 'day':
            self._run_every_day(func)
        elif self.granularity == 'week':
            self._run_every_week(func)
        elif self.granularity == 'month':
            self._run_every_month(func)
        else:
            raise ValueError("Invalid granularity specified")

    def _run_every_minute(self, func):
        while True:
            func()
            time.sleep(60)

    def _run_every_hour(self, func):
        while True:
            func()
            time.sleep(3600)

    def _run_every_day(self, func):
        while True:
            func()
            tomorrow = datetime.now() + timedelta(days=1)
            next_midnight = datetime(year=tomorrow.year, month=tomorrow.month, day=tomorrow.day)
            wait_seconds = (next_midnight - datetime.now()).seconds
            time.sleep(wait_seconds)

    def _run_every_week(self, func):
        while True:
            func()
            next_week = datetime.now() + timedelta(weeks=1)
            next_week_start = next_week - timedelta(days=next_week.weekday())
            wait_seconds = (next_week_start - datetime.now()).seconds
            time.sleep(wait_seconds)

    def _run_every_month(self, func):
        while True:
            func()
            next_month = datetime.now().replace(day=28) + timedelta(days=4)
            next_month_start = next_month - timedelta(days=next_month.day - 1)
            wait_seconds = (next_month_start - datetime.now()).seconds
            time.sleep(wait_seconds)

# Example usage:
def example_function():
    print("This function is executed at regular intervals.")

granularity = 'minute'  # Change this to 'hour', 'day', 'week', or 'month' as needed
time_granularity = TimeGranularity(granularity)
time_granularity.run(example_function)

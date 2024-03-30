# time-granularity

## Execution

To use the time_granularity package, you can follow these steps:

1. Install the package:
   ```bash
   pip install time-granularity

Use the package in your Python code:

```bash
from time_granularity import TimeGranularity
# usage
granularity = 'minute'  # Change this to 'hour', 'day', 'week', or 'month' as needed
time_granularity = TimeGranularity(granularity)
time_granularity.run(example_function)

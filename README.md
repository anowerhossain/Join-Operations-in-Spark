### Join Types and Their Descriptions

| Join Type          | Description                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| **Inner Join**      | Returns rows that have matching keys in both DataFrames                     |
| **Left Outer Join** | Returns all rows from the left DataFrame, with matching rows from the right (or null if no match) |
| **Right Outer Join**| Returns all rows from the right DataFrame, with matching rows from the left (or null if no match) |
| **Full Outer Join** | Returns all rows from both DataFrames, with null for missing matches        |
| **Left Semi Join**  | Returns rows from the left DataFrame that have matching rows in the right DataFrame, without any right DataFrame columns |
| **Left Anti Join**  | Returns rows from the left DataFrame that do not have matching rows in the right DataFrame |
| **Cross Join**      | Returns the Cartesian product of the two DataFrames (every row from the left joined with every row from the right) |


```python
from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder.appName("JoinExample").getOrCreate()
```

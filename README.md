### Join Types and Their Descriptions 🔗
Join operations allow you to combine two DataFrames or RDDs based on a common column or condition. Spark supports several types of joins, each with its own behavior and use case. Here are the different types of join operations in Spark:

| Join Type          | Description                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| **Inner Join**      | Returns rows that have matching keys in both DataFrames                     |
| **Left Outer Join** | Returns all rows from the left DataFrame, with matching rows from the right (or null if no match) |
| **Right Outer Join**| Returns all rows from the right DataFrame, with matching rows from the left (or null if no match) |
| **Full Outer Join** | Returns all rows from both DataFrames, with null for missing matches        |
| **Left Semi Join**  | Returns rows from the left DataFrame that have matching rows in the right DataFrame, without any right DataFrame columns |
| **Left Anti Join**  | Returns rows from the left DataFrame that do not have matching rows in the right DataFrame |
| **Cross Join**      | Returns the Cartesian product of the two DataFrames (every row from the left joined with every row from the right) |


### Set up Spark session 🚀
```python
from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder.appName("JoinExample").getOrCreate()
```

### Load CSV files into DataFrames 📥
```python
# Load the CSV files into DataFrames
employees_df = spark.read.option("header", "true").csv("employees.csv")
salaries_df = spark.read.option("header", "true").csv("salaries.csv")

# Show the loaded data
employees_df.show()
salaries_df.show()
```

### 🔗 Inner Join: 
Returns only the rows that have matching keys in both DataFrames. This means the result will only include rows where employee_id is present in both the employees_df and salaries_df.

```python
inner_join_df = employees_df.join(salaries_df, on="employee_id", how="inner")
```

### 🔻 Left Outer Join: 
Returns all rows from the left DataFrame (employees_df) and the matching rows from the right DataFrame (salaries_df). If no match is found in the right DataFrame, null values are returned for columns from the right.

```python
left_outer_join_df = employees_df.join(salaries_df, on="employee_id", how="left")
```

### 🔄 Right Outer Join:
Returns all rows from the right DataFrame (salaries_df) and the matching rows from the left DataFrame (employees_df). If no match is found in the left DataFrame, null values are returned for columns from the left.

```python
right_outer_join_df = employees_df.join(salaries_df, on="employee_id", how="right")
```

### 🌍 Full Outer Join: 
Returns all rows from both DataFrames. If no match is found on either side, null values are inserted for the missing side.

```python
full_outer_join_df = employees_df.join(salaries_df, on="employee_id", how="outer")
```

### 🔍 Left Semi Join: 
Returns rows from the left DataFrame (employees_df) that have matching rows in the right DataFrame (salaries_df), but only the columns from the left DataFrame are included.

```python
left_semi_join_df = employees_df.join(salaries_df, on="employee_id", how="leftsemi")
```

### 🚫 Left Anti Join:
Returns rows from the left DataFrame (employees_df) that do not have matching rows in the right DataFrame (salaries_df).

```python
left_anti_join_df = employees_df.join(salaries_df, on="employee_id", how="leftanti")
```

### 🔄 Cross Join:
Returns the Cartesian product of the two DataFrames. This means every row from the left DataFrame is joined with every row from the right DataFrame.

```python
cross_join_df = employees_df.crossJoin(salaries_df)
```

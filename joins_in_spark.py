from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName("JoinExample").getOrCreate()

# Sample Data for 'employees.csv'
data_employees = [
    (1, "HR", "New York"),
    (2, "Engineering", "Boston"),
    (3, "Marketing", "Chicago"),
    (4, "HR", "Boston")
]

# Sample Data for 'salaries.csv'
data_salaries = [
    (1, 60000),
    (2, 80000),
    (3, 70000),
    (4, 75000)
]

# Define schema for DataFrames
columns_employees = ["employee_id", "department", "location"]
columns_salaries = ["employee_id", "salary"]

# Create DataFrames
employees_df = spark.createDataFrame(data_employees, columns_employees)
salaries_df = spark.createDataFrame(data_salaries, columns_salaries)

# Show DataFrames
employees_df.show()
salaries_df.show()

# 🌟 INNER JOIN (Only matching rows)
inner_join_df = employees_df.join(salaries_df, on="employee_id", how="inner")
print("Inner Join (Only matching rows) 🌟")
inner_join_df.show()

# 🔻 LEFT JOIN (All rows from left, matching from right)
left_outer_join_df = employees_df.join(salaries_df, on="employee_id", how="left")
print("Left Join (All rows from left, matching from right) 🔻")
left_outer_join_df.show()

# 🔄 RIGHT JOIN (All rows from right, matching from left)
right_outer_join_df = employees_df.join(salaries_df, on="employee_id", how="right")
print("Right Join (All rows from right, matching from left) 🔄")
right_outer_join_df.show()

# 🌍 FULL OUTER JOIN (All rows from both sides)
full_outer_join_df = employees_df.join(salaries_df, on="employee_id", how="outer")
print("Full Outer Join (All rows from both sides) 🌍")
full_outer_join_df.show()

import duckdb

# Connect to an in-memory DuckDB database
con = duckdb.connect(database=':memory:', read_only=False)

# Create a table and insert data
con.execute("CREATE TABLE my_table (id INTEGER, name VARCHAR)")
con.execute("INSERT INTO my_table VALUES (1, 'Alice'), (2, 'Bob')")

# Query the data
result = con.execute("SELECT * FROM my_table").fetchdf()
print(result)

# Close the connection
con.close()
<h4 id=parquet><a href=#act_ref>Parquet</a></h4>

Parquet is a column-based table format. This enables efficient compression and it allows for the efficient reading a column subsets. In addition, due to the concept of row groups it can also allow for the efficient reading of row subsets. These features make Parquet interesting for handling very large tabular data.

- Create a table in memory
- Save the table as Parquet
- Read the stored Parquet table
    - If the library supports it, explore
        - Only reading a subset of columns
        - Only reading a subset of rows

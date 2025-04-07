# Code from: https://arrow.apache.org/docs/python/parquet.html

import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

# %
# create a dataframe
df = pd.DataFrame({'label_id': [1, 2, 3],
                   'area_um2': ['100.0', '151.3', '121.3'],
                   'circularity': [0.92, 0.73, 0.55]} )

# %
# save df as parquet
table = pa.Table.from_pandas(df)
table_file_path = "cells.parquet"
pq.write_table(table, table_file_path)

# %
# read a column subset
table = pq.read_table(table_file_path, columns=['label_id', 'area_um2'])
print(table)

# %
# convert to pandas dataframe
df = table.to_pandas()
print(df)

# %
# TODO:
# - Write and read "row groups"
#!/usr/bin/env python3
import sys
import pandas as pd

input_file = sys.argv[1]    # supplier_data.csv
output_file = sys.argv[2]   # output_files/1output.csv
data_frame=pd.read_csv(input_file)
print(data_frame)
data_frame.to_csv(output_file, index=True)
import pandas as pd
import numpy as np

# Specify the path to your CSV file

# Company = pd.read_csv('data/company.csv')
# X = np.array(Company.Description.to_json())
# print(X)

# # Output: {"0":"Company Description 1","1":"Company Description 2","2":"Company Description 3","3":"Company Description 4","4":"Company Description 5","5":"Company Description 6","6":"Company Description 7","7":"Company Description 8","8":"Company Description 9","9":"Company Description 10"}


import json

# Read data from file
with open('output.json', 'r') as file:
    data = json.load(file)

# Transform data
input_data = {
    "input_data": list(data.values())
}

# Write transformed data to a new file
with open('transformed_data.json', 'w') as outfile:
    json.dump(input_data, outfile, indent=2)

print("Data has been written to transformed_data.json")

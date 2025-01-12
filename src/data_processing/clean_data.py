import pandas as pd
import numpy as np

def clean_data(file_path, output_path):
    """
    Cleans the raw data and writes the cleaned data to a new file.

    args:
        file_path (str): The path to the raw data file.
        output_path (str): The path to write the cleaned data to.
    """

    data = pd.read_csv(file_path)

    # Replace invalid coes with NaN
    invalid_codes = [999, 888]
    data.replace(invalid_codes, np.nan, inplace=True)

    # Handle missing numerical data
    numerical_cols = data.select_dtype(include=['float64', 'int64']).columns
    data[numerical_cols] = data[numerical_cols].fillna(data[numerical_cols].mean())

    # handle missing categorical values
    categorical_cols = data.select_dtypes(include=['object']).columns
    data[categorical_cols] = data[categorical_cols].fillna('Unknown')

    # Save the cleaned data
    data.to_csv(output_path, index=False)
    print(f"Cleand data saved to {output_path}.")
import pandas as pd

def load_data(file_path):
    """
    Loads data from csv file given path

    args:
    - file_path (str): path to the data file

    returns:
    - Dataframe: Pandas DataFrame containing the loaded data
    """

    data = pd.read_csv(file_path)
    return data

def load_stata_data(file_path):
    """
    Load the the STATA file which contains variable names and Labels

    Args:
    - file_path (str): path to the stata file

    returns:
    - Dataframe: Pandas DataFrame containing the loaded variables and labels
    """
    
    stata_data = pd.read_stata(file_path, convert_categoricals=False)

    return stata_data

# display all columns within the dataset
def display():
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

    print('Display All Columns Feature Activated')

def null_columns(data):
    """"
    Check if any column is completely null within the dataset

    Args:
    - data (DataFrame): complete dataset

    Returns:
    - null columns
    """
    
    is_null_column = data.isnull().all()

    return data.columns[is_null_column]

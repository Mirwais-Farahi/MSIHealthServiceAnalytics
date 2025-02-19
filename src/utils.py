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

def summary_percentage_table(data, variable_list, question_mapping, channels_column, channels=None):
    """
    Generate a summary table with percentages for each question grouped by channels.

    Parameters:
    - data: pd.DataFrame, the dataset containing the questions, answers, and region information.
    - variable_list: list of str, the list of questions (column names) to analyze.
    - question_mapping: dict, a mapping of variable names to full question text.
    - channels_column: str, the column name representing channels in the dataset.
    - channels: list of str, the list of channels to include in the analysis (default: unique values in the channels column).

    Returns:
    - pd.DataFrame, the summary table.
    """
    if channels is None:
        channels = data[channels_column].unique()  # Get unique channels if not provided

    # Initialize a list to store the result rows
    results = []

    # Iterate through each question in the variable list
    for question in variable_list:
        # Get unique answers for the question
        answers = data[question].dropna().unique()

        # Iterate through each answer
        for answer in answers:
            row = {
                "Question": question_mapping.get(question, question),  # Use full text or fallback to variable name
                "Answers": answer
            }

            # Initialize a list to store the percentages for each region
            channel_percentages = []

            # Calculate percentage for each region
            for channel in channels:
                channel_data = data[data[channels_column] == channel]
                total_channels = len(channel_data)
                answer_count = (channel_data[question] == answer).sum()
                percentage = (answer_count / total_channels) * 100 if total_channels > 0 else 0

                # Store the percentage for the region
                row[channel] = f"{percentage:.2f}%"

                # Accumulate the percentage for the total row
                channel_percentages.append(percentage)

            # Calculate the average percentage for the total row
            row["Total"] = f"{sum(channel_percentages) / len(channel_percentages):.2f}%" if channel_percentages else "0.00%"

            # Append the row to results
            results.append(row)

    # Convert results to a DataFrame
    summary_table = pd.DataFrame(results)

    return summary_table
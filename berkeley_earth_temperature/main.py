import pandas as pd
import datetime


def parse_temperature_file(file_path: str):
    """Parses the Berkeley Earth Land and Ocean temperature data file.

    Args:
        file_path (str): Path to the temperature data file.

    Returns:
        pandas.DataFrame: DataFrame containing the parsed temperature data.
    """

    # Read the file into a list of lines
    with open(file_path, 'r') as f:
        lines = f.readlines()

    # Skip the header lines
    data_lines = lines[87:]
    len_data_lines = len(data_lines)

    # Initialize
    df_list = []

    # Parse each data line
    for i, line in enumerate(data_lines):
        print(f"Processing line {i} out of {len_data_lines}")
        # Split the line into columns
        columns = line.strip().split()

        # Does not handle the next set of data
        if line == ' \n':
            break

        # Convert the date string to a datetime object
        date_string = f"{columns[0]}-{columns[1]}"
        date_format = "%Y-%m"
        date = datetime.datetime.strptime(date_string, date_format)

        # Convert the temperature values to floats
        temperature_values = [float(value) for value in columns[2:]]

        # Create a dictionary with the parsed data
        data_row = {
            "date": date,
            "monthly_anomaly": temperature_values[0],
            "monthly_anomaly_uncertainty": temperature_values[1],
            "annual_anomaly": temperature_values[2],
            "annual_anomaly_uncertainty": temperature_values[3],
            "five_year_anomaly": temperature_values[4],
            "five_year_anomaly_uncertainty": temperature_values[5],
            "ten_year_anomaly": temperature_values[6],
            "ten_year_anomaly_uncertainty": temperature_values[7],
            "twenty_year_anomaly": temperature_values[8],
            "twenty_year_anomaly_uncertainty": temperature_values[9],
        }

        # Append the data row to the DataFrame
        df_list.append(data_row)

    # Create a dataframe
    df = pd.DataFrame(df_list)

    return df


# Parse the temperature data file
df = parse_temperature_file(file_path="land_and_ocean.txt")

# Save
df.to_csv("global_average_temperature_anomaly_with_sea_ice_temperature.csv", index=False)


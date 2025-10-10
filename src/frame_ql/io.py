from .frame import DataFrame

def read_csv(filepath, separator=','):
    """
    Reads a comma-separated values (csv) file into a DataFrame.

    This is a simple, in-memory implementation. It assumes the entire
    file can be loaded into memory.

    Args:
        filepath (str): The path to the CSV file.
        separator (str): The delimiter to use. Defaults to a comma.

    Returns:
        DataFrame: A DataFrame object containing the data from the CSV file.
    """
    with open(filepath, 'r') as f:
        lines = f.readlines()

    # header line
    header = [h.strip() for h in lines[0].split(separator)]
    
    # Initialize a dictionary to hold our data
    data_dict = {col: [] for col in header}

    # Process the rest of the lines
    for line in lines[1:]:
        if not line.strip():  # Skip empty lines
            continue
        
        values = [v.strip() for v in line.split(separator)]
        
        # assumption: number of values matches number of headers
        for i, col_name in enumerate(header):
            data_dict[col_name].append(values[i])
            
    return DataFrame(data_dict)

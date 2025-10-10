import textwrap

class DataFrame:
    """A 2D labeled table like data structure
    
    Properties:
        shape: Returns the dimensioality of (rows,column)
        columns: Returns the column labels of DataFrame
    """

    def __init__(self, data):
        """Initializes dataframe

        Args:
            data (dict): a dictionary where keys are the column names and
                         values are the list of column data.

        Raises:
            TypeError: If input data is not a dictionary
            ValueError: If the lists for the columns are not of the same length

        """
        if not isinstance(data, dict):
            raise TypeError("Input data should be a dictionary.")
        
        # convert all value sequences to lists 
        processed_data = {k: list(v) for k, v in data.items()}
        
        # validate the column lists length with data
        list_lengths = iter(len(v) for v in processed_data.values())
        first_len = next(list_lengths, None)
        if not all(l == first_len for l in list_lengths):
            raise ValueError("All column lists must be of same length.")
        
        self._data = processed_data
        self._columns = list(processed_data.keys())

    @property
    def shape(self):
        num_rows = len(self._data[self._columns[0]] if self._columns else 0)
        num_cols = len(self._columns)
        return (num_rows, num_cols)

    @property
    def columns(self):
        """
        Returns: The number of columns for the data.
        """
        return self._columns
    
    def head(self, n=5):
        """
        Args: 
            n (int) : number of rows to be shown by default

        Returns:
            DataFrame: A new dataframe object which contains n data rows
        """

        head_data = {col: val[:n] for col,val in self._data.items()}
        return self.__class__(head_data)
    
    def __repr__(self):
        """
        Returns: 
            A string representation of the dataframe with pretty formatting.
        """
        num_rows, num_cols = self.shape
        header = f"DataFrame Shape: ({num_rows},{num_cols})\n"

        # Only the head of the dataframe will be shown as the preview.
        df_head = self.head()

        # header
        col_str = " | ".join(f"{col:<15}" for col in df_head.columns)
        header_line = "-" * len(col_str)

        # rows
        row_strs = []
        for i in range(df_head.shape[0]):
            row = [str(df_head._data[col][i]) for col in df_head.columns]
            row_strs.append(" | ".join(f"{item:<15}" for item in row))

        body = "\n".join(row_strs)

        return f"{header}\n{col_str}\n{header_line}\n{body}"
    

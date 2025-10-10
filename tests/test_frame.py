import os
from frame_ql import DataFrame, read_csv

def test_dataframe_creation_and_shape():
    """Tests the basic creation and shape property of the DataFrame."""
    data = {'col1': [1, 2, 3], 'col2': ['A', 'B', 'C']}
    df = DataFrame(data)
    assert df.shape == (3, 2)
    assert df.columns == ['col1', 'col2']

def test_dataframe_head():
    """Tests the head() method."""
    data = {'id': range(10), 'value': [i * 2 for i in range(10)]}
    df = DataFrame(data)
    
    head_default = df.head()
    assert head_default.shape == (5, 2)
    assert head_default._data['id'] == [0, 1, 2, 3, 4]

    head_3 = df.head(3)
    assert head_3.shape == (3, 2)
    assert head_3._data['id'] == [0, 1, 2]

def test_read_csv():
    """Tests the basic in-memory read_csv function."""
    # Create a dummy CSV file for testing
    file_content = "student_id,class,score\n101,A,85\n102,B,92\n103,A,78"
    file_path = "temp_test.csv"
    with open(file_path, "w") as f:
        f.write(file_content)

    df = read_csv(file_path)

    # Assertions
    assert isinstance(df, DataFrame)
    assert df.shape == (3, 3)
    assert df.columns == ['student_id', 'class', 'score']
    assert df._data['score'] == ['85', '92', '78']

    # Clean up the dummy file
    os.remove(file_path)

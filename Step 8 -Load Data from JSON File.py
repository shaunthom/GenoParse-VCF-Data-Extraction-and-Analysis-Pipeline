def load_data_from_json(filename):
    import json
    with open(filename) as file:
        return json.load(file)

"""
A function whose input is a filename for a json file. 
The function should use the filename to read the JSON file in 
which you saved your final parsed data. 
"""

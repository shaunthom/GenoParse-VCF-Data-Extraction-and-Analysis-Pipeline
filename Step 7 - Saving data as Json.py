def save_data_as_json(data, filename):
    import json
    bool_value_F = False
    bool_value_T = True
    json_f = open("./" + filename , 'w', encoding = 'utf-8')
    json.dump(data, json_f, sort_keys = bool_value_T, indent = 4, separators = (',', ': '), ensure_ascii = bool_value_F)

  """
    The function will save the dictionary as a json file using the filename given. 
    Use this function to save your parsed data as a json file.
"""

def determine_data_type(value):
    
    try:
        value = int(value)
        return type(value)
    except ValueError:
        try:
            value = float(value)
            return type(value)
        except ValueError:
            return str



def determine_data_type_of_list(values):
   
    c = 0
    l=[]
    for value in values:
        dtype = determine_data_type(value)
        if dtype == str:
            return str
            break
        elif dtype == float:
            c = c + 1

    if c == 0:
        return int
    else:
        return float

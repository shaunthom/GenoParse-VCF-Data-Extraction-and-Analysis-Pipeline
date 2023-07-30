final_dict = {}
    list_format = format_field.split(':')
    #splitting the format field
    item_keys = list(sample_field.keys())
    list10 = []
    #accessing the keys in the sample_field dictionary
    i = [0]
    while i[0] <= (len(item_keys)-1):
        item_key = item_keys[i[0]]
        output_field_dict = {}
        value_sample_field = sample_field[item_key].split(':')
        #generating the list of sample field dictionary values
        list10.extend(value_sample_field)
        j,k = 0,1
        while j <= (len(list_format)-1):

            field_key = list_format[j]
            field_value = value_sample_field[j]
            output_field_dict[field_key] = field_value
            j = j+1
        final_dict[item_key] = output_field_dict
        k = k+1
        i[0] = i[0]+1

    return final_dict

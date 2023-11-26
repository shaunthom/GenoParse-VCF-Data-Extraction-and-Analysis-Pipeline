def create_dictionary_of_info_field_values(data):
    info_field_values_dict = {}

    for line in data:
        meta_fields = line.split(';')
        for field in meta_fields:
            key_value = field.split('=', 1)
            if len(key_value) == 2 and key_value[1] != '.':
                key, value = key_value
                if key in info_field_values_dict:
                    info_field_values_dict[key].add(value)
                else:
                    info_field_values_dict[key] = {value}

    # Convert sets back to lists for the output
    for key in info_field_values_dict:
        info_field_values_dict[key] = list(info_field_values_dict[key])

    return info_field_values_dict

"""
 This is a function that first takes the info fields and turns them into a dictionary. I have made sure to skip any fields that do not have a value or are missing a value.
"""

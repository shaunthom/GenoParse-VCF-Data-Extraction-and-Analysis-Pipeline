info_field_values_dict = {}
    value_list =[]
    i,j = 1,1
    num = [1,2,3]
    t_dict = {}
    for line in data:
        meta_1 = line.split(';', -1)
        value_list.clear()
        #initializing value_list = [] also works!!
        for eq in meta_1:
            #splitting it ino 2 items
            value_list.append(eq.split('=', 1))
        for var in value_list:
            i=[1]
            while i[0]<=(len(var)-num[0]):
                if not var[i[0]] == '.':
                    if var[0] in info_field_values_dict:
                        count = 0
                        for j in info_field_values_dict.get(var[0]):
                            if j == var[i[0]]:
                                #avoiding duplicate values
                                count = 99
                                break
                        if count == 0:
                            info_field_values_dict[var[0]].append(var[i[0]])
                    else:
                        info_field_values_dict[var[0]] = [var[i[0]]]
                i[0] = i[0] + num[0]
    return info_field_values_dict

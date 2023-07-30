sample_dict = {}
    l_line = line.split('\t')
    inter_dict={}
    m =[10,0,20,1]
    for item in range(m[1],len(header),m[3]):
        inter_dict[header[item]]=l_line[item]
    a=inter_dict['FORMAT']
    del inter_dict['FORMAT']
    for item in inter_dict:
        if item == "":
            continue
    sample_li = []
    b={}
    c=[]
    n = 9
    sample_list= header[n::1]
    i=[0,1]
    while i[0]<=(len(sample_list)-i[1]):
        b[sample_list[i[0]]]=inter_dict[sample_list[i[0]]]
        sample_li.append(sample_list[i[0]])
        del inter_dict[sample_list[i[0]]]
        c.append(sample_list)
        i[0] = i[0]+i[1]
    sample_dict.clear()
    sample_dict = format_sample_fields(a,b)
    inter_dict['SAMPLE']=sample_dict
    return inter_dict

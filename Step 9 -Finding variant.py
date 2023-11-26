def find_variant(CHROM, REF, ALT, POS, filename):
    data_loaded = load_data_from_json(filename)
    f_variant_list=[]
    for row in data_loaded:
        if (row['CHROM']==CHROM and row['REF']==REF and row['ALT']==ALT and row['POS']==POS):
            f_variant_list.append(row)
        else:
            continue
    return f_variant_list

"""
A function whose inputs are CHROM, REF, ALT, POS, and filename. 
    Using these inputs, the function should load a JSON file using the given 
    filename and return a list of variants that match the given CHROM, REF, ALT, and POS. 
"""

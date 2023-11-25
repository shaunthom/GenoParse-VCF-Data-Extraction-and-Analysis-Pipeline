def read_vcf_file(filename):
    variant_list = []
    header = None

    with open(filename) as file:
        for line in file:
            line = line.strip()
            if line.startswith('##'):
                continue
            elif line.startswith('#'):
                header = line.strip('#').split('\t')
            elif header:
                variant_dict = create_dict_from_line(header, line)
                variant_list.append(variant_dict)

    return variant_list

"""
 The function reads the vcf file one variant at a time and transforms it 
    into a dictionary using the create_dict_from_line function. 
    It returns a list containing all the variant dictionaries.
"""

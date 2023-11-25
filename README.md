# Bio-Gene_Format_Extracter

It is a genetic related project.
We will be manipulating a file. This file has one thousand variants in it. Each line after the header lines is a variant. We shall open the variant file and inspect its contents. We will parse each line and transform it into a dictionary. The final output will be a list of dictionaries.


### Introduction:

Variant Call Format (VCF) files are a standardized format used in bioinformatics for storing gene sequence variations. These files are particularly important in the fields of genomics and medical genetics.

Format: A VCF file is a text file with a specific structure. It starts with meta-information lines marked by '##', followed by a header line starting with '#'. After the header, each line represents a genetic variant.

Columns: The standard columns in a VCF file include:

1. CHROM: Chromosome number
2. POS: Position of the variant on the chromosome
3. ID: Identifier of the variant, if available
4. REF: Reference allele (the allele present in the reference genome)
5. ALT: Alternative allele(s) (the differing allele(s) at this position)
6. QUAL: Quality score of the variant call
7. FILTER: Indicates if the variant has passed quality filters
8. INFO: Additional information on the variant, in a key=value format
FORMAT and sample columns: These provide genotyping information for each sample if the VCF file includes multiple samples.

### Project Overview:

The VCF file will be parsed line-by-line, post the header lines. Each variant line is converted into a dictionary format. An example dictionary entry is truncated below for illustration:

{
    "ALT": "G",
    "CHROM": "4",
    "FILTER": "PASS",
    "ID": ".",
    "INFO": {
        "Gene.ensGene": "ENSG00000109471,ENSG00000138684",
        "Gene.refGene": "IL2,IL21",
        ...
    },
    "POS": 123416186,
    "QUAL" :23.25,
    "REF": "A",
    "SAMPLE": {
        "XG102": {
            "AD": "51,8",
            "DP": "59",
            ...
        }
    }
}

### Key Features:

Parsing VCF Files: Read and transform VCF file lines into dictionary entries.

Header Management: Identification and skipping of header lines beginning with double hashes (##).

Predictor Field Extraction: Implementation of pull_basic_and_predictor_fields function, which reads project_data.json and selects variants based on specific predictor fields (like FATHMM_pred, LRT_pred, MetaLR_pred, etc.).

Integer Mapping of Predictors: Convert predictor text descriptions to integer values and sum these into sum_predictor_values.

Processing Gzip Files: A function pull_basic_and_predictor_fields_gzip to handle gzipped VCF files, with output in mini_project1_gzip.json.

Filtering Non-Zero Predictors: return_all_non_zero_sum_predictor_values function selects variants with non-zero sum_predictor_values, outputting sum_predictor_values_gt_zero.json


### Contributing

Contributions to improve the functionality or efficiency of the code are welcome. Please follow the standard GitHub pull request process.

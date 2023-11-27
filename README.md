# Bio-Gene_Format_Extracter

This project involves genetic data analysis. We'll be working with a file containing a thousand genetic variants. Each variant is listed on a separate line following the introductory header lines. Our task involves opening this variant file to examine its details. We will process each line, converting it into a dictionary format. The end result will be a compilation of these dictionaries.

### Why do we need such a file parser?

The purpose of this project is to effectively analyze and manage genetic data, particularly the genetic variants contained in a Variant Call Format (VCF) file. Here are some key reasons for undertaking this task:

1. Facilitating Data Analysis: Genetic data, especially in VCF format, contains complex and detailed information about genetic variations. Converting each line of data into a dictionary format simplifies the data structure, making it easier to analyze and manipulate

2. Standardizing Data Format: By transforming each variant into a dictionary, the data is standardized, allowing for consistent processing and analysis.

3. Enhancing Accessibility and Usability: Dictionaries are a more accessible format for many computational processes.

4. Preparing for Advanced Applications: The simplified, dictionary-based format of the data paves the way for more advanced computational techniques, such as machine learning models, which can be used for predictive analysis, identifying patterns, and making significant biological discoveries.

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

### Step-by-Step Overview:

##### Step 1: Determining Data Type

Purpose: Analyze and identify the data types present in the VCF file.

##### Step 2: Formatting Sample Fields

Purpose: Format and standardize the sample-specific fields in the VCF file.

##### Step 3: Creating Dictionary from Line

Purpose: Transform each line of the VCF file into a dictionary format for easier data manipulation.

##### Step 4: Reading VCF Files

Purpose: Read and process VCF files, preparing the data for further analysis.

##### Step 5: Extracting Info Field

Purpose: Extract and process the 'INFO' field from each line in the VCF file.

##### Step 6: Creating Dictionary with Info Field

Purpose: Generate dictionaries keyed by 'INFO' field values from the VCF file data.

##### Step 7: Saving Data as JSON

Purpose: Save the processed VCF data in a JSON format for ease of use in downstream applications.

##### Step 8: Load Data from JSON File

Purpose: Load and possibly further process data from a previously saved JSON file.

##### Step 9: Finding Variant

Purpose: Identify and extract specific genetic variants from the processed data.

### Contributing

Contributions to improve the functionality or efficiency of the code are welcome. Please follow the standard GitHub pull request process.

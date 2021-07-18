# DNA Analyser

## Introduction

Write Python code to generate a report on the statistical occurrences of various amino acids in a given string.

Your job is to complete the missing pieces and update the code wherever necessary to make all the unit tests work.

## Prerequisites

Completion of this task requires the use of `Python 3`.

## Task Details

Note: Please do *NOT* modify any tests unless specifically told to do so.

### Part 1

Implement the `clean_strands` method in `app.dna_analyser.DNAAnalyser` class.

It should read the DNA strands from a given file (`filename` argument) in which every line represents a single strand.

The method should return the list of valid strands *only*. A strand is valid when:

1. its length is greater than 10,
2. its length is less than 100,
3. it contains only `A`, `T`,`G` and `C` characters,
4. it's not an empty string,
5. all characters are in uppercase.

When the number of clean strands is less than 3, the method should return an empty list.

### Part 2

Implement the `create_strands` method in `app.dna_analyser.DNAAnalyser` class.

This method receives a list of clean strands, computed by the `clean_strands` method. Using this list, it should find overlapping elements and build one long strand which should be returned as a string.

Two strands overlap when last 3 characters of the first one match exactly 3 first characters of the second strand.

The following rules should be used for building the resulting string.

1. All input strands must overlap.
2. When two strands overlap they should be merged, e.g. `AAACCCAATTT` and `TTTACACAGCT` should be merged to `AAACCCAATTTACACAGCT` - the overlapping part should not be repeated.
3. One strand must overlap with another one only by the end of it - this is the starting strand.
4. One strand must overlap with another one only by the begging of it - this is the ending strand.
5. All other strands must overlap on both ends.

Please note, the starting and ending strands can be anywhere in the received list.

#### Example

For the following input list

```
[AGTGGGGGGGGG, AAACCCAATTT, TTTACACAGCT, GCTGGGCCCAGT]
```

the method should return

```
AAACCCAATTTACACAGCTGGGCCCAGTGGGGGGGGG
```

where the strands would be matched and merged as shown below.

```
AAACCCAA[TTT] -> [TTT]ACACA[GCT] -> [GCT]GGGCCC[AGT] -> [AGT]GGGGGGGGG
```

### Part 3

The last part of this task is to actually generate the report. Please implement the `get_amino_acids_report` method in the `app.dna_analyser.DNAAnalyser` class.

This method should split the `dna_sequence` argument into 3-characters long substrings. Each substring is a codon specifying an amino acid. Based on the data from the `codon.tsv` file count amino acids occurrences in the given sequence.

The method should return a dictionary with amino acids as keys and their count as values.

#### Example

For sequence `AAATTTGGGAAA` and `codon.tsv` file with following content:

```
AAA    Lysine
GGG    Glycine
TTT    Phenylalanine
```

This method should return a dictionary like the one below.

```
{
	'Lysine': 2 ,
	'Phenylalanine': 1 ,
	'Glycine': 1
}
```

## Hints

You shouldn't modify the unit tests.

To execute the unit tests, use:

```
pip install -q -e . && python3 setup.py pytest
```

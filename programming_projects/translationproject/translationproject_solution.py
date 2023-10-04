

codon_map = {'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L', 'TCT': 'S',
             'TCC': 'S', 'TCA': 'S', 'TCG': 'S', 'TAT': 'Y', 'TAC': 'Y',
             'TAA': '*', 'TAG': '*', 'TGT': 'C', 'TGC': 'C', 'TGA': '*',
             'TGG': 'W', 'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
             'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P', 'CAT': 'H',
             'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q', 'CGT': 'R', 'CGC': 'R',
             'CGA': 'R', 'CGG': 'R', 'ATT': 'I', 'ATC': 'I', 'ATA': 'I',
             'ATG': 'M', 'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
             'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K', 'AGT': 'S',
             'AGC': 'S', 'AGA': 'R', 'AGG': 'R', 'GTT': 'V', 'GTC': 'V',
             'GTA': 'V', 'GTG': 'V', 'GCT': 'A', 'GCC': 'A', 'GCA': 'A',
             'GCG': 'A', 'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
             'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'}

# Write your functions below


def translate_codon(x):
    # turn into upper case:
    codon = x.upper()
    # check if the codon is in the amino acid dictionary:
    if codon in codon_map:
        # return the aminoacid by looking up in the dictionary:
        return codon_map[codon]
    else:
        # return '?' if we could not translate the codon:
        return '?'


def split_codons(orf):
    # define a list for the results to be returned from the function:
    result = []
    # loop over a list of indexes generated by range.
    # from 0 to, but not including, len(orf), in jumps of 3
    for i in range(0, len(orf), 3):
        result.append(orf[i:i+3])
    return result


def translate_orf(orf):
    # split orf into codons:
    codons = split_codons(orf)
    # define a string of amino acids to add to:
    aaString = ''
    # loop over the codons:
    for codon in codons:
        # translate the codon and add it to the growing amino acid string:
        aaString += translate_codon(codon)
    # return the string:
    return aaString



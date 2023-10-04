
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

start_codon = 'ATG'

stop_codons = ['TAG', 'TGA', 'TAA']


def find_start_positions(seq):
    # uppercase seq
    seq = seq.upper()
    # define a list for the results
    result = []
    # loop over all indexes of seq unless the last two (where codons can not start):
    for i in range(len(seq)-2):
        # check if the codon is the start codon (notice the slicing technique):
        if seq[i:i+3] == start_codon:
            # append the start codon position to the list:
            result.append(i)
    # return the list
    return result


def find_next_codon(seq, start, codon):
    # loop over a list of indexes generated by range.
    # from start to, but not including, len(seq), in jumps of 3    
    for i in range(start, len(seq)-2, 3):
        # check if the current position is the start codon we look for:
        if seq[i:i+3] == codon:
            # return the start position of thet codon - ending the function:
            return i
    # If we get this far it means that we did not find the codon we where looking for so
    # we return None. However, a function that does not explicitly return something
    # defaults to returning None. So it is not scrictly necessary
    return None


def find_next_stop_codon(seq, start):
    # uppercase the sequence:
    seq = seq.upper()
    # define a list for temporary restults:
    results = []
    # loop over the different stop codons:
    for stop_codon in stop_codons:
        # find the start position of the next stop codon:
        pos = find_next_codon(seq, start, stop_codon)
        # check that pos is not None, which would indicate that the codon was not found:
        if pos != None:
            # append the start position of the codon to the list of temporary retults.
            results.append(pos)
    if len(results) > 0:
        # if we found the position of one or more stop codons we return the smallest (closet) one:
        return min(results)
    else:
        # if we did not find any stop codons we return None
        return None


def find_orfs(seq):
    # define a list to add results to:
    result = []
    # loop over the list of start positions returned by findStartPositions:
    for start_position in find_start_positions(seq):
        # get the stop position for each start position:
        stop_position = find_next_stop_codon(seq, start_position)
        # check that we actually found a stop positions:
        if stop_position != None:
            # append a tuple with start and stop positiosn to the list:
            result.append( [start_position, stop_position] )
    # return the list:
    return result


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
    # make sure the sequence length is a multiple of three:
    assert not len(orf) % 3
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


def read_genome(file_name):
    f = open(file_name, 'r')
    lines = f.readlines()
    header = lines.pop(0) 
    substrings = []
    for line in lines:
        substrings.append(line.strip())
    genome = ''.join(substrings)
    f.close()
    return genome

# def read_sequences(file_name):
#     f = open(file_name, 'r')
#     sequences = []
#     for line in f:
#         seq = line.strip()
#         sequences.append(seq)
#     f.close()
#     return sequences

def find_candidate_proteins(seq):
    # uppercase seq:
    seq = seq.upper()
    # define a list to add results to:
    result = []
    # loop over the list of start, stop tuples returned from findOpenReadingFrames:
    for start, stop in find_orfs(seq):
        # slice out the appropriate part of the sequence:
        orf = seq[start:stop+3]
        # append a translation fo the org to the list of results:
        result.append(translate_orf(orf))
    # return the list:
    return result

genome = read_genome('e_coli_O157_H157_str_Sakai.fasta')

print(find_candidate_proteins(genome[:1000]))


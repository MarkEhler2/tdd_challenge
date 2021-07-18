import collections.Counter
import r

class DNAAnalyser:

    REPORT_MAPPING_FILENAME = "codon.tsv"

    def __init__(self):
        pass

    @staticmethod
    def clean_strands(filename):
        """
        TODO(Part 1): Complete this method
        """
        cleaned_list = []
        processing = []
        dropped = []
        valid_chars = ['G','A','T','C']
        for item in filename:
            item = item.upper()
            processing.append(item)

        for item in processing:
            if (len(item) > 10) & (len(item) < 100):
                dropped.append(item)

        for item in dropped:
            filtered = filter(valid_chars.__contains__, item)
            cleaned_list.append(filtered)

        if len(cleaned_list) < 3:
            cleaned_list = []

        return cleaned_list

    def create_strands(self, cleaned_list):
        """
        TODO(Part 2): Complete this method
        """
        tails = []
        heads = []
        for item in cleaned_list:
            tails.append = item[:-3]
            heads.append = item[:2]
        # head_tail = zipped tuple of heads and tails for indexing

        # the idea should be to create a matrix of matches and join the matches in sequential order
        # find strand that match on the tail only
        matches = []
        for i, tail in enumerate(tails):
            for j, head in enumerate(heads):
                if tail == head:
                    matches.append([j,i])
        for j, head in enumerate(tails):
            for i, tail in enumerate(heads):
                if head == tail:
                    matches.append([j,i])

        # matches should return and index list of  x2 the length of input items from cleaned list
        # two items will have only one occurance [j,] takes postion 0 [,i] takes position -1
        ocurrances = counter(matches)
        middle = matches
        for i,item in enumerate(matches):
            if (ocurrances[i] == 1) & (item[0] not in [x[0] for i, x in enumerate(matches) if i != item]):
                head = item
                middle = [x for i, x in enumerate(matches) if i !=  item]
            if (ocurrances[i] == 1) & (item[1] not in [x[1] for i, x in enumerate(matches) if i != item]):
                tail = item
                middle = [x for i, x in enumerate(matches) if i != item]

        for item in matches
        results

        result = results.join('')
        return result

    def get_amino_acids_report(self, dna_sequence):
        """
        TODO(Part 3): Complete this method
        """
        strings = {'AAA' : 'Lysine',
        'GGG' : 'Glycine',
        'TTT' : 'Phenylalanine',
        'CCC' : 'Cytosine',
        }

        report = {'Lysine' : 0,
        'Glycine' : 0,
        'Phenylalanine' : 0,
        'Cytosine' : 0}


        for pattern in strings.keys():
            ls = re.findall(pattern, dna_sequence)
            report[pattern] = len(ls)

        return report

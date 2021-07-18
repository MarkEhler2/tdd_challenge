import pytest

from app.dna_analyser import DNAAnalyser


class TestCreateStrands:
    """Create Strands testing class"""

    def test_valid_sequence_in_sequence(self):
        """Test valid sequence"""
        seq = ["AAACCCAATTT", "TTTACACAGCT", "GCTGGGCCCAGT", "AGTGGGGGGGGG"]
        dna_analyser = DNAAnalyser()
        result = dna_analyser.create_strands(seq)
        assert result == "AAACCCAATTTACACAGCTGGGCCCAGTGGGGGGGGG"

    def test_valid_sequence_out_of_seq(self):
        """Test valid sequance - out of sequence"""
        seq = ["TTTACACAGCT", "GCTGGGCCCAGT", "AGTGGGGGGGGG", "AAACCCAATTT"]
        dna_analyser = DNAAnalyser()
        result = dna_analyser.create_strands(seq)
        assert result == "AAACCCAATTTACACAGCTGGGCCCAGTGGGGGGGGG"

    def test_invalid_first_value(self):
        """Test invalid first value"""
        seq = ["TTTACACAGCT", "GCTGGGCCCAGT", "AGTGGGGGGAAA", "AAACCCAATTT"]
        dna_analyser = DNAAnalyser()
        result = dna_analyser.create_strands(seq)
        assert result == ""

import pytest

class TestCleanStrands:
    """Clean Strands testing class"""

    FILE1 = "input1.txt"
    FILE2 = "input2.txt"
    FILE3 = "input3.txt"
    FILE4 = "input4.txt"

    @classmethod
    def write_file(cls, filename, lines):
        """File writing method"""
        with open(filename, "w") as _file:
            for line in lines:
                _file.write(line + "\n")

    @classmethod
    def setup_class(cls):
        """set up - before tests"""
        cls.write_file(cls.FILE1, ["A", "BCCC", "CD"])
        cls.write_file(cls.FILE2, ["GGGAAAATCCC", "CCCAATTT"])
        cls.write_file(cls.FILE3, ["GGGAAAA", "AAAATTTGG", "RETERAS"])
        cls.write_file(
            cls.FILE4,
            [
                "NEWDNASEQUENCE",
                "CCCCTTTGAGAGA",
                "AGATCTCTCTC",
                "TGATGCATCCCGGA",
                "GGAAAATCCCC",
                "RRASDLKJASDLKLAJ",
                "CC",
                "A",
                "CTCTATATATATA",
            ],
        )

    @classmethod
    def teardown_class(cls):
        """Tear down - after tests"""
        os.remove(cls.FILE1)
        os.remove(cls.FILE2)
        os.remove(cls.FILE3)
        os.remove(cls.FILE4)

    def test_invalid_length(self):
        """Test for invalid length"""
        dna_analyser = DNAAnalyser()
        result = dna_analyser.clean_strands(self.FILE1)
        assert len(result) == 0

    def test_invalid_two_value_result(self):
        """Test for invalid result len"""
        dna_analyser = DNAAnalyser()
        result = dna_analyser.clean_strands(self.FILE2)
        assert len(result) == 0

    def test_invalid_characters(self):
        """Test for invalid characters"""
        dna_analyser = DNAAnalyser()
        result = dna_analyser.clean_strands(self.FILE3)
        assert len(result) == 0

    def test_correct_file(self):
        """Test with correct input file"""
        dna_analyser = DNAAnalyser()
        result = dna_analyser.clean_strands(self.FILE4)
        assert len(result) == 5

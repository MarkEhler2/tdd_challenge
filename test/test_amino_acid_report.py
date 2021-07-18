import pytest

from app.dna_analyser import DNAAnalyser


class TestReport:
    """Amino Acid Strands Report testing class"""

    def test_codon_mapping(self):
        """Test codon mapping"""
        dna_analyser = DNAAnalyser()
        result = dna_analyser.get_amino_acids_report(
            "AAACCCAATTTTTTACACAGCTGCTGGGCCCAGT"
        )
        assert result.get("Proline") == 1

    def test_codon_mapping_wrong_result(self):
        """Test codon mapping with wrong result"""
        dna_analyser = DNAAnalyser()
        result = dna_analyser.get_amino_acids_report("AAACCCAATTTTTT")
        assert "Opal" not in result

    def test_codon_mapping_new_values(self):
        """Test codon mapping with new values"""
        dna_analyser = DNAAnalyser()
        result = dna_analyser.get_amino_acids_report(
            "CTAGATCGTATCGGTTACTGTGGGGAAACCTGCATGCATGCATG"
        )
        assert result.get("Glycine") == 2

    def test_amino_length(self):
        """Test report length"""
        dna_analyser = DNAAnalyser()
        result = dna_analyser.get_amino_acids_report(
            "CTAGATCGTATCGGTTACTGTGGGGAAACCTGCATGCATGCATG"
        )
        assert len(result.keys()) == 12

class IntronicVariant:
    _MAX_POSITION = 1000000 # Internal attribute which does not belong to the public class interface, and can be subject to change without notice
    _MAX_ALLELE_LENGTH = 50
    def __init__(self, chrom, position, ref, alt):
        self.chrom, self.position, self.ref, self.alt = chrom, position, ref, alt
    @classmethod
    def from_str(cls, variantstr):
        chrom, position, ref, alt = variantstr.split(":")
        return cls(chrom, int(position), ref, alt)
    # _is_valid(): check if the variant attributes are within valid ranges
    def _is_valid(self):
        return (0 < self._position <= IntronicVariant._MAX_POSITION) and \
               (1 <= len(self._ref) <= IntronicVariant._MAX_ALLELE_LENGTH) and \
               (1 <= len(self._alt) <= IntronicVariant._MAX_ALLELE_LENGTH)

variant1 = IntronicVariant("chr1", 500000, "A", "T")
print(variant1._is_valid()) # True

variant2 = IntronicVariant("chr2", 1500000, "CAG", "G")
print(variant2._is_valid()) # False 

variant3 = IntronicVariant("chr3", 800000, "G", "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG")
print(variant3._is_valid()) # False

s = "GCCAATGTATCAATGTACGGTCAATGTAGCCAGCAATGTATACCAGCAATGTAACTGCCTGCAATGTAATGTCCAATGTACAGCAATGTAGTCGTGCAATGTACACATGCACGCCTCAATGTATCCAAGATACAATGTAACAATGTACCAATGTACAATGTATCAATGTAGCAATGTATTACAATGTAAGCGCAATGTATCAATGTACAATGTACAATGTATCATGTCTACAATGTATCAATGTATCAATGTAGCTCTCAATGTACAATGTACAATGTAGGCAATGTAATGTATGAGACAATGTACAATGTACAATGTATCAATGTACAATGTAAGAGGAAGCAATGTACCAATGTAAAGACAATGTACCAATGTACAATGTAGCAATGTAGGGACAATGTATCAATGTACAATGTACAATGTACAATGTACATCAATGTATAGTCACAATGTATCAATGTAGCTTACAATGTACCAATGTACAATGTAAATTTACAATGTAACAATGTATATCGCCACAATGTACAATGTACAATGTACCGGACAATGTACAATGTACGCCAATGTATCAATGTACAATGTACCGTGAAGGCATCAATGTAGTGGTCAATGTACAATGTAGGCAATGTAATGCAATGTAGGTTTCAATGTATCAATGTAAGTGCAATGTACAATGTACAATGTATGGCCAATGTACAATGTACAATGTACCAATGTATCAATGTACAATGTACCACAATGTATTCAATGTATAGCATCAATGTAGCAATGTACAATGTAGGACAATGTAGGTTATCAATGTAATGCAATGTAACAATGTAGGCACAATGTACAATGTACAATGTAACAATGTAATCAATGTACAATGTACGGCTGCAATGTAACCCAATGTAATCCGTTCAATGTATG"
t = "CAATGTACA"

positions = []

for i in range(len(s)):
    text = s[i:i+9]
    if text == t:
        positions.append(i+1)

for i in positions:
    print(i, end = " ")
seq = "ATGCGT"
seq = seq.upper()

if seq == "":
    print("Invalid: empty sequence")
elif set(seq).issubset({"A", "T", "G", "C"}):
    print(seq, "is a valid DNA sequence")
else:
    print(seq, "is invalid. Bad symbols:", set(seq) - {"A", "T", "G", "C"})


seq = "AUGCGU"
seq = seq.upper()

if seq == "":
    print("Empty sequence")
elif "T" in seq and "U" in seq:
    print("Invalid: has both T and U")
elif set(seq).issubset({"A", "T", "G", "C"}) and "T" in seq:
    print(seq, "is DNA")
elif set(seq).issubset({"A", "U", "G", "C"}) and "U" in seq:
    print(seq, "is RNA")
elif set(seq).issubset({"A", "G", "C"}):
    print(seq, "could be DNA or RNA (no T or U)")
else:
    print(seq, "is invalid")




seq = "ATGCGTACGGTATCCG"

print("Length:", len(seq))
print("A:", seq.count("A"))
print("T:", seq.count("T"))
print("G:", seq.count("G"))
print("C:", seq.count("C"))




seq = "ATGCGTACGGTATCCG"

g = seq.count("G")
c = seq.count("C")
gc = (g + c) / len(seq) * 100

print("Length:", len(seq))
print("G + C:", g + c)
print(f"GC content: {gc:.2f}%")



seq = "GAATTC"
comp = {"A": "T", "T": "A", "G": "C", "C": "G"}

complement = ""
for base in seq:
    complement = complement + comp[base]

rev_comp = complement[::-1]

print("Original:", seq)
print("Complement:", complement)
print("Reverse complement:", rev_comp)

if seq == rev_comp:
    print("It is a palindrome")
else:
    print("Not a palindrome")
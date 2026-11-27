# #Activity 01
# print ("Name: Mohana Prabath Reg_No : 2020ICTS21")
# print ("course code: TICT4272 course titile : Applied Bio-informatics")
# print ("name of a biological organism: Oryza sativa")
# print ("Common name: Rice")
# print("Short description:Bioinformatics is the application of computational methods and tools to collect, store, analyse, and interpret biological data, especially DNA, RNA, and protein sequences.")

# #Exersize 01
# sampleID= "BIO-2026-001"
# organism= "Oryza sativa (Rice)"
# SampleType="Leaf Tissue"
# Collection_Date="15 October 2026"
# Location="Vavuniya, Sri Lanka"
# Research_Project="Rice Genetic Diversity Analysis"
# CollectedBy="Research Assistant"
# StorageCondition=-"20 degrees Celsius"

# print("SampleID: ",sampleID)
# print("organism: ",organism)
# print("SampleType: ",SampleType)
# print("Collection_Date: ",Collection_Date)
# print("Location: ",Location)
# print("Research_Project: ",Research_Project)
# print("CollectedBy: ",CollectedBy)
# print("StorageCondition: ",StorageCondition)




# #activity 04
# organism_name = "Homo sapiens"
# chromosome_number = 46
# dna_sequence_length = 1200
# gc_content = 42.5
# is_coding = True

# print("organism_name: ",organism_name)
# print("chromosome_number: ",chromosome_number)
# print("dna_sequence_length: ",dna_sequence_length)
# print("gc_content: ",gc_content)
# print("is_coding: ",is_coding)

# #activity 5
# length=2400
# number_of_fregments=6
# maximum_fregment_length=500

# average_fregment_length=length/number_of_fregments
# number_of_comlete_codons=length//3
# number_of_remainng_codons=length%3

# requred_fregment=(length+maximum_fregment_length-1)//maximum_fregment_length
# print("average_fregment_length: ",average_fregment_length)
# print("number_of_comlete_codons",number_of_comlete_codons)
# print("number_of_remainng_codons: ",number_of_remainng_codons)
# print("requred_fregment: ",requred_fregment)



# #activity 5

# dna_sequence_length=int(input("Enter the DNA sequence length: "))
# gc_percentage=int(input("Enter the GC percentage: "))

# GC_bases=dna_sequence_length*(gc_percentage/100)
# AT_bases=dna_sequence_length-GC_bases

# print("Number of GC bases:",GC_bases)
# print("Number of AT bases:",AT_bases)

# sequenc_length=2400
# num_of_fregment=int(input("Enter the number of fragments:"))
# maximum_fregment_length=int(input("Enter the maximum fragment length:"))

# avg_fregment_length=sequenc_length/num_of_fregment
# number_of_complete_codons= sequenc_length//3
# num_of_remining=sequenc_length%3
# requred_fregment=(sequenc_length+maximum_fregment_length-1)/maximum_fregment_length

# print("Average fragment length:",avg_fregment_length)
# print("Number of complete codons:",number_of_complete_codons)
# print("Remaining nucleotides:",num_of_remining)
# print("Minimum number of fragments required:",requred_fregment)

#Activity 07
# dna_sequence_length=int(input("Enter the DNA sequence length:"))
# number_of_complete_codons=dna_sequence_length//3
# remaing_nucleotities=dna_sequence_length%3
# percentage_complete_codons=((number_of_complete_codons*3)/dna_sequence_length)*100

# print("number_of_complete_codons:",number_of_complete_codons)
# print("remaing_nucleotities:",remaing_nucleotities)
# print("percentage_complete_codons",percentage_complete_codons)
# print("Divisible by 3:",bool(remaing_nucleotities==0))

#Activity 08
# sequence="ATGCGTACCGTAAGCT"
# print("DNA Sequence:",sequence)
# print("Sequence Length:",len(sequence))
# print("First Nucleotide:",sequence[0])
# print("Last Nucleotide:",sequence[-1])
# print("First Six Nucleotides:",sequence[0:6])
# print("Nucleotides from Position 4 to 10:",sequence[4:10])
# print("Reversed Sequence:",sequence[::-1])



#Activity 09
dna_sequence=" atgcgttacgtaatgc "
gene_names="TP53,BRCA1,EGFR,MYC"
#1
clean_dna_sequence=dna_sequence.strip()
convert_sequence=clean_dna_sequence.upper()
print("Clean_DNA sequence:",clean_dna_sequence)
print("Uppercase: ",convert_sequence)
#2
print("Calculate the length: ",len(convert_sequence))
print("first and last five nucleotride: ",)
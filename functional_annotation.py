from Bio.Blast import NCBIXML
with open ("project_blast.xml") as b:
   blast_record = NCBIXML.read(b)

print(len(blast_record.alignments))

first_alignment = blast_record.alignments[0]
print(first_alignment.title)
print(first_alignment.length) 

for a in blast_record.alignments:
   print(a.title)

print(len(first_alignment.hsps))

first_hsp = first_alignment.hsps[0]
print(first_hsp.score)
print(first_hsp.expect)

print("Query sequence")
print(first_hsp.query)

print("Matched seq")
print(first_hsp.match)

print("Alignment seq")
print(first_hsp.match)



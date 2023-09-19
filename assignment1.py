#open or read file
#create a new empty column
#for loop 
# create variable takes position - position, put number in new column


#import csv

#list comprehension chapter skapar lists med for loop 
import csv

with open('brca_cnvs_tcga-1.csv', newline='') as f:
    reader = csv.reader(f)
    header = next(reader)
    header.append("seq_length")
    row_list = []
    for row in reader:
        x=int(row[2])
        y=int(row[3])
        z=(y-x)
        r = row
        r.append(z)
        row_list.append(r)
    
with open('new_file.csv', 'w', newline='') as nf:
    writer = csv.writer(nf)
    writer.writerow(header)
    writer.writerows(row_list)

import csv
def my_func(filename, new_filename):
#open and read the csv file 
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        header = next(reader) #assigns the first row in the file to the header variable
        header.append("seq_length") #adds seq_length to header
        row_list = [] #creates an empty list 
        for row in reader: #iterates over the rows in the file, except the first
            x=int(row[2]) #assigns the third value of the row to x and makes it an integer
            y=int(row[3]) #assigns the fourth value of the row to y and makes it an integer
            z=(y-x) #calculates the sequence length
            r = row #assigns the list in each row to variable r
            r.append(z) #adds the seq length to the list r
            row_list.append(r) #adds the list r to row_list, creating a list of lists
        
    with open(new_filename, 'w', newline='') as nf: #creates a new csv file
        writer = csv.writer(nf)
        writer.writerow(header) #adds the header
        writer.writerows(row_list) #adds rows from row_list

#my_func('brca_cnvs_tcga-1.csv','new_file.csv') #example of input to the function
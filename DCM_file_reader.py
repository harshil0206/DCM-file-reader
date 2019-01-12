import pydicom                          #importing pydicom package to read dcm files

print("\nfor file name ttfm.dcm\n")

ttfm_data = pydicom.read_file("ttfm.dcm")    #reading the data from the ttfm.dcm file

print(ttfm_data)                             #printing data from the ttfm.dcm file

a = str(ttfm_data)                          #converting the data elements to string to write in the file

f = open("digisoft_ttfm.txt","w+")           #creating a file named digisoft

for i in a:                            #writing the data of the ttfm.dcm file into the digisoft.txt file
    f.writelines(a)

print("\nfor file name bmode.dcm\n")

bmode_data = pydicom.read_file("bmode.dcm")    #reading the data from the ttfm.dcm file

print(bmode_data)                             #printing data from the bmode.dcm file

b = str(bmode_data)                          #converting the data elements to string to write in the file

f = open("digisoft_bmode.txt","w+")           #creating a file named digisoft

for i in b:                            #writing the data of the ttfm.dcm file into the digisoft.txt file
    f.writelines(b)
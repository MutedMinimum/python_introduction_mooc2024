#Sometimes it is necessary to clear the contents of an existing file. 
#Opening the file in write mode and closing the file immediately will achieve just this:


#with open("clearing_deleting_files.txt", "w") as my_file:
#    pass                                                    #python erlaubt keinen leeren Block, deswegen pass



#ALTERNATIV
#open("clearing_deleting_files.txt", "w").close()



import os

#os.remove("clearing_deleting_files.txt")
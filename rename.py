
import os #need this to work with files
import datetime #this module allows us to reformat the date. read more at: https://docs.python.org/3/library/datetime.html

print(os.listdir()) #os.listdir() returns a list of the files in the current directory

for statement in os.listdir():
    if statement.endswith(".pdf"): #this makes sure i am only renaming the statements and not this file itself!
        basename = statement.replace(".pdf", "") #remove the file extension
        old_date = basename.replace("Statement_", "") #remove the first bit of filename e.g. Statement_25Apr2021 becomes 25Apr2021
        new_date = datetime.datetime.strptime(old_date, "%d%b%Y") #reading the date and creating a date object from that string
        new_statement = new_date.strftime("%Y-%m-%d") + ".pdf" #constructs new filenames in format YYYY-MM-DD and puts file extension back on
        print(statement, ">", new_statement) 
        os.rename(statement, new_statement) #rename the files



    

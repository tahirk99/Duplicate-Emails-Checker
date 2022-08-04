import time
import os
import pandas as pd

cwd = os.getcwd()
print(f"Current Working Directory: {cwd}")
sib_input = input("Enter Path of main list having all the emails ;make sure you remove quotes from both the sides of file path: ")
target_input = input("Enter Path of Target list within which you want to search for duplicates ;make sure you remove quotes from both the sides of file path: ")

start = time.time()
try:
    sib_list = pd.read_csv(sib_input)
    to_validate = pd.read_csv(target_input)
except Exception as e:
    print(f"Error: {e}\n1. Please give accurate filepath \n2. Check file extension it should be .csv")
    exit()

try:
    sib_emails = sib_list["EMAIL"]
    to_verify = to_validate["EMAIL"]
    duplicates = []
except Exception as e:
    print("Error: 'EMAIL' column is missing, misspelled. Please check & keep column name as EMAIL with all caps")
    exit()

def check_duplicates():
    for i in sib_emails:
        for j in to_verify:
            if j == i:
                duplicates.append(j)

#dups = [i for i in sib_emails j for j in to_verify if i == j]

def export_duplicates():
    export = pd.Series(duplicates)
    export.to_csv(r"".join([cwd, "\Duplicates.csv"]), index=False)

print("Processing...")
check_duplicates()
export_duplicates()

end = time.time()
time_took = end-start
print(f"Time took to exexute program: {time_took:.2f} Seconds")

import pandas as pd
import re
import os
import glob

def remove_spaces(sheet_name):
    # Load the CSV file
    #sheet_name = "toBatch - ENIB"
    file_path = "to-Batch-final/"+sheet_name # Replace with your actual file path
    data = pd.read_csv(file_path)

    # Capitalize the first letter of each word in Variable1
    data['Variable1'] = data['Variable1'].str.title()

    # Remove spaces around underscores and backslashes in @Variable2
    #data['@Variable2'] = data['@Variable2'].apply(lambda x: re.sub(r'\s*([_\\])\s*', r'\1', x))
    data['Variable2'] = data['Variable2'].str.title()
    # Save the modified data back to a new CSV file
    output_path = "sheets-mod/mod-"+sheet_name  # Replace with your desired output file name
    data.to_csv(output_path, index=False)

    print(f"Updated file saved to {output_path}")

sheet_names_list=[]
#folder_path

    # Specify the folder containing the CSV files
folder_path = "to-batch-final"  # Replace with the actual folder path

# Get all CSV files in the folder
csv_files = glob.glob(os.path.join(folder_path, "*.csv"))

# Extract just the file names (without the folder path)
#csv_file_names = [os.path.basename(file) for file in csv_files]
csv_file_names= ["OC Badges  - to-automate.csv"]
print("CSV File Names:", csv_file_names)

for i in csv_file_names:
    print("removing spcaes for:",i)
    remove_spaces(i)
    




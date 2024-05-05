import os
import re

def replace_date_with_title(directory):
    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        # Check if the file is a .tex file
        if filename.endswith(".tex"):
            file_path = os.path.join(directory, filename)
            # Read the content of the file
            with open(file_path, 'r') as file:
                content = file.read()
            # Replace \date with \title
            new_content = content.replace("\\date", "\\title")
            # Write the modified content back to the file
            with open(file_path, 'w') as file:
                file.write(new_content)

def find_and_replace(directory, environment):
    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        # Check if the file is a .tex file
        if filename.endswith(".tex"):
            file_path = os.path.join(directory, filename)
            # Read the content of the file
            with open(file_path, 'r') as file:
                content = file.read()
            # Find and replace the environment with the desired text
            new_content = content.replace("\\maketitle}", "\\maketitle")#.replace("\\end{" + environment + "}", "\\end{br}")
            # Write the modified content back to the file
            with open(file_path, 'w') as file:
                file.write(new_content)



find_and_replace('InClassProblems2024/','br')


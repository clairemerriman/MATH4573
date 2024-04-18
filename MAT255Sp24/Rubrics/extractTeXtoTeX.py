import os

# Input and output definitions at the beginning
input_file = '../../../Homework/HW7Sp24.tex'
section_name = 'Proofs and writing'  # Change this to the desired section name

# Use input file to name output file
start_pattern = 'HW'  # Start pattern to search for
end_pattern = 'Sp'  # End pattern to search for

# Find the indices of the start and end patterns
start_index = input_file.find(start_pattern) + len(start_pattern)
end_index = input_file.find(end_pattern, start_index)

# Extract the substring between the start and end patterns
document_string = input_file[start_index:end_index]

# Derive output file name from input XML file name
output_file = os.path.join('Rubrics','Homework' + document_string + '.tex')


def extract_section(input_file, section_name):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    section_found = False
    extracted_lines = []

    for line in lines:
        if section_found:
            if line.strip().startswith(r'\section') or line.strip().startswith(r'\section*'):
                break
            extracted_lines.append(line)
            # Add specific text after every instance of the example environment
            if r'\end{ex}' in line:
                extracted_lines.append(r'''
\begin{writeRubric}
    \item \textbf{Does not demonstrate understanding}
     Contains a reasonable attempt to prove each part, but does not meet the criteria for two points.
    \item \textbf{Needs revisions}
     
    \item \textbf{Demonstrates understanding}
    
    \item \textbf{Exemplary}
        
\end{writeRubric}
                                       ''')
        elif r'\section*{' + section_name in line:
            section_found = True
            extracted_lines.append(line)

    return ''.join(extracted_lines)

extracted_section = extract_section(input_file, section_name)

# Construct the complete LaTeX document with preamble and extracted section
output_content = r'''
\documentclass[letterpaper, 11pt]{ximera}
\input{rubricsPreamble.tex}

\StrBetween*[1,1]{\currfilename}{Homework}{.tex}[\homework]

\begin{document}

\chapter{Homework \#\homework\ Rubrics}

''' + extracted_section + r'''

\end{document}
'''


# Write the output to a file
with open(output_file, 'w') as f:
    f.write(output_content)

print(f"File '{output_file}' created with the section '{section_name}' from '{input_file}'.")

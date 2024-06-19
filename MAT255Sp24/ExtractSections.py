import re
import os

def extract_all_sections(input_file):

    # Use input file name to create the folder for the week
    filename = os.path.splitext(os.path.basename(input_file))[0]
    folder_name = filename.split('Sp')[0]

    # Create folder for output files
    os.makedirs(folder_name, exist_ok=True)
    with open(input_file, 'r') as f:
        lines = f.readlines()

    append_line = False
    extracted_lines = []

    for line in lines:
        if append_line:
            if line.startswith(r'\section') or line.startswith(r'\end{document}'):
                output_content = r'''\documentclass{ximera}
\input{../lessonplanheader.tex}

\title{''' + section_title + r'''}
\begin{document}
\begin{abstract}
\end{abstract}
\maketitle

''' + ''.join(extracted_lines) + r'''

\end{document}
'''
                #Now we use the content information from the section title to name the file
                #Remove spaces and special characters

                file_title = ''.join(letter for letter in section_title if letter.isalnum())

                output_file = os.path.join(folder_name, f"{file_title.strip()}.tex")

                with open(output_file, "w") as section_file:
                    section_file.write(output_content)
            
                # Reset variables to keep looping
                if line.startswith(r'\section'):
                    section_title = line.split(': ', 1)[1].split('}')[0]
                extracted_lines = []
            
            else:
                extracted_lines.append(line)
        elif line.startswith(r'\section') or line.startswith(r'\section*'):
            append_line = True
            #Get the Content Title that is after
            section_title = line.split(': ', 1)[1].split('}')[0]
            # extracted_lines.append(line)


sections = extract_all_sections('XimeraMAT255Sp24/Week13Spring24.tex')

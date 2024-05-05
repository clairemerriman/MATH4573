import os

def find_files(directory, extension):


    found_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith("." + extension):
                found_files.append(file)
    return found_files

def filter_files_by_date(directory, extension):
    found_files = find_files(directory, extension)
    filtered_files = []
    for file in found_files:
        file_name = os.path.splitext(os.path.basename(file))[0]  # Extract file name without extension
        # Find potential date part by splitting filename by underscore and taking the last part
        potential_date = file_name.split('_')[-1]
        # Remove file extension
        potential_date = potential_date.split('.')[0]
        month_map = {
            'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04',
            'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08',
            'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'
        }
        # Check if the potential date matches the MonDD format
        if potential_date[:3] in month_map and potential_date[3:].isdigit():
            # Extract month and day
            mon, day = potential_date[:3], potential_date[3:]
            # Convert month abbreviation to numerical value
            mm = month_map[mon]
            # Pad day with leading zero if necessary
            dd = day.zfill(2)
            # Get current year (you might need a different way to determine the year)
            current_year = '2024'  # For example, use the current year
            # Format the date as YYYYMMDD
            sortable_date = f"{current_year}{mm}{dd}"
            filtered_files.append((file, sortable_date))
    # Sort files by sortable date
    sorted_files = sorted(filtered_files, key=lambda x: x[1])
    return [file[0] for file in sorted_files]


def add_activities(directory, extension, template):
    filtered_files = filter_files_by_date(directory,extension)

    # Read the original content of the template file
    with open(template, 'r') as template_file:
        original_content = template_file.read()
    
    # Find the index of the marker where to insert the new content
    marker = '%% Here we have a listing of the activities.'

    # Find the index of the marker where to insert the new content
    marker_index = original_content.find(marker)
    
    if marker_index == -1:
        # Marker not found, append the new content at the end
        insertion_point = len(original_content)
    else:
        # Marker found, insert the new content after the marker
        insertion_point = marker_index + len(marker)
    
    # Construct the input statements for each file
    input_statements = [f"\n\\activity{{{filename}}}\n" for filename in filtered_files]
    
    # Construct the new content by inserting the input statements at the insertion point
    new_content = (original_content[:insertion_point] +
                   '\n'.join(input_statements) +
                   original_content[insertion_point:])
    
    # Write the combined content back to the template file
    with open(template, 'w') as template_file:
        template_file.write(new_content)


print(add_activities('XimeraInClass/','tex','XimeraInClass/AllInClass2024.tex'))


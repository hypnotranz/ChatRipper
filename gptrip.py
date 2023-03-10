import os
import re
import datetime

# Set the path to the directory containing the markdown files
directory_path = "."

# Get a list of all the markdown files in the directory
files = os.listdir(directory_path)

# Sort the files by creation date
files = sorted(files, key=lambda x: os.path.getctime(os.path.join(directory_path, x)))

# Loop through each file in the directory
for file in files:

    # Check if the file is a markdown file
    if file.endswith(".md"):

        # Set the path to the input file and output file
        input_file_path = os.path.join(directory_path, file)
        output_file_path = os.path.join(directory_path, datetime.datetime.fromtimestamp(os.path.getctime(input_file_path)).strftime('%Y-%m-%d') + ".chatgpt")

        # Open the markdown file for reading
        with open(input_file_path, 'r') as input_file:

            # Open a new file for writing the prompts
            with open(output_file_path, 'w') as output_file:

                # Loop through each line in the input file
                for line in input_file:

                    # If the line starts with ">" character, write it to the output file
                    if line.startswith(">"):
                        output_file.write(line)

import os
import re
import datetime
import logging

logging.basicConfig(filename='ripped.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
logging.getLogger('').addHandler(console)

directory_path = "./chatgpt"

output_directory_path = "./ripped"

files = os.listdir(directory_path)

files = sorted(files, key=lambda x: os.path.getctime(os.path.join(directory_path, x)))

for file in files:
    if file.endswith(".md"):
        input_file_path = os.path.join(directory_path, file)
        with open(input_file_path, 'r') as input_file:
            file_counter = 1
            prompt = ""
            prompts = []
            lists = []
            for line in input_file:
                if line.startswith(">"):
                    if lists:
                        output_file_path_lists = os.path.join("./ripped", os.path.splitext(file)[0] + f".{file_counter}.list")
                        with open(output_file_path_lists, 'w') as output_file_lists:
                            output_file_lists.write(prompt + "\n")
                            output_file_lists.write("\n".join(lists) + "\n\n")
                            logging.info("Found list: {}".format(prompt))
                            logging.info("\n".join(lists))
                        lists = []
                        file_counter += 1
                    prompt = line.strip()
                    prompts.append(prompt)
                    logging.info("Found prompt: {}".format(prompt))
                elif re.match(r"^\d+\.", line.strip()):
                    lists.append(line.strip())
            if prompts:
                output_file_path_prompts = os.path.join("./ripped", os.path.splitext(file)[0] + ".prompts")
                with open(output_file_path_prompts, 'w') as output_file_prompts:
                    output_file_prompts.write("\n".join(prompts) + "\n")

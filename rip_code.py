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
            code_blocks = []
            for line in input_file:
                if line.startswith(">"):
                    if code_blocks:
                        output_file_path_code = os.path.join("./ripped", os.path.splitext(file)[0] + f".{file_counter}.code")
                        with open(output_file_path_code, 'w') as output_file_code:
                            output_file_code.write(f"# Generated from prompt: {prompt}\n\n")
                            output_file_code.write("".join(code_blocks).strip("\n"))
                            logging.info("Found code block for: {}".format(prompt))
                        code_blocks = []
                        file_counter += 1
                    prompt = line.strip()
                    prompts.append(prompt)
                    logging.info("Found prompt: {}".format(prompt))
                elif line.startswith("```"):
                    if code_blocks:
                        output_file_path_code = os.path.join("./ripped", os.path.splitext(file)[0] + f".{file_counter}.code")
                        with open(output_file_path_code, 'w') as output_file_code:
                            output_file_code.write(f"# Generated from prompt: {prompt}\n\n")
                            output_file_code.write("".join(code_blocks).strip("\n"))
                            logging.info("Found code block for: {}".format(prompt))
                        code_blocks = []
                        file_counter += 1
                    else:
                        code_blocks.append("\n")
                elif code_blocks:
                    code_blocks.append(line)
            if prompts:
                output_file_path_prompts = os.path.join("./ripped", os.path.splitext(file)[0] + ".prompts")
                with open(output_file_path_prompts, 'w') as output_file_prompts:
                    output_file_prompts.write("\n".join(prompts) + "\n")

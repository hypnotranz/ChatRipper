import os
import shutil

# Create the chatgpt directory if it doesn't exist
if not os.path.exists("chatgpt"):
    os.makedirs("chatgpt")

# Get a list of all the markdown files in the current directory
files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith(".md")]

# Move each file to the chatgpt directory
for file in files:
    shutil.move(file, os.path.join("chatgpt", file))
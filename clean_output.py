import os
import logging


def clear_output_directory(directory_path):
    # Create the output directory if it doesn't exist
    output_directory_path = os.path.join(directory_path, "ripped")
    if not os.path.exists(output_directory_path):
        os.makedirs(output_directory_path)

    # Clear the output directory
    for filename in os.listdir(output_directory_path):
        file_path = os.path.join(output_directory_path, filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            logging.error("Failed to delete {}: {}".format(file_path, e))


clear_output_directory(".")
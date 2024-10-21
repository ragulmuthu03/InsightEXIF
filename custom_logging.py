# custom_logging.py

import logging
import os

def setup_logging():
    # Set up logging configuration
    log_path = 'metadata_extraction.log'
    logging.basicConfig(filename=log_path, level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
    return os.path.abspath(log_path)

def log_metadata(parent_folder_id, file_metadata, link_information, size_information, owner_information, sharing_information,
                 description_information, image_metadata, video_metadata):
    # Log output information
    logging.info(f"\nParent Folder ID: {parent_folder_id}")

    logging.info("\nFile Metadata:")
    for key, value in file_metadata.items():
        logging.info(f"  {key}: {value}")

    logging.info("\nLink information:")
    for key, value in link_information.items():
        logging.info(f"  {key}: {value}")

    logging.info("\nSize information:")
    for key, value in size_information.items():
        logging.info(f"  {key}: {value}")

    logging.info("\nOwner information:")
    for key, value in owner_information.items():
        logging.info(f"  {key}: {value}")

    logging.info("\nSharing information:")
    for key, value in sharing_information.items():
        if isinstance(value, list):
            logging.info(f"  {key}:")
            for item in value:
                logging.info(f"    {item}")
        else:
            logging.info(f"  {key}: {value}")

    # Log additional metadata information
    logging.info("\nDescription:")
    for key, value in description_information.items():
        logging.info(f"  {key}: {value}")

    logging.info("\nImage Metadata:")
    for key, value in image_metadata.items():
        logging.info(f"  {key}: {value}")

    logging.info("\nVideo Metadata:")
    for key, value in video_metadata.items():
        logging.info(f"  {key}: {value}")

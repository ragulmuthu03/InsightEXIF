# logging.py

import logging

def setup_logging():
    # Set up logging configuration
    logging.basicConfig(filename='metadata_extraction.log', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

def log_output(parent_folder_id, file_metadata, link_information, size_information, owner_information, sharing_information):
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

def log_additional_metadata(description, image_metadata, video_metadata):
    # Log additional metadata information
    logging.info("\nDescription:")
    for key, value in description.items():
        logging.info(f"  {key}: {value}")

    logging.info("\nImage Metadata:")
    for key, value in image_metadata.items():
        logging.info(f"  {key}: {value}")

    logging.info("\nVideo Metadata:")
    for key, value in video_metadata.items():
        logging.info(f"  {key}: {value}")

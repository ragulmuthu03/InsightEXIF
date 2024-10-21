# main.py

import os
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from additional_metadata import get_metadata, get_link_information, get_size_information, get_owner_information, \
    get_sharing_information, get_parents_information, get_description, get_image_metadata, get_video_metadata, get_created_time
from additional_metadata import get_parent_id
from custom_logging import setup_logging, log_metadata
from additional_metadata import get_modified_time, get_opened_time
from additional_metadata import get_exif_data, get_camera_make_and_model, get_capture_datetime, get_gps_location, get_exposure_time, get_aperture_value, get_iso_speed, get_flash_information, get_orientation

from googleapiclient.http import MediaIoBaseDownload
from io import BytesIO
import piexif

def authenticate():
    # Set up OAuth 2.0 credentials
    creds = None
    token_path = 'token.json'  # Replace with the path to your token file

    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path)

    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json',  # Replace with the path to your credentials file
            ['https://www.googleapis.com/auth/drive.metadata.readonly']
        )
        creds = flow.run_local_server(port=0)

        # Save the credentials for future use
        with open(token_path, 'w') as token_file:
            token_file.write(creds.to_json())

    return creds

def main():
    # Set up logging
    log_path = setup_logging()

    # Authenticate and get credentials
    creds = authenticate()
    file_id = input("Enter File ID: ")

    # Specify the file ID you want to retrieve metadata for
    #file_id = '1yHJ5JmZ7NgWXCnklBd-KacHFNKc_Q8rs'  # Replace with your file ID

    # Get the parent folder ID
    parent_id = get_parent_id(file_id, creds)
    if parent_id:
        print(f"\nParent Folder ID: {parent_id}")

    # Print extended metadata for the specified file within the parent folder
    metadata = get_metadata(file_id, creds)
    print("\nFile Metadata:")
    for key, value in metadata.items():
        print(f"  {key}: {value}")

    link_info = get_link_information(file_id, creds)
    print("\nLink information:")
    for key, value in link_info.items():
        print(f"  {key}: {value}")

    size_info = get_size_information(file_id, creds)
    print("\nSize information:")
    for key, value in size_info.items():
        print(f"  {key}: {value}")

    owner_info = get_owner_information(file_id, creds)
    print("\nOwner information:")
    for key, value in owner_info.items():
        print(f"  {key}: {value}")

    sharing_info = get_sharing_information(file_id, creds)
    print("\nSharing information:")
    for key, value in sharing_info.items():
        if isinstance(value, list):
            print(f"  {key}:")
            for item in value:
                print(f"    {item}")
        else:
            print(f"  {key}: {value}")

    parents_info = get_parents_information(file_id, creds)
    print("\nParent information:")
    for key, value in parents_info.items():
        if isinstance(value, list):
            print(f"  {key}:")
            for item in value:
                print(f"    {item}")
        else:
            print(f"  {key}: {value}")
            
    created_time = get_created_time(file_id, creds)
    #print(type(created_time))
    print(f"\nFile Created Time: {created_time}")
    
    # Get modified time for the specified file
    modified_time = get_modified_time(file_id, creds)
    print(f"\nFile Modified Time: {modified_time}")

    # Get opened time for the specified file
    opened_time = get_opened_time(file_id, creds)
    print(f"\nFile Opened Time: {opened_time}")

    description_info = get_description(file_id, creds)
    print("\nDescription:")
    for key, value in description_info.items():
        print(f"  {key}: {value}")

    image_metadata = get_image_metadata(file_id, creds)
    print("\nImage Metadata:")
    for key, value in image_metadata.items():
        print(f"  {key}: {value}")
        
    # Get Exif data using existing functions
    #exif_data = get_exif_data(file_id, creds)

    #if exif_data:
        # Use Exif functions to retrieve specific metadata
       # camera_make_and_model = get_camera_make_and_model(exif_data)
        #capture_datetime = get_capture_datetime(exif_data)
        #gps_location = get_gps_location(exif_data)
        #exposure_time = get_exposure_time(exif_data)
        #aperture_value = get_aperture_value(exif_data)
        #iso_speed = get_iso_speed(exif_data)
        #flash_info = get_flash_information(exif_data)
        #orientation = get_orientation(exif_data)

        # Print the retrieved metadata
        #print("\nExif Metadata:")
        #print(f"Camera Make and Model: {camera_make_and_model}")
        #print(f"Capture Datetime: {capture_datetime}")
        #print(f"GPS Location: {gps_location}")
        #print(f"Exposure Time: {exposure_time}")
        #print(f"Aperture Value: {aperture_value}")
        #print(f"ISO Speed: {iso_speed}")
        #print(f"Flash Information: {flash_info}")
        #print(f"Orientation: {orientation}")
    #else:
        #print("No Exif data found for the given file ID.")

    video_metadata = get_video_metadata(file_id, creds)
    print("\nVideo Metadata:")
    for key, value in video_metadata.items():
        print(f"  {key}: {value}")

    # Log metadata
    log_metadata(parent_id, metadata, link_info, size_info, owner_info, sharing_info,
                 description_info, image_metadata, video_metadata)

    print(f"\nLog files are stored at: {log_path}")

if __name__ == "__main__":
    main()

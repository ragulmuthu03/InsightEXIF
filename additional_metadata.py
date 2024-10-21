# additional_metadata_info.py
import os
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from googleapiclient.http import MediaIoBaseDownload
from io import BytesIO
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

def get_parent_id(file_id, creds):
    drive_service = build('drive', 'v3', credentials=creds)
    file_info = drive_service.files().get(fileId=file_id, fields='parents').execute()
    parents = file_info.get('parents', [])
    if parents:
        return parents[0]
    else:
        return None

def get_metadata(file_id, creds):
    # Build the service object
    drive_service = build('drive', 'v3', credentials=creds)

    # Get metadata for the file
    file_metadata = drive_service.files().get(fileId=file_id).execute()

    return file_metadata

# additional_metadata.py

def get_created_time(file_id, creds):
    # Build the service object
    drive_service = build('drive', 'v3', credentials=creds)

    # Get created time for the file
    file_info = drive_service.files().get(fileId=file_id, fields="createdTime").execute()
    created_time = file_info.get('createdTime', None)

    # Format the date and time with a space
    formatted_created_time = datetime.strptime(created_time, "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

    return formatted_created_time


# additional_metadata.py

def get_modified_time(file_id, creds):
    # Build the service object
    drive_service = build('drive', 'v3', credentials=creds)

    # Get modified time for the file
    file_info = drive_service.files().get(fileId=file_id, fields="modifiedTime").execute()
    modified_time = file_info.get('modifiedTime', None)

    # Format the date and time with a space
    formatted_modified_time = datetime.strptime(modified_time, "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

    return formatted_modified_time

def get_opened_time(file_id, creds):
    # Build the service object
    drive_service = build('drive', 'v3', credentials=creds)

    # Get opened time for the file
    file_info = drive_service.files().get(fileId=file_id, fields="viewedByMeTime").execute()
    opened_time = file_info.get('viewedByMeTime', None)
    # Format the date and time with a space
    formatted_opened_time = datetime.strptime(opened_time, "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    
    return formatted_opened_time


def get_version_information(file_id, creds):
    # Build the service object
    drive_service = build('drive', 'v3', credentials=creds)

    # Get version information for the file
    version_info = drive_service.files().get(fileId=file_id, fields="version").execute()

    return version_info

def get_link_information(file_id, creds):
    # Build the service object
    drive_service = build('drive', 'v3', credentials=creds)

    # Get link information for the file
    link_info = drive_service.files().get(fileId=file_id, fields="webViewLink").execute()

    return link_info

def get_size_information(file_id, creds):
    # Build the service object
    drive_service = build('drive', 'v3', credentials=creds)

    # Get size information for the file
    size_info = drive_service.files().get(fileId=file_id, fields="size").execute()

    return size_info

def get_owner_information(file_id, creds):
    # Build the service object
    drive_service = build('drive', 'v3', credentials=creds)

    # Get owner information for the file
    owner_info = drive_service.files().get(fileId=file_id, fields="owners").execute()

    return owner_info

def get_sharing_information(file_id, creds):
    # Build the service object
    drive_service = build('drive', 'v3', credentials=creds)

    # Get sharing information for the file
    sharing_info = drive_service.files().get(fileId=file_id, fields="shared,sharingUser").execute()

    return sharing_info

def get_parents_information(file_id, creds):
    # Build the service object
    drive_service = build('drive', 'v3', credentials=creds)

    # Get parents information for the file
    parents_info = drive_service.files().get(fileId=file_id, fields="parents").execute()
    
    return parents_info

def get_permissions_information(file_id, creds):
    # Build the service object
    drive_service = build('drive', 'v3', credentials=creds)

    # Get permissions information for the file
    permissions_info = drive_service.files().get(fileId=file_id, fields="permissions").execute()

    return permissions_info

def get_description(file_id, creds):
    # Build the service object
    drive_service = build('drive', 'v3', credentials=creds)

    # Get description for the file
    description_info = drive_service.files().get(fileId=file_id, fields="description").execute()

    return description_info

def get_image_metadata(file_id, creds):
    # Build the service object
    drive_service = build('drive', 'v3', credentials=creds)

    # Get image metadata for the file
    image_metadata = drive_service.files().get(fileId=file_id, fields="imageMediaMetadata").execute()

    return image_metadata

def get_exif_data(file_id, creds):
    service = build('drive', 'v3', credentials=creds)

    # Download the file content
    request = service.files().get_media(fileId=file_id)
    fh = BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        _, done = downloader.next_chunk()

    # Extract Exif data from the downloaded file content
    exif_data = extract_exif_data(fh.getvalue())
    return exif_data

def extract_exif_data(file_content):
    try:
        exif_dict = piexif.load(file_content)
        return exif_dict
    except Exception as e:
        print(f"Error extracting Exif data: {e}")
        return None


#def get_exif_data(image_path):
    """
#    Retrieve Exif data from an image file.
    """
#    try:
#        with Image.open(image_path) as img:
#            exif_data = img._getexif()
#        return exif_data
 #   except (AttributeError, IndexError, KeyError, OSError):
 #       return None

def get_camera_make_and_model(exif_data):
    """
    Retrieve the camera make and model from Exif data.
    """
    if exif_data:
        make = exif_data.get(271)  # Tag for Camera Make
        model = exif_data.get(272)  # Tag for Camera Model
        return f"{make} {model}" if make and model else None
    return None

def get_capture_datetime(exif_data):
    """
    Retrieve the date and time of image capture from Exif data.
    """
    if exif_data:
        datetime_original = exif_data.get(36867)  # Tag for DateTimeOriginal
        return datetime_original
    return None


def get_gps_location(exif_data):
    """
    Retrieve GPS location (latitude and longitude) from Exif data if available.
    """
    if exif_data:
        gps_info = exif_data.get(34853)  # Tag for GPSInfo
        if gps_info:
            lat_ref = gps_info.get(1)  # Tag for GPSLatitudeRef
            lon_ref = gps_info.get(3)  # Tag for GPSLongitudeRef
            lat = gps_info.get(2)  # Tag for GPSLatitude
            lon = gps_info.get(4)  # Tag for GPSLongitude

            if lat and lon:
                lat_deg = lat[0][0] / lat[0][1]
                lat_min = lat[1][0] / lat[1][1]
                lat_sec = lat[2][0] / lat[2][1]
                lat_decimal = lat_deg + (lat_min / 60.0) + (lat_sec / 3600.0)
                if lat_ref == 'S':
                    lat_decimal *= -1

                lon_deg = lon[0][0] / lon[0][1]
                lon_min = lon[1][0] / lon[1][1]
                lon_sec = lon[2][0] / lon[2][1]
                lon_decimal = lon_deg + (lon_min / 60.0) + (lon_sec / 3600.0)
                if lon_ref == 'W':
                    lon_decimal *= -1

                return lat_decimal, lon_decimal
    return None


def get_exposure_time(exif_data):
    """
    Retrieve exposure time from Exif data.
    """
    if exif_data:
        exposure_time = exif_data.get(33434)  # Tag for ExposureTime
        return exposure_time
    return None


def get_aperture_value(exif_data):
    """
    Retrieve aperture value from Exif data.
    """
    if exif_data:
        aperture_value = exif_data.get(33437)  # Tag for FNumber
        return aperture_value
    return None


def get_iso_speed(exif_data):
    """
    Retrieve ISO speed from Exif data.
    """
    if exif_data:
        iso_speed = exif_data.get(34855)  # Tag for ISOSpeedRatings
        return iso_speed
    return None


def get_flash_information(exif_data):
    """
    Retrieve flash information from Exif data.
    """
    if exif_data:
        flash = exif_data.get(37385)  # Tag for Flash
        return flash
    return None


def get_orientation(exif_data):
    """
    Retrieve image orientation information from Exif data.
    """
    if exif_data:
        orientation = exif_data.get(274)  # Tag for Orientation
        return orientation
    return None

def get_video_metadata(file_id, creds):
    # Build the service object
    drive_service = build('drive', 'v3', credentials=creds)

    # Get video metadata for the file
    video_metadata = drive_service.files().get(fileId=file_id, fields="videoMediaMetadata").execute()

    return video_metadata

def count_modifications(metadata):
    # Example: Count modifications based on modifiedTime presence
    return 1 if 'modifiedTime' in metadata else 0

def count_uploads(metadata):
    # Example: Count uploads based on the absence of parents (assuming new file)
    return 1 if 'parents' not in metadata else 0

def count_downloads(metadata):
    # Example: Count downloads based on the presence of parents (assuming existing file)
    return 1 if 'parents' in metadata else 0

def count_collaborators(metadata):
    # Example: Count collaborators based on the sharing information
    collaborators_count = 0
    sharing_info = metadata.get('sharing_info', {})
    
    if 'shared' in sharing_info:
        collaborators_count = len(sharing_info.get('sharingUser', []))
    
    return collaborators_count


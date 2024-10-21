import os
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from datetime import datetime


# Function to authenticate with Google Drive API
def authenticate():
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

        with open(token_path, 'w') as token_file:
            token_file.write(creds.to_json())

    return creds

# Function to get the last 4 modified dates and times
def get_last_modified_dates(file_id, creds):
    drive_service = build('drive', 'v3', credentials=creds)

    # Get the file metadata
    file_metadata = drive_service.files().get(fileId=file_id, fields='modifiedTime').execute()

    # Get the last 4 modified dates and times
    modified_dates = []
    for activity in drive_service.activities().list(
            source='drive.google.com',
            driveAncestorId=file_id,
            pageSize=4
    ).execute().get('activities', []):
        modified_dates.append(activity['combinedEvent']['eventTime'])

    return file_metadata['modifiedTime'], modified_dates

if __name__ == "__main__":
    # Authenticate and get credentials
    creds = authenticate()

    # Specify the file ID of the document you want to access
    file_id = '1th1Lzb86oIDq_KscrKPFLwY1I1nQyo5W'  # Replace with the actual file ID

    # Get metadata and last modified dates
    metadata, last_modified_dates = get_last_modified_dates(file_id, creds)

    # Print the results
    print(f"File ID: {file_id}")
    print(f"Created Time: {metadata['createdTime']}")
    print(f"Modified Time: {metadata['modifiedTime']}")
    print("Last 4 Modified Dates (with date and time):")
    for i, date_time in enumerate(last_modified_dates, start=1):
        print(f"last_modified{i}_{date_time}")

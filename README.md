# Metadata Extractor for Digital Forensics

This project is a **Metadata Extractor Application** designed for **Digital Forensics**. It processes a collection of images, extracting metadata beyond what is typically visible in file properties. This includes location data (latitude and longitude), timestamps, camera information, and more. Additionally, it plots the geolocation on an interactive **Leaflet Map**, enabling investigators to visualize where the images were captured.

## Features
- **Image Metadata Extraction**: Retrieves hidden metadata such as camera model, ISO, exposure time, and more.
- **Google Drive Integration**: Extracts metadata from images stored on Google Drive.
- **Exif Data Handling**: Reads EXIF data for deeper insights.
- **Geolocation Mapping**: Displays image locations using **Leaflet Map** based on latitude and longitude.
- **Timestamps**: Shows creation, modification, and last opened times.
- **Ownership and Sharing Information**: Retrieves file ownership, permissions, and sharing status from Google Drive.

## Technologies Used
- **Python**  
- **Pillow** (for image processing)  
- **piexif** (for reading EXIF data)  
- **Google Drive API**  
- **Leaflet.js** (for geolocation map display)

## Prerequisites
1. **Google API Credentials**: Create and download `credentials.json` from the Google Cloud Console.  
2. **Python Packages**:
   - Install the required Python libraries using the following command:
     ```bash
     pip install pillow google-api-python-client google-auth-oauthlib piexif
     ```

3. **Enable Google Drive API**: Ensure you have enabled the Google Drive API in the Google Cloud Console.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/metadata-extractor-digital-forensics.git
   cd metadata-extractor-digital-forensics
   ```

2. **Add Credentials and Token**:
   - Place your `credentials.json` in the root directory.
   - Run the application once to generate `token.json` for authentication.

3. **Authentication**:
   - The app will open a browser to authenticate your Google account the first time it runs.
   - Save the token for future access.

## How to Use

1. **Authenticate with Google Drive**:
   ```python
   creds = authenticate()
   ```

2. **Extract Metadata**:
   ```python
   metadata = get_metadata(file_id, creds)
   print(metadata)
   ```

3. **Display Location on Leaflet Map**:
   If the image contains GPS metadata:
   ```python
   lat, lon = get_gps_location(exif_data)
   print(f"Location: {lat}, {lon}")
   ```

4. **Additional Metadata Retrieval**:
   - **Creation Time**: `get_created_time(file_id, creds)`
   - **Modification Time**: `get_modified_time(file_id, creds)`
   - **Owner Information**: `get_owner_information(file_id, creds)`

## Example Output

- **Camera**: Nikon D850  
- **ISO**: 200  
- **Location**: Latitude: 12.9716, Longitude: 77.5946 (Bangalore, India)  
- **Creation Date**: 2024-10-15 10:32:45.123  
- **Web View Link**: [View on Drive](https://drive.google.com)  

## Map Visualization
The geolocation data extracted from the images will be plotted on a **Leaflet Map** for better visualization.  
Example:

![Leaflet Map](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/OpenStreetMap_Logo.svg/600px-OpenStreetMap_Logo.svg.png)

## File Structure
```
.
├── additional_metadata_info.py
├── credentials.json
├── token.json
├── README.md
└── images/
```

## Known Issues
- Some images may not contain EXIF or GPS data, limiting the metadata that can be extracted.
- Google Drive API quotas may restrict the number of requests per day.

## Future Improvements
- Add support for more file formats (e.g., PDFs, videos).
- Implement batch processing for larger datasets.
- Enable visualization with other mapping libraries (e.g., Google Maps).

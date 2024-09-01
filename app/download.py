import os
import requests
from dotenv import load_dotenv

load_dotenv()

def download_sheet_as_csv(output_file):
    spreadsheet_id = os.getenv('SPREADSHEET_ID')
    sheet_id = os.getenv('SHEET_ID')
    print(f'Downloading sheet {sheet_id} from {spreadsheet_id} to {output_file}')
    url = f'https://docs.google.com/spreadsheets/d/{spreadsheet_id}/export'
    params = {
        'format': 'csv',
        'gid': sheet_id
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        with open(output_file, 'wb') as f:
            f.write(response.content)
        print(f'Successfully downloaded to {output_file}')
    else:
        print(f'Failed to download. HTTP status code: {response.status_code}')
        print(f'Response content: {response.content.decode()}')

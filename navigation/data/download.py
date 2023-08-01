import sys
import requests
import zipfile
import os


def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download&confirm=1"

    session = requests.Session()

    response = session.get(URL, params={"id": id}, stream=True)
    token = get_confirm_token(response)

    if token:
        params = {"id": id, "confirm": token}
        response = session.get(URL, params=params, stream=True)

    save_response_content(response, destination)


def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith("download_warning"):
            return value

    return None


def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)

def unzip_file(zip_file_path, extract_to):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

    # Delete the zip file after extraction
    os.remove(zip_file_path)


def main():
    if len(sys.argv) == 2:
        opt = sys.argv[1]
    else:
        print('Cannot download, please check your cammond. *')
        print('Please run code by python download.py All')
        exit()
        
    drive_id = ['1dcTSEleQoOqriYE0-Hq-r0lHNsQXBSHg', # all.zip
                '1LE-UTlnt8i9mz6-91D_P3DIUoKO9xxVy'] # tx_posistion.zip
    print("dowload TxPosition, CHECK README.md to use the coordinates of TX.")
    size_list = ['6MB']
    download_file_from_google_drive(drive_id[1], './tx_position.zip')
    if opt == 'All':
        print(f"dowload {opt} with {size_list[0]}")
        download_file_from_google_drive(drive_id[0], './all.zip')
    else:
        print('Cannot download, please check your cammond.')
        print('Please run code by python download.py All')
        exit()
    print('done')
    print('start unzip')

    # After downloading the files, unzip them if needed
    print(f"Unzipping {opt}.zip...")
    unzip_file('./All.zip', './')
    unzip_file('./tx_position.zip', './')
    print('done')


if __name__ == "__main__":
    main()
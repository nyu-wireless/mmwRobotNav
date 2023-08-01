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
        print('Please run code by python download.py PartX')
        print('Replace PartX with one of: Part1, Part2, Part3, All')
        exit()
        
    drive_id = ['1Fw_vq2ZjejMjziOHGMqQRC4r4BmnRMVa', # Part1.zip
                '15fA5QZIsTGkl2tEH3Kz1m0Y00laNYgMX', # Part2.zip
                '1GSjFEJ2zex6vPyYnDt62z0Q86NVHT7pN', # Part3.zip
                '1LE-UTlnt8i9mz6-91D_P3DIUoKO9xxVy'] # tx_posistion.zip
    print("dowload TxPosition, CHECK README.md to use the coordinates of TX.")
    size_list = ['31MB', "33MB", '29MB']
    download_file_from_google_drive(drive_id[3], './tx_position.zip')
    if opt == 'Part1':
        print(f"dowload {opt} with {size_list[0]}")
        download_file_from_google_drive(drive_id[0], './Part1.zip')
    elif opt == 'Part2':
        print(f"dowload {opt} with {size_list[1]}")
        download_file_from_google_drive(drive_id[1], './Part2.zip')
    elif opt == 'Part3':
        print(f"dowload {opt} with {size_list[2]}")
        download_file_from_google_drive(drive_id[2], './Part3.zip')
    elif opt == 'All':
        print(f"dowload {opt} with {size_list[0]}")
        download_file_from_google_drive(drive_id[0], './Part1.zip')
        print(f"dowload {opt} with {size_list[1]}")
        download_file_from_google_drive(drive_id[1], './Part2.zip')
        print(f"dowload {opt} with {size_list[2]}")
        download_file_from_google_drive(drive_id[2], './Part3.zip')
    else:
        print('Cannot download, please check your cammond.')
        print('Please run code by python download.py PartX')
        print('Replace PartX with one of: Part1, Part2, Part3, All')
        exit()
    print('done')
    print('start unzip')

    # After downloading the files, unzip them if needed
    if opt == 'Part1':
        print(f"Unzipping {opt}.zip...")
        unzip_file('./Part1.zip', './')
    elif opt == 'Part2':
        print(f"Unzipping {opt}.zip...")
        unzip_file('./Part2.zip', './')
    elif opt == 'Part3':
        print(f"Unzipping {opt}.zip...")
        unzip_file('./Part3.zip', './')
    elif opt == 'All':
        print(f"Unzipping {opt}.zip...")
        unzip_file('./Part1.zip', './')
        unzip_file('./Part2.zip', './')
        unzip_file('./Part3.zip', './')
    unzip_file('./tx_position.zip', './')
    print('done')


if __name__ == "__main__":
    main()
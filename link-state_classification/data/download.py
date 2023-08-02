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
    if len(sys.argv) != 2:
        print('Cannot download, please check your command.')
        print('Please run the code by python download.py PartX')
        print('Replace PartX with one of: Part1, Part2, Part3, All')
        exit()

    opt = sys.argv[1]
    drive_id = [
        '1Fw_vq2ZjejMjziOHGMqQRC4r4BmnRMVa',  # Part1.zip
        '15fA5QZIsTGkl2tEH3Kz1m0Y00laNYgMX',  # Part2.zip
        '1GSjFEJ2zex6vPyYnDt62z0Q86NVHT7pN',  # Part3.zip
        '1LE-UTlnt8i9mz6-91D_P3DIUoKO9xxVy'   # tx_position.zip
    ]
    size_list = ['31MB', '33MB', '29MB']

    print("Download TxPosition, CHECK README.md to use the coordinates of TX.")
    download_file_from_google_drive(drive_id[3], './tx_position.zip')

    if opt == 'All':
        for i in range(3):
            print(f"Download Part{i + 1} with {size_list[i]}")
            download_file_from_google_drive(drive_id[i], f'./Part{i + 1}.zip')
    elif opt.startswith('Part') and opt[4:].isdigit() and 1 <= int(opt[4:]) <= 3:
        part_num = int(opt[4:])
        print(f"Download {opt} with {size_list[part_num - 1]}")
        download_file_from_google_drive(drive_id[part_num - 1], f'./{opt}.zip')
    else:
        print('Invalid command. Please run the code by python download.py PartX')
        print('Replace PartX with one of: Part1, Part2, Part3, All')
        exit()

    print('Download completed. Starting unzip.')

    if opt == 'All':
        for i in range(3):
            print(f"Unzipping Part{i + 1}.zip...")
            unzip_file(f'./Part{i + 1}.zip', './')
    else:
        print(f"Unzipping {opt}.zip...")
        unzip_file(f'./{opt}.zip', './')

    unzip_file('./tx_position.zip', './')
    print('Unzip completed.')

if __name__ == "__main__":
    main()
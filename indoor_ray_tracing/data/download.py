import sys
import requests
import zipfile
import os
import shutil


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
        # Create a folder with the same name as the zip file
        zip_folder_name = os.path.splitext(os.path.basename(zip_file_path))[0]
        zip_folder_path = os.path.join(extract_to, zip_folder_name)
        os.makedirs(zip_folder_path, exist_ok=True)

        for file_info in zip_ref.infolist():
            if file_info.is_dir():
                continue

            file_name = os.path.basename(file_info.filename)
            dest_path = os.path.join(zip_folder_path, file_name)

            if file_name.endswith('.zip'):
                print(f"Unzipping nested zip file: {file_name}...")
                nested_zip_path = zip_ref.extract(file_info, zip_folder_path)
                unzip_file(nested_zip_path, zip_folder_path)
            else:
                with zip_ref.open(file_info) as source, open(dest_path, 'wb') as target:
                    shutil.copyfileobj(source, target)

    # Delete the zip file after extraction
    os.remove(zip_file_path)


def main():
    if len(sys.argv) != 2:
        print('Cannot download, please check your command.')
        print('Please run the code by python download.py PartX')
        print('Replace PartX with one of: Part1, Part2, Part3, Part4, Part5, All')
        exit()

    opt = sys.argv[1]
    drive_id = [
        '1lb1mAEFVloVSyQ_ObXXnE7WwZLdS7aDn',  # Part1.zip
        '10jss0_u6z_Va7DwKFtPXcwGNBabYoYD5',  # Part2.zip
        '1_I9FEuH8YIOUDZt_FRUZeFE5ph8ICf7P',  # Part3.zip
        '1Ia1-XyiW3azMxCXVEXeZfscFaMyyBMzi',  # Part4.zip
        '18ZvOPpAx8x7jqLC8Org7Umkx0ZsD7mDr',  # Part5.zip
        '1LE-UTlnt8i9mz6-91D_P3DIUoKO9xxVy'   # tx_position.zip
    ]
    size_list = ['74MB', '88MB', '103MB', '80MB', '66MB']

    print("Download TxPosition, CHECK README.md to use the coordinates of TX.")
    download_file_from_google_drive(drive_id[5], './tx_position.zip')

    if opt == 'All':
        for i in range(5):
            print(f"Download Part{i + 1} with {size_list[i]}")
            download_file_from_google_drive(drive_id[i], f'./Part{i + 1}.zip')
    elif opt.startswith('Part') and opt[4:].isdigit() and 1 <= int(opt[4:]) <= 5:
        part_num = int(opt[4:])
        print(f"Download {opt} with {size_list[part_num - 1]}")
        download_file_from_google_drive(drive_id[part_num - 1], f'./{opt}.zip')
    else:
        print('Invalid command. Please run the code by python download.py PartX')
        print('Replace PartX with one of: Part1, Part2, Part3, Part4, Part5, All')
        exit()

    print('Download completed. Starting unzip.')

    if opt == 'All':
        for i in range(5):
            print(f"Unzipping Part{i + 1}.zip...")
            unzip_file(f'./Part{i + 1}.zip', './')
    else:
        print(f"Unzipping {opt}.zip...")
        unzip_file(f'./{opt}.zip', './')

    unzip_file('./tx_position.zip', './')
    print('Unzip completed.')

if __name__ == "__main__":
    main()
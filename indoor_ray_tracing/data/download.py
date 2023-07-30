import sys
import requests


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


def main():
    if len(sys.argv) == 2:
        opt = sys.argv[1]
    else:
        print('Cannot download, please check your cammond. *')
        print('Please run code by python download.py PartX')
        print('Replace PartX with one of: Part1, Part2, Part3, Part4, Part5, All')
        exit()
        
    drive_id = ['1lb1mAEFVloVSyQ_ObXXnE7WwZLdS7aDn', # Part1.zip
                '10jss0_u6z_Va7DwKFtPXcwGNBabYoYD5', # Part2.zip
                '1_I9FEuH8YIOUDZt_FRUZeFE5ph8ICf7P', # Part3.zip
                '1Ia1-XyiW3azMxCXVEXeZfscFaMyyBMzi', # Part4.zip
                '18ZvOPpAx8x7jqLC8Org7Umkx0ZsD7mDr', # Part5.zip
                '1LE-UTlnt8i9mz6-91D_P3DIUoKO9xxVy'] # tx_posistion.zip
    print("dowload TxPosition, CHECK README.md to use the coordinates of TX.")
    size_list = ['74MB', "88MB", '103MB', '80MB', '66MB']
    download_file_from_google_drive(drive_id[5], './tx_position.zip')
    if opt == 'Part1':
        print(f"dowload {opt} with {size_list[0]}")
        download_file_from_google_drive(drive_id[0], './Part1.zip')
    elif opt == 'Part2':
        print(f"dowload {opt} with {size_list[1]}")
        download_file_from_google_drive(drive_id[1], './Part2.zip')
    elif opt == 'Part3':
        print(f"dowload {opt} with {size_list[2]}")
        download_file_from_google_drive(drive_id[2], './Part3.zip')
    elif opt == 'Part4':
        print(f"dowload {opt} with {size_list[3]}")
        download_file_from_google_drive(drive_id[3], './Part4.zip')
    elif opt == 'Part5':
        print(f"dowload {opt} with {size_list[4]}")
        download_file_from_google_drive(drive_id[4], './Part5.zip')
    elif opt == 'All':
        print(f"dowload {opt} with {size_list[0]}")
        download_file_from_google_drive(drive_id[0], './Part1.zip')
        print(f"dowload {opt} with {size_list[1]}")
        download_file_from_google_drive(drive_id[1], './Part2.zip')
        print(f"dowload {opt} with {size_list[2]}")
        download_file_from_google_drive(drive_id[2], './Part3.zip')
        print(f"dowload {opt} with {size_list[3]}")
        download_file_from_google_drive(drive_id[3], './Part4.zip')
        print(f"dowload {opt} with {size_list[4]}")
        download_file_from_google_drive(drive_id[4], './Part5.zip')
    else:
        print('Cannot download, please check your cammond.')
        print('Please run code by python download.py PartX')
        print('Replace PartX with one of: Part1, Part2, Part3, Part4, Part5, All')
    print('done')


if __name__ == "__main__":
    main()
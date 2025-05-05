import qrcode

get_url = input('Enter the text or url: ').strip()
get_file_name = input('Enter the file name: ').strip()
qrcode.make(get_url).save(get_file_name)
print(f"QR code saved as {get_file_name}")
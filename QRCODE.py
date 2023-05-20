import qrcode

def generate_qr_code(link, file_path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)

    qr_code = qr.make_image(fill_color="black", back_color="white")
    qr_code.save(file_path)

link = "www.youtube.com"
file_path = "qrcode.png"
generate_qr_code(link, file_path)
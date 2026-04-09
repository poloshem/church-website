import qrcode

# Church website base URL (replace with actual deployed URL after deployment)
BASE_URL = "https://www.lifespringdominionchurchinter.co.ke/"

def generate_home_qr():
    """Generate a QR code for the home page."""
    # Full URL (index.htm is usually the default)
    url = BASE_URL + "index.htm"
    
    # Create QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    # Create image
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save image
    img.save("church_home_qr.png")
    print(f"QR Code generated: church_home_qr.png")
    print(f"URL: {url}")

if __name__ == "__main__":
    print("Generating QR code for Church Home Page...")
    print("-" * 50)
    generate_home_qr()
    print("-" * 50)
    print("Done! Open church_home_qr.png to view.")
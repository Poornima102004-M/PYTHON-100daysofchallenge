import qrcode
from PIL import Image

# Function to generate and display a QR code
def generate_qr_code(data, filename):
    # Generate QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code instance
    img = qr.make_image(fill='black', back_color='white')

    # Save QR code image to a file
    img.save(filename)

    # Display the QR code image
    img.show()

# Example usage
if __name__ == "__main__":
    data = "https://example.com"
    filename = "example_qr_code.png"
    generate_qr_code(data, filename)

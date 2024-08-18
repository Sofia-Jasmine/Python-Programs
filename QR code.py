import qrcode

# Define the data you want to encode in the QR code
data = "https://www.example.com"  # Replace with the data you want to encode

# Generate the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# Create an image of the QR code
qr_image = qr.make_image(fill_color="black", back_color="white")

# Save the QR code as an image file (e.g., PNG)
qr_image.save("qr_code.png")

print("QR code generated and saved as 'qr_code.png'")

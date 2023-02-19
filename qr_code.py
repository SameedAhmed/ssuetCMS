import qrcode
def Sameed():
    features = qrcode.QRCode(version=1,box_size=40,border=5)

    features.add_data("\tHere You have a Google Drive Link below:")
    features.add_data("Your Selected Student: Sameed AHMED")
    features.add_data("\n https://drive.google.com/drive/folders/16BPcpnPFRoVwME9l2v9--9faw-Ekvq9Y")
    features.make(fit=True)
    generate_image = features.make_image(fill_color="black",back_color="white")
    generate_image.save("qrcode.png")

def Aiman():
    features = qrcode.QRCode(version=1,box_size=40,border=5)

    features.add_data("\tHere You have a Google Drive Link below:")
    features.add_data("\nYour Selected Student: Aiman FATIMA")
    features.add_data("\n https://drive.google.com/drive/folders/1RvkM8AJjWE8xBqmJdAZM7XwNJmGUvv0d")
    features.make(fit=True)
    generate_image = features.make_image(fill_color="black",back_color="white")
    generate_image.save("qrcode.png")

def Nabeera():
    features = qrcode.QRCode(version=1,box_size=40,border=5)

    features.add_data("\tHere You have a Google Drive Link below:")
    features.add_data("\nYour Selected Student: Nabeera SIDDIQUI")
    features.add_data("\n https://drive.google.com/drive/folders/1yzgEXIyzj2XfhDE4CcRL9fyWC2FrohKy")
    features.make(fit=True)
    generate_image = features.make_image(fill_color="black",back_color="white")
    generate_image.save("qrcode.png")
    

def Maaz():
    features = qrcode.QRCode(version=1,box_size=40,border=5)

    features.add_data("\tHere You have a Google Drive Link below:")
    features.add_data("\nYour Selected Student: Maaz HUSSAIN")
    features.add_data("\n https://drive.google.com/drive/folders/1I9JYbS8gCb0uGialrUMuWi5jDHdloZyI")
    features.make(fit=True)
    generate_image = features.make_image(fill_color="black",back_color="white")
    generate_image.save("qrcode.png")

    
def Ayaan():
    features = qrcode.QRCode(version=1,box_size=40,border=5)

    features.add_data("\tHere You have a Google Drive Link below:")
    features.add_data("\nYour Selected Student: Ayaan JAWAID")
    features.add_data("\n https://drive.google.com/drive/folders/1hYtG5UA4dN_E58OJQblRYwQ3qeIJlP9t")
    features.make(fit=True)
    generate_image = features.make_image(fill_color="black",back_color="white")
    generate_image.save("qrcode.png")    
# Importing library
import qrcode
import os

def saveQRCode(filename = 'test'):
    # Data to encode
    data = filename

    # Creating an instance of QRCode class
    qr = qrcode.QRCode()

    # Adding data to the instance 'qr'
    qr.add_data(data)

    qr.make(fit=True)
    img = qr.make_image(fill_color='red',
                        back_color='white')

    img.save(os.getcwd() + '/FileGeneration/Data/' + filename + '.png')

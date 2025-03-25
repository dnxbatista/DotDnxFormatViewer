import struct
from PIL import Image
import zlib
from tkinter import messagebox

def SaveFileAsDNX(img_path, save_path):
    """
    Receive a image file and save it as a DNX file
    :param img_path: Open image path
    :param save_path: Save file path
    :return:
    """
    try:
        img  = Image.open(img_path).convert('RGBA')
        width, height = img.size
        pixels = list(img.getdata())

        #Convert pixel data to binary
        raw_data = b''.join(struct.pack('BBBB', r,g,b,a) for r,g,b,a in pixels)

        #Compress pixel data
        compressed_data = zlib.compress(raw_data)

        with open(save_path, 'wb') as f:
            f.write(b'DNX')
            f.write(struct.pack('II', width, height))
            f.write(compressed_data)

        print(f"Saved {save_path}")
    except:
        return

def OpenDNXFile(file_path):
    """
    open a DNX file and return a PIL image, and show it
    :param file_path: Open file path
    :return:
    """
    try:
        with open(file_path, 'rb') as f:
            header = f.read(3)
            print(header)
            if header != b'DNX':
                raise ValueError("Invalid file format")

            width, height = struct.unpack('II', f.read(8))
            compressed_data = f.read()

            #Decompress pixel data
            raw_data = zlib.decompress(compressed_data)

            pixels = [struct.unpack('BBBB', raw_data[i:i+4]) for i in range(0, len(raw_data), 4)]

            img = Image.new('RGBA', (width, height))
            img.putdata(pixels)
            img.show()
            return img
    except:
        return
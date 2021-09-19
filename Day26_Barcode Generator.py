# import EAN13 from barcode module
from barcode import EAN13

# import ImageWriter to generate an image file
from barcode.writer import ImageWriter

number = '123456789101'
my_code = EAN13(number, writer=ImageWriter())
my_code.save("new_code")                          #This will Generate the PNG type image in the same directory in which your python file is.
print("Barcode Generated Successfully!")

from zipfile import ZipFile
import os

zipObj = ZipFile('sample.zip', 'w')

zipObj.write('test_1.txt')
zipObj.write('test_2.txt')
print("Zip File Created Successfully!")

zipObj.close()

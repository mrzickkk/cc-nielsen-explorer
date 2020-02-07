from zipfile import ZipFile
 
 
def main():

    path_zip = '/home/zickk/Documentos/Coca/nielsen/A005SFF1 (10).zip'
    second_path = '/home/zickk/Documentos/Coca/nielsen/A005SFF1.zip'
    # print('Extract all files in ZIP to current directory')
    # # Create a ZipFile Object and load sample.zip in it
    # with ZipFile('sampleDir.zip', 'r') as zipObj:
    #    # Extract all the contents of zip file in current directory
    #    zipObj.extractall()
 
    # print('Extract all files in ZIP to different directory')
 
    # # Create a ZipFile Object and load sample.zip in it
    # with ZipFile('sampleDir.zip', 'r') as zipObj:
    #    # Extract all the contents of zip file in different directory
    #    zipObj.extractall('temp')
 
    # print('Extract single file from ZIP')
 
    # Create a ZipFile Object and load sample.zip in it
    with ZipFile(path_zip, 'r') as zipObj:
        name_file = zipObj.filename
        if name_file.endswith('.zip'):
            zipObj.extractall()
            with ZipFile(second_path, 'r') as unzipObj:
                listOfFileNames = unzipObj.namelist()
                print(listOfFileNames)

       # Get a list of all archived file names from the zip
    #    listOfFileNames = zipObj.namelist()
    #    print(listOfFileNames)
    #    if 
       # Iterate over the file names
    #    for fileName in listOfFileNames:
           # Check filename endswith csv
        #    if fileName.endswith('.csv'):
        #        # Extract a single file from zip
        #        zipObj.extract(fileName, 'temp_csv')
 
 
 
if __name__ == '__main__':
   main()
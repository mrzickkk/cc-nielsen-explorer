import os
import re
from azure.storage.blob import BlockBlobService
from azure.storage.blob.baseblobservice import BaseBlobService

def test_blobs():

    container_name = 'ana-cervantes'
    blob_name = '202001/Archivos Planos'
    ACCOUNT_NAME = 'salrsuse2tcccmbrtest01'
    ACCOUNT_KEY = 'lO9mQDHbdAcYRaurJcSkAyCvXQ/ZMihzUaXyJdcUDk1wgVeowqrn0QgNkW1JB5EVrXae5bmJ/Y2BuAe/NF5h0Q=='
    file_path = 'downloads/'

    base_blob_service = BaseBlobService(
        account_name=ACCOUNT_NAME,
        account_key=ACCOUNT_KEY
    )

    block_blob_service = BlockBlobService(
        account_name=ACCOUNT_NAME,
        account_key=ACCOUNT_KEY
    )
    #os.makedirs(name='zipfiles')

    lista_blobs = (base_blob_service.list_blobs(container_name, prefix=blob_name))
    path = os.path.join(os.path.dirname(__file__))
    for blob in lista_blobs:
        file_blob = blob.name
        if file_blob.endswith('.zip'):
            match_trigger_file = re.search(r"(\d+[/])\w+\s\w+[/](\w+\s\S+)", file_blob)
            
            #base_blob_service.get_blob_to_path(container_name, blob_name=file_blob, file_path='zipfiles/A005SFF1 (10).zip')
    
    # lista = block_blob_service.get_block_list(container_name, blob_name)
    # print(lista_blobs)
    #print(block_blob_service.exists(container_name))


test_blobs()
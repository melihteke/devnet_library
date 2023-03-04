import os
from mydict import MyDict
from boxsdk import JWTAuth
from boxsdk import Client
import boxsdk.exception
import logging
import environment
from pprint import pprint

logging.getLogger('boxsdk').setLevel(logging.CRITICAL)

class BoxClient():
    '''
    The code defines a BoxClient class which provides methods to interact with the Box API for managing files and folders. The class has a class method called get_client() that authenticates with the Box API using the provided client ID, client secret, enterprise ID, public key ID, private key data and passphrase, and returns a client object for performing operations on the API.

    The class also has several instance methods, including:

    - get_folder_contents(client, folder_id): Returns the contents of a Box folder as a list of dictionaries with type, ID and name as keys. The method takes a client object and folder ID as inputs.
    - upload_file(client, folder_id, file_name): Uploads a file to the specified folder on the Box API. The method takes a client object, folder ID and file name as inputs.
    - upload_file_new_version(client, folder_id, local_file_name, file_id): Uploads a new version of an existing file to the specified folder on the Box API. The method takes a client object, folder ID, local file name and file ID as inputs.
    - rename_file(client, file_id, new_file_name): Renames an existing file on the Box API. The method takes a client object, file ID and new file name as inputs.
    - download_file(client, file_id, downloaded_file_name): Downloads a file from the Box API to the specified location. The method takes a client object, file ID and downloaded file name as inputs.
    - get_url_link(client, file_id): Retrieves the download URL for a file on the Box API. The method takes a client object and file ID as inputs.
    - delete_file(client, file_id): Deletes a file from the Box API. The method takes a client object and file ID as inputs.
    
    All methods except for get_client() take a client object as the first parameter, which is used to authenticate with the API and perform operations. The methods return a dictionary containing information about the action performed, such as the file name, folder ID and action name. If an error occurs during the API call, the methods return an empty list or None and print an error message.
    '''
    CLIENT_ID = environment.BOX_CLIENT_ID
    CLIENT_SECRET = environment.BOX_CLIENT_SECRET
    ENTERPRISE_ID = environment.BOX_ENTERPRISE_ID
    PUBLIC_KEY_ID = environment.BOX_PUBLIC_KEY_ID
    PRIVATE_KEY_DATA = environment.BOX_PRIVATE_KEY_DATA
    PRIVATE_KEY_PASSPHRASE = environment.BOX_PRIVATE_KEY_PASSPHRASE

    def __init__(self) -> None:
        pass

    @classmethod
    def get_client(cls):
        if not cls.CLIENT_ID:
            raise ValueError("Missing Box client_id")
        if not cls.CLIENT_SECRET:
            raise ValueError("Missing Box client_secret")
        if not cls.ENTERPRISE_ID:
            raise ValueError("Missing Box enterprise_id")
        if not cls.PUBLIC_KEY_ID:
            raise ValueError("Missing Box public_key_id")
        if not cls.PRIVATE_KEY_DATA:
            raise ValueError("Missing Box private_key")
        if not cls.PRIVATE_KEY_PASSPHRASE:
            raise ValueError("Missing Box private_key_passphrase")

        private_key = cls.PRIVATE_KEY_DATA.encode('ascii').decode('unicode_escape').replace('"', "")

        auth = JWTAuth(
            client_id=cls.CLIENT_ID,
            client_secret=cls.CLIENT_SECRET,
            enterprise_id=cls.ENTERPRISE_ID,
            jwt_key_id=cls.PUBLIC_KEY_ID,
            rsa_private_key_data=private_key,
            rsa_private_key_passphrase=cls.PRIVATE_KEY_PASSPHRASE
        )
        try:
            auth.authenticate_instance()
        except boxsdk.exception.BoxOAuthException:
            print("Authentication Error")
            return

        client = Client(auth)
        return client


    def get_folder_contents(self, client, folder_id) -> list:
        """
        This function returns the contents of a Box folder
        :param client: The client object
        :param folder_id: The folder ID
        :return: The contents of the folder as a list of dictionaries with type, ID and name as keys
        """
        result = []
        try:
            items = client.folder(folder_id=folder_id).get_items()
            for item in items:
                result.append(MyDict({'type': item.type.capitalize(), 'id': item.id, 'name': item.name}))
        except boxsdk.exception.BoxAPIException:
            print("Folder not found")
            return []
        return result

    def upload_file(self, client, folder_id=None, file_name=None):
        root_folder = client.folder(folder_id)
        file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), file_name)
        a_file = root_folder.upload(file_path, file_name=file_name)
        return {'file_name': file_name,
                'folder_id': folder_id,
                'Action':'File Uploaded'}

    def upload_file_new_version(self, client, folder_id=None, local_file_name=None, file_id=None):
        root_folder = client.folder(folder_id)
        file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), local_file_name)
        updated_file = client.file(file_id).update_contents(file_path)
        return {'file_name': local_file_name,
                'folder_id': folder_id,
                'Action':'New version of the file Uploaded'}

    def rename_file(self, client, file_id=None, new_file_name=None):
        file = client.file(file_id)
        renamed_file = file.rename(new_file_name)
        return {'new_file_name': new_file_name,
                'file_id': file_id,
                'Action':'File Renamed'}

    def download_file(self, client, file_id=None, downloaded_file_name=None):
        with open(downloaded_file_name, 'wb') as output_file:
            client.file(file_id).download_to(output_file)
            return {'downloaded_file_name': downloaded_file_name,
                'file_id': file_id,
                'Action':'File downloaded'}

    def get_url_link(self, client, file_id=None):
        download_url = client.file(file_id).get_download_url()
        return {'file_id': file_id,
                'Action':'URL created',
                'url': download_url }

    def delete_file(self, client, file_id=None):
        client.file(file_id).delete()
        return {'file_id': file_id,
                'Action':'File deleted'}



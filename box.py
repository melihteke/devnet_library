"""
The Box Platform module provides functions for working with the Box content management platform using the boxsdk Python library, allowing users to upload, remove, and update files within specific directories.

The following functions are included in this module:
- upload_file(file_path, folder_path): Uploads a file located at the given file_path to the Box folder specified by the folder_path parameter.
- remove_file(file_id): Removes the file with the given ID from the Box platform.
- update_version(file_id, file_path): Updates the file with the given ID on the Box platform to a new version, replacing the existing file content with the contents of the file located at file_path.

By leveraging the functionality provided by the `boxsdk` library through this module, users can easily manage their content on the Box platform without the need for manual interaction. This can improve overall efficiency and reduce the risk of errors or inconsistencies in the content management process.

Note that authentication credentials for the Box platform must be provided in order to use this module. Please refer to the Box API documentation for information on obtaining and managing these credentials.
"""
import os
from mydict import MyDict
from boxsdk import JWTAuth
from boxsdk import Client
import boxsdk.exception
import logging
import environment
from pprint import pprint

logging.getLogger('boxsdk').setLevel(logging.CRITICAL)

# Get environment variables
CLIENT_ID = environment.BOX_CLIENT_ID
CLIENT_SECRET = environment.BOX_CLIENT_SECRET
ENTERPRISE_ID = environment.BOX_ENTERPRISE_ID
PUBLIC_KEY_ID = environment.BOX_PUBLIC_KEY_ID
PRIVATE_KEY_DATA = environment.BOX_PRIVATE_KEY_DATA
PRIVATE_KEY_PASSPHRASE = environment.BOX_PRIVATE_KEY_PASSPHRASE


def get_client():
    if not CLIENT_ID:
        print("Missing Box client_id")
        return None
    if not CLIENT_SECRET:
        print("Missing Box client_secret")
        return None
    if not ENTERPRISE_ID:
        print("Missing Box enterprise_id")
        return None
    if not PUBLIC_KEY_ID:
        print("Missing Box public_key_id")
        return None
    if not PRIVATE_KEY_DATA:
        print("Missing Box private_key")
        return None
    if not PRIVATE_KEY_PASSPHRASE:
        print("Missing Box private_key_passphrase")
        return None

    private_key = PRIVATE_KEY_DATA.encode('ascii').decode('unicode_escape').replace('"', "")

    auth = JWTAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        enterprise_id=ENTERPRISE_ID,
        jwt_key_id=PUBLIC_KEY_ID,
        rsa_private_key_data=private_key,
        rsa_private_key_passphrase=PRIVATE_KEY_PASSPHRASE
    )
    try:
        auth.authenticate_instance()
    except boxsdk.exception.BoxOAuthException:
        print("Authentication Error")
        return

    client = Client(auth)
    return client


def get_folder_contents(client, folder_id) -> list:
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

def upload_file(client, folder_id=None, file_name=None):
    root_folder = client.folder(folder_id)
    file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), file_name)
    a_file = root_folder.upload(file_path, file_name=file_name)
    return {'file_name': file_name,
            'folder_id': folder_id,
            'Action':'File Uploaded'}

def upload_file_new_version(client, folder_id=None, local_file_name=None, file_id=None):
    root_folder = client.folder(folder_id)
    file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), local_file_name)
    updated_file = client.file(file_id).update_contents(file_path)


def rename_file(client, file_id=None, new_file_name=None):
    file = client.file(file_id)
    renamed_file = file.rename(new_file_name)
    print(f'File was renamed to "{renamed_file.name}"')

def download_file(client, file_id=None, downloaded_file_name=None):
    with open(downloaded_file_name, 'wb') as output_file:
        client.file(file_id).download_to(output_file)

def get_url_link(client, file_id=None):
    download_url = client.file(file_id).get_download_url()
    print(f'The file\'s download URL is: {download_url}')

def delete_file(client, file_id=None):
    client.file(file_id).delete()


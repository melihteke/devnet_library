# Retail Store Testing Tool

This project is a network automation tool for a retail store. It includes modules for infrastructure standards, physical topology tests, and platform integration tests.

## Getting Started

### Prerequisites

To run this project, you will need to have Python 3.7 or higher installed on your machine. You will also need to install the required Python packages by running the following command:

```bash
pip install -r requirements.txt

```

## Environment Variables

```python
AD_USERNAME=<USER>
AD_PASSWORD=<PASSWORD>

SLACK_URL=<URL>
SW_USERNAME=<USER>
SW_PASSWORD=<PASSWORD>

VELO_TOKEN=<TOKEN>

SNMP_USERNAME=<USER>
SNMP_AUTH_PASSWORD=<PASSWORD>
SNMP_PRIV_PASSWORD=<PASSWORD>
TACACS_SECRET=<PASSWORD>
RADIUS_SECRET=<PASSWORD>

LOCAL_USERNAME=<USER>
LOCAL_PASSWORD=<PASSWORD>

DB_USER=<USER>
DB_PASS=<PASSWORD>

VERBOSE=False
DEBUG=False

```
You should replace the <USER>, <PASSWORD>, and <URL> placeholders with your own values. Be sure to keep this file secure and not to share it publicly.

## Modules

### infrastructure/standards.py

This module contains the current standard datas for the retail infrastructure, including:

- CELLULAR_ROUTER_OS_VERSION
- SW_9300_OS_VERSION
- SW_3650_OS_VERSION
- SW_NUM_OF_STACK_MEMBER
- SW_9300_LICENCE_PACKAGE
- SW_9300_SYSTEM_IMAGE
- SW_MODE
- ETC.

### slack.py
This module provides a simple interface for sending notifications to a Slack channel. It uses the requests module to send HTTP requests to the Slack API.

### store.py
This module defines the Store class, which represents a retail store. It has the following attributes:

- store_number: the store's unique identifier
- geo: the store's geographic location (default: 'emea')
- store_type: the store's type (default: 'nike')

## box.py
This module box.py provides a BoxClient class that interacts with the Box API for managing files and folders. It has a class method get_client() that authenticates with the Box API using the provided client ID, client secret, enterprise ID, public key ID, private key data, and passphrase, and returns a client object for performing operations on the API.

The BoxClient class has several instance methods, including:

get_folder_contents(client, folder_id): Returns the contents of a Box folder as a list of dictionaries with type, ID, and name as keys. The method takes a client object and folder ID as inputs.
upload_file(client, folder_id, file_name): Uploads a file to the specified folder on the Box API. The method takes a client object, folder ID, and file name as inputs.
upload_file_new_version(client, folder_id, local_file_name, file_id): Uploads a new version of an existing file to the specified folder on the Box API. The method takes a client object, folder ID, local file name, and file ID as inputs.
rename_file(client, file_id, new_file_name): Renames an existing file on the Box API. The method takes a client object, file ID, and new file name as inputs.
download_file(client, file_id, downloaded_file_name): Downloads a file from the Box API to the specified location. The method takes a client object, file ID, and downloaded file name as inputs.
get_url_link(client, file_id): Retrieves the download URL for a file on the Box API. The method takes a client object and file ID as inputs.
delete_file(client, file_id): Deletes a file from the Box API. The method takes a client object and file ID as inputs.
All methods except for get_client() take a client object as the first parameter, which is used to authenticate with the API and perform operations. The methods return a dictionary containing information about the action performed, such as the file name, folder ID, and action name. If an error occurs during the API call, the methods return an empty list or None and print an error message.
### How to run the app in dockercontainer

1- Open a terminal window and navigate to the directory where the Dockerfile is saved.

2- Build the Docker image using the following command:

```bash
docker build -t nike-app .

```
This command will create a Docker image called "nike-app" based on the instructions in the Dockerfile.

3- Once the Docker image is built, run the app in a container using the following command:

```bash
docker run -p 8000:8000 nike-app

```
This command will start a container using the "nike-app" image and map port 8000 in the container to port 8000 on the host machine..



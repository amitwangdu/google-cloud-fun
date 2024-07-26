# Google cloud Function course
## Starting a project
To start the new project in gcp we can go to the 
[Firebase console](http://console.firebase.google.com) or 
created it from[Google Cloud Platform Console](http://console.cloud.google.com).
## creating the virtual environment
Ffirst we have to install 'python3-venv'

Then execute the following command
'''
python3 -m venv venv
'''\'

To activate the virtual env we do :
source venv/bin/activate
'''
in order to add new packages to our virtual env we create a file call requurements.txt and execute the following command:
'''
pip install -r requirements.txt
'''
### Deploy the cloud function in gcp
First we have to set the project id with the following commands:

'''
gcloud config set project [YOUR_PROJECT_ID]
'''
 gcloud functions deploy [FUNCTION_NAME] --runtime python37 --trigger-http
'''


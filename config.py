#pip install python-dotenv
from dotenv import load_dotenv
import os

#load the .env file
load_dotenv()

#Access the environment variables

client_id = os.getenv("client_id")
client_secret =os.getenv("client_secret")
refresh_token = os.getenv("refresh_token")
access_token = os.getenv("access_token")
code= os.getenv("code")
profile_id= os.getenv("profile_id")   
defect_dojo_Api= os.getenv("defect_dojo_Api")
Gmail_user= os.getenv("Gmail_user") 
Gmail_password= os.getenv("Gmail_password") 
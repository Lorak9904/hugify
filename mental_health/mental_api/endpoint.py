from decouple import config
from google.cloud import aiplatform
from google.oauth2 import service_account
from google.cloud import aiplatform

# def analyze_emotion(text):
#     # Initialize the Vertex AI client
#     aiplatform.init(
#         project=config("PROJECT_ID"),  # Replace with your project ID
#         location=config("REGION")     # Replace with your endpoint's region
#     )
    
#     # Endpoint ID of your deployed model
#     endpoint = aiplatform.Endpoint(
#         endpoint_name=config("ENDPOINT")  # Replace with your endpoint ID
#     )
    
#     # Make a prediction
#     response = endpoint.predict(instances=[text])
    
#     # Extract and return prediction result
#     if response.predictions:
#         return response.predictions[0]
#     else:
#         return "Error: No prediction returned"
    

def analyze_emotion(text):
    # Specify the path to your service account key file
    credentials = service_account.Credentials.from_service_account_file(
        'key.json'  # Replace with the actual path to your key.json file
    )
    
    # Initialize the Vertex AI client with the credentials
    aiplatform.init(
        project=config("PROJECT_ID"),  # Replace with your project ID
        location=config("REGION"),     # Replace with your region
        credentials=credentials     # Attach the credentials explicitly
    )
    
    # Endpoint ID of your deployed model
    endpoint = aiplatform.Endpoint(
        endpoint_name=config("ENDPOINT")  # Replace with your endpoint ID
    )
    
    # Make a prediction
    response = endpoint.predict(instances=[text])
    
    # Extract and return prediction result
    if response.predictions:
        return response.predictions[0]
    else:
        return "Error: No prediction returned"
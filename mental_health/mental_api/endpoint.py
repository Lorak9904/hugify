from decouple import config

from google.cloud import aiplatform

def analyze_emotion(text):
    # Initialize the Vertex AI client
    aiplatform.init(
        project=config("PROJECT"),  # Replace with your project ID
        location=config("LOCATION")     # Replace with your endpoint's region
    )
    
    # Endpoint ID of your deployed model
    endpoint = aiplatform.Endpoint(
        endpoint_name=config("ENDPOINT_ID")  # Replace with your endpoint ID
    )
    
    # Make a prediction
    response = endpoint.predict(instances=[text])
    
    # Extract and return prediction result
    if response.predictions:
        return response.predictions[0]
    else:
        return "Error: No prediction returned"
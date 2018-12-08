from wand.image import Image


def hello_gcs(event, context):
  
    from google.cloud import storage
    
    # Instantiates a client
    storage_client = storage.Client()

    
    eventBucket= event['bucket']
    eventName=event['name']
    
    bucket = storage_client.get_bucket(eventBucket)
    blob = bucket.blob(eventName)
    
    blob.download_to_filename('/tmp/image.jpg')
    
    with Image(filename='/tmp/image.jpg') as img:
        img.resize(200, 200)
        img.save(filename='/tmp/image.jpg')
    
    	
    bucket = storage_client.get_bucket('my-new-bucket111-sau')

    destination_blob_name= eventName
        
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename('/tmp/image.jpg')
    
    
    
        
    
    
    
    

    
    
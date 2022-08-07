import json

def lambda_handler(event, context):
    
    # --------------------
    # Parse DynamoDB Events
    # --------------------
    
    dynamo_events = event['Records']
    #print(dynamo_events)
    
    for event in dynamo_events:
        #print(event)
        
        personid = (event['dynamodb']['NewImage']['person-id']['N'])
        name = (event['dynamodb']['NewImage']['name']['S'])
        email = (event['dynamodb']['NewImage']['email']['S'])
        
        print(personid)
        print(name)
        print(email)
        
    # --------------------
    # Insert into OpenSearch Index
    # --------------------
    
    

        
    return {
        'statusCode': 200,
        'body': json.dumps('Success')
    }
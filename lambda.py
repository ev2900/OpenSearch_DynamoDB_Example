import json
import urllib3

def lambda_handler(event, context):
    
    dynamo_events = event['Records']
    #print(dynamo_events)

    bulk_documents_opensearch = ''
    
    print("Batch Count: " + str(len(dynamo_events)))
    
    # Parse DynamoDB Change Evenet 
    #print(event['dynamodb']['NewImage']['person-id']['N'])
    #print(event['dynamodb']['NewImage']['name']['S'])
    #print(event['dynamodb']['NewImage']['email']['S'])
    
    for event in dynamo_events:
        #print(event)
        
        if event['eventName'] != 'REMOVE':
            #print("Not a delete")

            document_body = {
                "personid": event['dynamodb']['NewImage']['person-id']['N'],
                "name": event['dynamodb']['NewImage']['name']['S'],
                "email": event['dynamodb']['NewImage']['email']['S']
            }
            
            meta_data = {
                "index": 
                {
                  "_id": str(event['dynamodb']['NewImage']['person-id']['N'])
                }
            }
    
            bulk_documents_opensearch = str(bulk_documents_opensearch) + str(meta_data) + str('\n')
            bulk_documents_opensearch = str(bulk_documents_opensearch) + str(document_body) + str('\n')
            bulk_documents_opensearch = bulk_documents_opensearch.replace("'", "\"")
            
        else:
            # print("Delete")
            
            meta_data = {
                "delete": 
                {
                  "_id": str(event['dynamodb']['OldImage']['person-id']['N'])
                }
            }
    
            bulk_documents_opensearch = str(bulk_documents_opensearch) + str(meta_data) + str('\n')
            bulk_documents_opensearch = bulk_documents_opensearch.replace("'", "\"")
        
    # ------
    # Send DynamoDB Evenet(s) to OpenSearch via. bulk API
    # ------
    #print(bulk_documents_opensearch)
    
    http = urllib3.PoolManager()
    
    os_url = '<os_url>'.rstrip("/")
    index_name = 'person'
    auth_header = urllib3.make_headers(basic_auth='OSMasterUser:AwS#OpenSearch1')
    
    resp = http.request(
        'POST',
        os_url + '/' + index_name + '/' + '_bulk/',
        body=bulk_documents_opensearch,
        headers={'Content-Type': 'application/x-ndjson', 'authorization': auth_header['authorization']}
    )
    
    # API Response
    # print('Request sent')
    print('OpenSearch response status = ' + str(resp.status))
    #print(resp.headers)
    print('OpenSearch response body = ' + str(resp.data.decode('utf-8')))

    return {
        'statusCode': 200,
        'body': json.dumps('Success')
    }

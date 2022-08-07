# DynamoDB OpenSearch Example

1. Run the CloudFormation stack below

[![Launch CloudFormation Stack](https://sharkech-public.s3.amazonaws.com/misc-public/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home#/stacks/new?stackName=dynamo-lambda-opensearch&templateURL=https://sharkech-public.s3.amazonaws.com/misc-public/dynamo_lambda_opensearch.yaml)

2. Update the code section of the deployed lambda with the [lambda.py](https://github.com/ev2900/DynamoDB_OpenSearch_Example/blob/main/lambda.py) code
3. Update the ```os_url```, ```index_name```, ```auth_header``` 
4. Add a DynamoDB trigger to the lambda

5. Use the PartiQL editor in DynamoDB insert 3 record

```
-- Insert #1
INSERT INTO "workshop-table" VALUE {
	'person-id': 1,
    'name': 'Will Smith',
    'email': 'willsmith@email.com'
}

-- Insert #2
INSERT INTO "workshop-table" VALUE {
	'person-id': 2,
    'name': 'John Parker',
    'email': 'parker@email.com'
}

-- Insert #3
INSERT INTO "workshop-table" VALUE {
	'person-id': 3,
    'name': 'Adam William',
    'email': 'adamw@email.com'
}
```

6. If you log into the OpenSearch dashboard, create and index patter you can see the 3 records in OpenSearch

For testing purposes to delete the records in DynamoDB via. PartiQL

```
DELETE FROM "workshop-table" WHERE "person-id" = 1
DELETE FROM "workshop-table" WHERE "person-id" = 2
DELETE FROM "workshop-table" WHERE "person-id" = 3
```

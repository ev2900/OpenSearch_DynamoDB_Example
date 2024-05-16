# DynamoDB OpenSearch Example

<img width="275" alt="map-user" src="https://img.shields.io/badge/cloudformation template deployments-21-blue"> <img width="85" alt="map-user" src="https://img.shields.io/badge/views-181-green"> <img width="125" alt="map-user" src="https://img.shields.io/badge/unique visits-061-green">

The instruction below outline how to keep OpenSearch upto date with a DynamoDB table via. a Lambda function

1. Run the CloudFormation stack below

[![Launch CloudFormation Stack](https://sharkech-public.s3.amazonaws.com/misc-public/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home#/stacks/new?stackName=dynamo-lambda-opensearch&templateURL=https://sharkech-public.s3.amazonaws.com/misc-public/dynamo_lambda_opensearch.yaml)

The resources created by the CloudFormation stack are documented in the architecture below

<img alt="dynamo-lambda-os" src="https://github.com/ev2900/DynamoDB_OpenSearch_Example/blob/main/Architecture/dynamo-lambda-opensearch.png">

Or run the CloudFormation stack below to deploy a VPC based architecture

[![Launch CloudFormation Stack](https://sharkech-public.s3.amazonaws.com/misc-public/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home#/stacks/new?stackName=dynamo-lambda-opensearch&templateURL=https://sharkech-public.s3.amazonaws.com/misc-public/dynamo_lambda_opensearch_vpc.yaml)

<img alt="dynamo-lambda-os" src="https://github.com/ev2900/DynamoDB_OpenSearch_Example/blob/main/Architecture/dynamo-lambda-opensearch-vpc.png">

2. Update the code section of the deployed lambda with the [lambda.py](https://github.com/ev2900/DynamoDB_OpenSearch_Example/blob/main/lambda.py) code
3. Update the ```<os_url>```place holder in the lambda code
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

6. Log into the OpenSearch dashboard, create and index patter you can see the 3 records in OpenSearch

7. Optional. Test the update / delete capabilities via. the PartiQL editor

Update(s)

```
-- Update #1
UPDATE "workshop-table" SET name='William Smith' WHERE "person-id" = 1

-- Update #2
UPDATE "workshop-table" SET name='Jonathan Parker' WHERE "person-id" = 2

-- Update #3
UPDATE "workshop-table" SET name='Sr. Adam William' WHERE "person-id" = 3
```

Delete(s)

```
-- Delete #1
DELETE FROM "workshop-table" WHERE "person-id" = 1

-- Delete #2
DELETE FROM "workshop-table" WHERE "person-id" = 2

-- Delete #3
DELETE FROM "workshop-table" WHERE "person-id" = 3
```

# DynamoDB OpenSearch Example

1. Run the CloudFormation stack below

[![Launch CloudFormation Stack](https://sharkech-public.s3.amazonaws.com/misc-public/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home#/stacks/new?stackName=open-search-demo&templateURL=https://sharkech-public.s3.amazonaws.com/misc-public/OpenSearch_demo.yaml)

2. In the PartiQL editor in DynamoDB insert 3 records using the SQL below

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

3. 

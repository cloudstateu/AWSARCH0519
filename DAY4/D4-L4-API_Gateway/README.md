<img src="../../img/logo.png" alt="Chmurowisko logo" width="200" align="right">
<br><br>
<br><br>
<br><br>

# Introduction to Amazon API Gateway

## LAB Overview

#### This lab will give you a basic understanding of Amazon API Gateway. You will create an API Gateway and Lambda function. This solution will be used to send an information to the DynamoDB table.

## Task 1: Create Lambda Function.
In this section, you will create a lambda function.

1. On the **Services** menu, click **Lambda**.

2. Press **Create function**.

3. Select: **Author from scratch.**

4. Provide following information:

   * **Name:** StudentX
   * **Runtime:** Python 3.6
   * **Role:** Choose an existing role
   * **Existing role:** FULL_LAMBDA_ROLE

5. Click **Create function**.

6. Scroll down to the code editor.

7. Copy the content of the file **[LambdaFun.py](LambdaFun.py)** to the code editor.

   ```python
   import json
   import boto3
   import os
   
   dbclient = boto3.client("dynamodb")
   table_name = os.environ['TABLE_NAME']
   
   def lambda_handler(event, context):
       # TODO implement
       print(json.dumps(event))
       name = event['message']
       email = event['email']
       print("name = {}, email = {}".format(name, email))
       response = save_person(email, name)
       return {
           'statusCode': 200,
           'body': json.dumps(response)
       }
   
   
   def save_person(email, name):
       item = create_item(email, name)
       response = add_item_to_dynamodb_table(table_name, item)
       return response
       
   def create_item(email, name):
       item = {
       'email': {'S': email},
       'name': {'S': name}
       }
       return item
       
   def add_item_to_dynamodb_table(table, item):
       response = dbclient.put_item(TableName=table, Item=item)
       return(response)
   ```

   

8. Scroll down to the **Environment variables**

9. Create a new one be putting:

   * Key**: TABLE_NAME**
   * Value: **materialy**

10. **Save** the function (top right corner)

## Task 2: Create an API Gateway

In this section, you will create API Gateway and point the resources to the lambda funtions

11. On the Services menu, click API Gateway
12. Click Create API.
13. Select New API and provide the name: studentX
14. Endpoint Types choose Regional.
15. Click Create API.
16. In the **Resources** section of your API click **Actions** 
17. Click **Create Resources** 
18. Provide following configuration: 
    * **Resource Name**: sendmsq 
    * **Resource Path**: /sendmsq 
19. Click **Create Resource**. 
20. When a **/sendmsq** is highlighted (in the Resources column), click **Actions** 
21. Click **Create Method** 
22. Form dropdown menu select **POST** and confirm
23. In the /sendmsq POST - Setup window select: 
    * **Integration type:** Lambda Function 
    * **Lambda Region:** eu-west-1 
    * **Lambda Function:** name of your lambda 
24. Click **Save** and then **OK** 
25. Once again click on **Actions.** 
26. Select **Enable CORS** and just press **Enable CORS and replace existing CORS headers** 
27. Confirm by clicking **YES.....** 
28. Again click on **Actions** 
29. Select **Deploy API** 
30. Provide informations: 
    * Deployment stage: [New Stage] 
    * Stage name: test 
    * Stage description: test api 
    * Deployment description: my first api 
31. Click **Deploy**. 
32. Copy your **Invoke URL** 

Example: https://5jo4t9i0l7.execute-api.eu-west-1/amazonaws.com/test

## Task 3: TEST your API

In this section, you will test the backend presented over API Gateway

33. Open your favorite web browser and paste the following url: **http://contact.becomecloud.ninja**
34. Provide all necessary informations: 
    * **Backend URL:** paste your Invoke URL
    * **EMAIL:** your email if you want to received training materials + addons. 
    * Message
35. Click **Send**

Now your message should appear in DynamoDB table “materialy”. Go to the DynamoDB and check it.

## END LAB

Congratulations! You have now successfully completed this laboratory.

<br><br>

<center><p>&copy; 2019 Chmurowisko Sp. z o.o.<p></center>
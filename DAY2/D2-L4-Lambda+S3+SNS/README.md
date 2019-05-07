<img src="../../img/logo.png" alt="Chmurowisko logo" width="200" align="right">
<br><br>
<br><br>
<br><br>

# AWS Lambda + S3 + SNS

## LAB Overview

#### This lab lets you build a serverless solution which uses AWS Lambda triggered by S3 bucket and simple Notification Service 

#### This lab will demonstrate:
* Creating S3 bucket
* Creating AWS Lambda function and connecting it to S3 bucket

## Task 1: Creating S3 bucket
In this task you will create private S3 bucket

1. In the AWS Management Console, on the **Services** menu, click **S3**.
2. Click **Create bucket**.
3. Enter a bucket name, e.g. "StudentX-upload".
4. Click **Create**.

## Task 2: Create a simple Lambda function

In this task you will create simple Lambda function and will look into event object.

1. In the AWS Management Console, on the **Services** menu, click **Lambda**.
2. Click **Create function**.
3. Insert a name for your function e.g "Student-X-Lambda".
4. Select "Python 3.6" as a runtime.
5. Select "Create a new role with basic Lambda permissions" in the Role menu.
6. Click **Create function** .
7. Download **[simple_lambda.py](simple_lambda.py)** file and paste the file content into lambda function editor.
8. Click **Save** button.
9. Click **Test** button.
10. Select "Amazon S3 Put" as **Event template**.
11. Enter a name for "Event name", e.g. "Testevent".
12. Click **Create** button.
13. Click **Test** button.
14. Go to the top of the page and click **Monitoring**.
15. Click **View logs in CloudWatch**.
16. Click on the latest log stream.
17. Look into lambda execution details. Take a look at test data passed to Lambda function as an event. Find bucket and object name.

## Task 3: Configuring S3 events as Lambda trigger

In this task you will connect your S3 bucket events to your Lambda function. Putting any object into S3 bucket will trigger the Lambda.

1. In the AWS Management Console, on the **Services** menu, click **Lambda**.
2. Find your Lambda function and click on its name.
3. In the **Designer** area select "S3" as a trigger.
4. Scroll down and select your bucket as **Bucket**.
5. Select "All object create events" as **Event type**.
6. Mark **Enable trigger** as checked.
7. Click **Add**.
8. Click **Save**.
9. In the AWS Management Console, on the **Services** menu, click **S3**.
10. Find your bucket and click on its name.
11. Click **Upload**.
12. Click **Add files**.
13. Select any file and click **Upload**.
14. Go back to your Lambda function.
15. Go to the top of the page and click **Monitoring**.
16. Click **View logs in CloudWatch**.
17. Click on the latest log stream.
18. Look into lambda execution details. Take a look at test data passed to Lambda function as an event. Find bucket and object name.


## Task 4: Editing Lambda code. Generating signed URLs and sending SMS using SNS.

In this task you will edit existing Lambda code. Lambda will generate signed url for every uploaded file and send SMS using Simple Notification Service.

1. In the AWS Management Console, on the **Services** menu, click **Lambda**.
2. Find your Lambda function and click on its name.
3. Download **[lambda.py](lambda.py)** file and paste the file content into lambda function editor.
4. Scroll down and insert two environment variables:
* phone_number - number of the phone SNS will send messages to eg. +48111111111
* sender_id - self explanatory variable ;-) (between 1 and 11 chars)
5. Click **Save**.
6. Click **View the \<your role name\>** link.

![Editing role](./img/edit_role.png)

7. Click **Add inline policy**.
8. Click **Choose a service**.
9. Click **SNS**.
10. Unwind **Write** actions.
11. Select **Publish**.
12. As **Resources** select **All resources**.
13. Click **Review policy**.
14. Enter a name for your policy.
15. Click **Create policy**.

## Task 5: Testing the solution

In this task you will test if everything is ok. After uoploading any file to your S3 bucket you should get a message with a signed url to your file.

1. In the AWS Management Console, on the **Services** menu, click **S3**.
2. Find your bucket and click on its name.
3. Click **Upload**.
4. Click **Add files**.
5. Select any file and click **Upload**.

You should get a message in a moment. If anything goes wrong look into **Cloud watch** logs.

## END LAB

<br><br>

<center><p>&copy; 2019 Chmurowisko Sp. z o.o.<p></center>
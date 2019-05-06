<img src="../../img/logo.png" alt="Chmurowisko logo" width="200" align="right">
<br><br>
<br><br>
<br><br>

# AWS Cross Account Access

## LAB Overview

#### This LAB teaches you how to use a role to delegate access to resources that are in different AWS accounts that you own (ex. Production and Development). You share resources in one account with users in a different account. By setting up cross-account access in this way, you don't need to create individual IAM users in each account.

## Task 1: Create S3 bucket

In this task you will create an S3 bucket that will be shared with another AWS Account.

1. In the AWS Management Console, on the **Services** menu, click **S3**. 
2. Click **+Create bucket** button. 
3. Paste the name: **studentX-caa** 
4. Select Region: **EU (Ireland)** 
5. Click **Create**.

## Task 2: Create IAM Policy

Before creating the role, prepare the managed policy that defines the permissions that the role requires. You attach this policy to the role in a later step.

6. In the AWS Management Console, on the **Services** menu, click **IAM**.
7. In the navigation pane on the left, click **Policies**.
8. Click **Create policy** button.
9. Choose the **JSON** tab and copy the text from the following JSON policy document (or take from file [cca_policy.json](cca_policy.json)).

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "s3:ListAllMyBuckets",
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:ListBucket",
        "s3:GetBucketLocation"
       ],
      "Resource": "arn:aws:s3:::YOUR_BUCKET_NAME"
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject",
        "s3:DeleteObject"
      ],
      "Resource": "arn:aws:s3:::YOUR_BUCKET_NAME/*"
    }
  ]
}
```

10. Paste this text into the **JSON** text box, replacing the resource ARN (`arn:aws:s3:::YOUR_BUCKET_NAME`) with the real one appropriate to your S3 bucket.
11. Click **Review policy**.
12. Insert the name for the policy **StudentX-CAA**.
13. Click **Create policy**.

## Task 3: Create IAM Role

To allow users from one AWS account to access resources in another AWS account, create a role that defines who can access it and what permissions it grants to users that switch to it.

14. In the AWS Management Console, on the **Services** menu, click **IAM**.
15. In the navigation pane on the left, click **Roles**.
16. Choose the **Another AWS account** role type.
17. For **Account ID**, enter account ID provided by the instructor.

For now you do not need to require an external ID, or require users to have multi-factor authentication (MFA) in order to assume the role. So leave these options unselected

18. Choose **Next: Permissions** to set the permissions that will be associated with the role.
19. Select the box next to the policy that you created previously.
20. Click **Next: Tags** and **Next: Review**.
21. For **Role name** type **StudentX-CAA**.
22. Click **Create role**.

## Task 4: Test 

Notify the instructor when you are ready to check.

Instructor will test solution from another account.



## END LAB

Follow these steps to end the lab.

23. In the AWS Management Console, on the **Services** menu, click **IAM**.
24. In the navigation pane on the left, click **Roles**.
25. Look for role created in task 3 and delete it.
26. In the navigation pane on the left, click **Policies**.
27. Find and delete policy created in task 2.

<br><br>

<center><p>&copy; 2019 Chmurowisko Sp. z o.o.<p></center>
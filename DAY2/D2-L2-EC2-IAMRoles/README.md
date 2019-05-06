<img src="../../img/logo.png" alt="Chmurowisko logo" width="200" align="right">
<br><br>
<br><br>
<br><br>

# Creating IAM Roles for EC2

## LAB Overview

#### In this lab you will create a Role for your EC2 instances. This role gives permissions to S3 bucket, where the code of the application will be stored. Next, you will spin up a new EC2 instance with a created Role and automated process of code deployment.

## Task 1: Create S3 bucket

In this task you will create an S3 bucket for storing an application code.

1. In the AWS Management Console, on the **Services** menu, click **S3**. 
2. Click **+Create bucket** button. 
3. Paste the name: **csa0419-studentX** 
4. Select Region: **EU (Ireland)** 
5. Click **Create**. 

## Task 2: Create IAM Role

During this task you will create an IAM Role for your servers. This Role grants permission to read and write
to your S3 bucket. With this role you will be able to sync a code and implement it with a new EC2 instances.

6. In the AWS Management Console, on the **Services** menu, click **IAM**.
7. In the navigation pane on the left, click **Roles**.
8. Click **Create role** button.
9. For **Select type of trusted entity** choose the **EC2** service and **EC2** for use case.
10. Click **Next:Permissions**.

You can choose one or more policies that are already created. Policies with the orange icon are created by AWS (called AWS Managed policies).  For our lab you will create a new Policy from scratch.

11. Click **Create policy**.

12. Switch to **JSON** tab and paste the code (availeble in [S3_Access_Policy_ext.json](S3_Access_Policy_ext.json) ):

    ```JSON
    {
      "Version": "2012-10-17",
      "Statement":[
        {
          "Effect": "Allow",
          "Action": [
            "s3:GetObject",
            "s3:PutObject",
            "s3:ListBucket"
          ],
          "Resource": [
            "arn:aws:s3:::your_bucket_name",
            "arn:aws:s3:::your_bucket_name/*"
            ]
        },
        {
          "Effect": "Allow",
          "Action": "s3:ListAllMyBuckets",
          "Resource": "arn:aws:s3:::*"
        }
      ]
    }
    ```

13. In **Resource** section insert the name of your bucket.
14. Click **Review policy**.
15. Insert the name for the policy **StudentX-S3Access**.
16. Click **Create policy**.
17. Switch back to the create role windows and press **Refresh** and in the **Search** box search for you policy.
18. Select your policy and press **Next:Review**.
19. Insert the **Role name**: **StudentX-EC2Role**.
20. Click **Create role**.

## Task 3: Assign role to your EC2

In this task you will assign an IAM Role to your current EC2 instance, and copy an application code to your S3 bucket.

21. In the AWS Management Console, on the **Services** menu, click **EC2**.
22. In the navigation pane on the left, click **Instances**.
23. Select your instance and press **Action**.
24. Go to **Instance Setting** and choose **Attache/Replace IAM Role**.
25. Select your IAM role and press **Apply**.
26. Go back to an EC2’s ssh console.
27. Check if IAM Role is assigned to instance: **curl http://169.254.169.254/latest/meta-data/iam/info/**

As a result you will get an **InstanceProfileArn** with a name of your IAM Role. This is an example of using instance metadata to get the configuration details about your machine.

28. Check the access to the s3 by typing: **aws s3 ls**

You should get a list of  S3 buckets created on this AWS Account. AWS provides also a cli which is another option to manage AWS resources. In this lab you are using cli to interact with Amazon S3 service.

```shell
aws s3 ls 
2018-11-07 12:04:52 awsmasterprzemek
2019-02-19 15:51:40 cf-templates-10pk9zx0qpxae-eu-central-1
2018-12-04 17:39:51 cf-templates-10pk9zx0qpxae-eu-west-1
2018-06-18 12:12:39 cf-templates-10pk9zx0qpxae-us-east-1
2018-07-10 08:47:02 cf-templates-10pk9zx0qpxae-us-east-2
2018-06-06 10:40:17 chmodcsaalllogs
2018-10-17 10:16:28 config-bucket-094104221953
2018-12-06 22:13:14 contact.becomecloud.ninja
2018-07-02 14:19:43 student0.becomecloud.ninja
```

29. List the content of your S3 bucket created in task 1:

```sh
aws s3 ls s3://csa0419-studentX
```

30. Try to list the content one of your colleague’s S3 bucket.

You should get an error: “*An error occurred (AccessDenied) when calling the ListObjects operation: Access Denied”* 
Do you know why?

31. Go to your application’s code:

```she
cd /var/www/html
```

32. Copy index.php file into your s3 bucket:

```she
aws s3 cp index.php s3://csa0419-studentX
```

33. Check your S3 bucket:

```shell
aws s3 ls s3://csa0419-studentX
```



## Task 4: Create new EC2 instance

In this task you will spin up a new EC2 machine with EC2 role and deploy the code.

34. On the **Services** menu, click **EC2**.
35. Click **Launch** **Instance**.
36. Select **Amazon Linux AMI.**
37. On the **Choose an Instance Type** page, select the **t2.micro** instance type.
38. Click **Next: Configure Instance Details**.
39. On the **Configure Instance Details** page select your VPC and your public subnet and enable public IP.
40. Additionally set up IAM Role that you created in task 2.
41. Scroll down and expand the **Advanced Details** section.
42. For **User data**, select **As text**.
43. Copy the initialization script seen below. Paste the script into the **User data** box:

```shell
#!/bin/sh
yum -y install httpd php &&
chkconfig httpd on &&
/etc/init.d/httpd start &&
aws s3 cp s3://csa0419-studentX/index.php /var/www/html
```

You can also copy a script from [bootstrap.sh](bootstrap.sh)

**Note:** Don’t forget to provide your bucket name in the list line of the script!

44. Click **Next: Add Storage**.
45. Click **Next: Add Tags** to accept the default storage device configuration.
46. On the **Add Tags** page, click **Add Tag,** type a **Name** for a Key box and  studentX_02 in the Value  box.
47. Click **Next: Configure Security Group**.
48. For **Assign a security group**, select a WebServers Security Group you created in LAB2-VPC.
49. Click **Review and Launch**.
50. Review your choices, and then click **Launch**.
51. Select a key you created in Lab 3 and check Acknowledge box.
52. On the status page, which notifies you that your instances are launching, click **View Instances**.
53. Select your instance to display a list of details and status update in the lower pane.
54. Copy the **Public DNS (IPv4)** value to your Clipboard.
55. Open a new browser window, and then paste the public DNS value into the address bar.

You should see your application. If not wait for a moment and try again.



## END LAB

This is the end of the lab. Terminate instance your created in this LAB (studentX_02).

56. In AWS console select your **studentX_02** EC2 instance.
57. Click **Action** button and select **Instance state** -> **Terminate.**
58. Click **Yes, Terminate.**

<br><br>


<center><p>&copy; 2019 Chmurowisko Sp. z o.o.<p></center>
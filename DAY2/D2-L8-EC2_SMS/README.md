<img src="../../img/logo.png" alt="Chmurowisko logo" width="200" align="right">
<br><br>
<br><br>
<br><br>

# EC2 Systems Manager - Run Command

## LAB Overview

#### In this lab you will create use EC2 System Manager to restore ssh connection to your virtual machine.

## Task 1: Create IAM Role for SSM.

By default, AWS Systems Manager doesn't have permission to perform actions on your instances. You must grant access by using an AWS Identity and Access Management (IAM) instance profile. 

1.  In the AWS Management Console, on the **Services** menu, click **IAM**.
2. In the navigation pane on the left, click **Roles**.
3. Click **Create role** button.
4. For **Select type of trusted entity** choose the **EC2** service and click **Next: Permissions** button.
5. In **Search** box paste **AmazonEC2RoleforSSM**, and select a policy.
6. Click **Next:Tags** and **Next: Review**.
7. Insert the **Role name**: **StudentX-SSMRole**.
8. Click **Create role**.

## Task 2: Create new EC2 instance

In this task you will spin up a new EC2 machine without SSH key.

9. On the **Services** menu, click **EC2**.
10. Click **Launch** **Instance**.
11. Select **Amazon Linux AMI.**
12. On the **Choose an Instance Type** page, select the **t2.micro** instance type.
13. Click **Next: Configure Instance Details**.
14. On the **Configure Instance Details** page select your VPC and your public subnet and enable public IP.
15. Additionally set up IAM Role that you created in task 1.
16. Click **Next: Add Storage**.
17. Click **Next: Add Tags** to accept the default storage device configuration.
18. On the **Add Tags** page, click **Add Tag,** type a **Name** for a Key box and  studentX_NoKey in the Value  box.
19. Click **Next: Configure Security Group**.
20. For **Assign a security group**, select a WebServers Security Group you created in LAB2-VPC.
21. Click **Review and Launch**.
22. Review your choices, and then click **Launch**.
23. Select **Proceed without a key pair** and check Acknowledge box.
24. On the status page, which notifies you that your instances are launching, click **View Instances**.
25. Wait unitl install will be ready.

## Task 3: Test EC2 SSM.

26. On the **Services** menu, click **EC2**.
27. Scroll down and in the navigation pane on the left, click **Run Command**.
28. Click **Run Command** button.
29. For **Command document**, choose **AWS-RunShellScript**.
30. For **Target instances**, choose the instance you created. If you don't see the instance, verify that you are currently in the same region as the instance you created. Also verify that you configured the IAM role and trust policies as described earlier.
31. For **Commands**, type **ps aux**.
32. For **Comment**, type StudentX-ps.
33. Choose **Run** to execute the command. Run Command displays a status screen. Choose **View result**.
34. To view the output, choose the command invocation for the command, choose the **Output** tab, and then choose **View Output**.

## Task 4: Retrive a public key from you key pair.

You need you public key that needs to be imported into orphaned VM.

35. On your local Linux or Mac computer, you can use the **ssh-keygen** command to retrieve the public key for your key pair. 

```she
ssh-keygen -y -f /path_to_key_pair/my-key-pair.pem
```

The command returns the public key. For example:

```she
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQClKsfkNkuSevGj3eYhCe53pcjqP3maAhDFcvBS7O6V
hz2ItxCih+PnDSUaw+WNQn/mZphTk/a/gU8jEzoOWbkM4yxyb/wB96xbiFveSFJuOp/d6RJhJOI0iBXrlsLnBItntckiJ7FbtxJMXLvvwJryDUilBMTjYtwB+QhYXUMOzce5Pjz5/i8SeJtjnV3iAoG/cQk+0FzZqaeJAAHco+CY/5WrUBkrHmFJr6HcXkvJdWPkYQS3xqC0+FmUZofz221CBt5IMucxXPkX4rWi+z7wB3RbBQoQzd8v7yeb7OzlPnWOyN0qFU0XA246RA8QFYiCNYwI3f05p6KLxEXAMPLE
```

36. (Optionally) You can retrive a key from your other instance (with the same key) through its instance metadata:

```shell
[ec2-user ~]$ curl http://169.254.169.254/latest/meta-data/public-keys/0/openssh-key
```

## Task 5: Use SSM to import a public key.

During this task you will use SSM to import a public key to the virtual machine. After that you will try to connect.

37. To import a key repeat a steps 26-30.
38. For **Comment**, paste the following command

```shell
echo 'key name' >> /home/ec2-user/.ssh/authorized_keys
```

For example:

```she
echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCwfPwfUU9KjUYpuia6wcAsXrbetJOS/T7yOvJOukK/78CQT4xOUteHi36w4KOxzanDsVYg/jdU2RoXLZ5cof05TJKU7QgD3Ahhnm+D2g97wkjeBz34fjyqUJlivMlmpxt1zzSMXQh+PYHXC1d4bhJFE0QY4jMGq4fNbg+VBjIf7gYVoj1DB+DMxpGlz8JtEBmpYl6bhp6gqe9916laMEOh6Ja9RJJCvmWCm0PSGg2aeKRCdDjzGLiRZEGGva4hixRJ5/Ob69h4bsJuVCYf6FS7tJEfaZiYgcuVWuxkYcNO7VPQqumXUvuotFTL/kehBRPkGsnW21fsi9lAVwb4s7Qt klucz' >> /home/ec2-user/.ssh/authorized_keys
```

39. For **Comment**, type StudentX-addKey.
40. Choose **Run** to execute the command.

Check if the key has been correctly imported.

41. Repeat a steps 26-30.
42. For **Comment**, paste the following command:

```she
cat /home/ec2-user/.ssh/authorized_keys
```

43. For **Comment**, type StudentX-check.
44. Choose **Run** to execute the command. Run Command displays a status screen. Choose **View result**.
45. To view the output, choose the command invocation for the command, choose the **Output** tab, and then choose **View Output**.
46. If the key is correctly imported try to connect over SSH.

## END LAB

This is the end of the lab. Terminate instance your created in this LAB (studentX_NoKey).

56. In AWS console select your **studentX_02** EC2 instance.
57. Click **Action** button and select **Instance state** -> **Terminate.**
58. Click **Yes, Terminate.**

<br><br>

<center><p>&copy; 2019 Chmurowisko Sp. z o.o.<p></center>
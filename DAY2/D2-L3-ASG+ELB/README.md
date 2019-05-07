<img src="../../img/logo.png" alt="Chmurowisko logo" width="200" align="right">
<br><br>
<br><br>
<br><br>

# Build your first Amazon EC2 Auto Scaling

## LAB Overview

#### This lab shows you how to use Auto Scaling to automatically launch Amazon EC2 instances in response to conditions that you specify. You will then test Auto Scaling by terminating a running instance and watching while Auto Scaling automatically creates a replacement instance.

## Task 1: Creating an AMI from your Instance
First you need to create an image (AMI) from your EC2 instance.

1. In the AWS Management Console, on the **Services** menu, click **EC2**.
2. Select your instance: **stundetX_01** (where X is your login number). 
3. On the **Actions** menu, click **Image** and then **Create Image**. 
4. For **Image name** box, enter **studentX_AMI**. 
5. In the **Image description** box, type your name. 
6. Click **Create Image**. 
7. In the navigation pane on the left, click **AMIs**. 
8. Locate your AMI and wait until Status will change to **available**. 

## Task 2: Create Elastic Load Balancer

For this lab, you will be creating a simple HTTP load balancer. This load balancer will be used with auto
scaling group.

9. In the left navigation pane, click **Load Balancers**. 
10. Click **Create Load Balancer**. 
11. In **Select load balancer type** page, for **Classic Load Balancer**, click **Create**. 
12. In the **Load Balancer name** box, type a new name **studentX-ELB**. 
13. In the **Create LB Inside** box, select your VPC. 
14. Check **Enable advanced VPC configuration** checkmark.
15. In the **Listener Configuration:** set parameters:
    * **Load Balancer Protocol**: HTTP
    * **Load Balancer Port**: 80
    * **Instance Protocol**: HTTP
    * **Instance Port**: 80
16. In **Select Subnets** configuration look for **Available subnets** and click a **+** button for your all Public subnets. 
17. Click **Next: Assign Security Groups**. 
18. For **Assign a security group**, make sure that **Create a new security group** is selected. 
19. In the **Security group name** box, type a name **studentX-ELB-SG**. 
20. In the **Description** box, type **studentX SG for ELB**. 
21. Create a rule for **HTTP** and **custom source 0.0.0.0/0** 
22. Click **Next: Configure Security Settings** and **Next: Configure Health Check**. 
23. For Health Check settings provide following configuration: 
    * **Ping Protocol**: HTTP
    * **Ping Port**: 80
    * **Ping Path**: /index.php
    * **Response Timeout**: 5 seconds
    * **Interval**: 7 seconds
    * **Unhealthy threshold**: 2
    * **Healthy threshold**: 2
24. Click **Next: Add EC2 Instances**.

At this time you don’t select any EC2 instances, because they will configured by Auto Scaling Group.

24. Leave default and click **Next: Add Tags.**
25. Leave default and click **Review and Create**.
26. Click **Create**.

## Task 3: Create a Launch Configuration

A launch configuration specifies the type of EC2 instance that Auto Scaling launches for you. You create the
launch configuration by specifying information such as the Amazon Machine Image (AMI) ID to use for
launching the EC2 instance, the instance type, key pairs, security groups, and block device mappings,
among other configuration settings.

27. In the left navigation pane, click **Launch Configurations** (you might need to scroll down to find it).

29. Click **Create launch configuration**.

You will be asked to select an Amazon Machine Image (AMI), which is a template for the root volume of the
instance and can contain an operating system, an application server and applications. You use an AMI to
launch an instance, which is a copy of the AMI running as a virtual server in the cloud. In this LAB you will
use an AMI created in previous task.

30. In the left navigation pane, click **My AMIs**.
31. Look for an AMI you created in task 1 and press **Select**.

You are next asked to choose an **Instance Type**.
When you launch an instance, the **instance type** determines the hardware allocated to your instance.

32. Confirm that the **t2.micro** instance type is selected.
33. Click **Next: Configure details**.
34. For **Name**, type: **studentX_LC**.
35. For **Monitoring** select **Enable CloudWatch detailed monitoring**.
36. Scroll down and expand **Advanced Details**.
37. For **IP Address Type** select **Assign a public IP address to every instance.**
38. Click **Next: Add Storage** and leave default option.
39. Click **Next: Configure Security Group**.
40. Choose **Select an existing security group** and select your security group for WebServers.
41. Click **Review** and then **Create launch configuration**.
42. Select a your key and check Acknowledge box and **Create launch configuration**.

Your launch configuration has now been created and you will be prompted to create an Auto Scaling group.

## Task 4: Create an Auto Scaling Group

The Launch Configuration defines what should be launched, while the Auto Scaling group defines how
many instances to launch and where to launch them within your network.

40. On the Configure Auto Scaling group details page, configure:
    * **Group name:** studentX_ASG
    *  **Group size:** Start with 1 instance 
    * **Network:** Select your VPC 
    * **Subnet:** Select your all Public subnets
41. Scroll down to **Advanced Details** and expand this section.
42. In **Load Balancing** select box, **Receive traffic from one or more load balancers**.
43. In **Classic Load Balancers** box select your load balancer created in task 2.
44. In **Health Check Type** select **ELB**.
45. In **Monitoring** select **Enable CloudWatch detailed monitoring**.
46. Click **Next: Configure Scaling policies**.
47. Leave **Keep this group at its initial size** option selected.
48. Click **Review** and **Create Auto Scaling group**.
49. Click **Close**.

Auto Scaling will launch an Amazon EC2 instance and will maintain the Auto Scaling group at that quantity.

## Task 5: Verify your Auto Scaling group

Now that you have created your Auto Scaling group, you can verify that the group has launched your EC2
instance.

49.  On the Auto Scaling Groups page, select the Auto Scaling group that you just created.

Examine the **Details** tab at the bottom of the page to view information about the Auto Scaling group.

50. Click the **Activity History** tab.

The Status column contains the current status of your instance. When your instance is launching, the status
column shows In progress. The status changes to Successful once the instance is launched. You can click the
refresh button to see the current status of your instance.

51. Click the **Instances** tab.

The Lifecycle column contains the state of your newly launched instance. You can see that your Auto
Scaling group has launched your EC2 instance and it is in the *InService* lifecycle state. The Health Status
column shows the result of the EC2 instance health check on your instance.

## Task 6: Verify your Load Balancer

Now when the Auto Scaling Group is created and EC2 machine is operational, you can check the status of
your Load Balancer.

52. In the left navigation pane, click **Load Balancers**.
53. Select the load balancer that you just created, click the **Instances** tab, and wait for the status of Instance to change to *InService*. To refresh the status, click the circular arrow icon in the upper-right. 
54. When the status of Instance is *InService*, click the **Description** tab. 
55. Copy the **DNS name** value to your Clipboard. 

Load balancers can span Availability Zones, and they also scale elastically as needed to handle demand. Therefore, you should always access a load balancer by DNS hostname, and not by IP address. A load balancer may have multiple IP addresses associated with its DNS hostname.

56. Open a new browser window, paste the DNS Name value into the address bar, and press ENTER. You should get a view of your application.
57. Return to the AWS Management Console and, on the **Services** menu, click **CloudWatch**.
58. In the navigation pane, click **Metrics** and in the **All metrics** tab, click **ELB**.
59. Scroll up and down to select the metric or metrics you would like to view.

Load balancing metrics include latency, request count, and healthy and unhealthy host counts. Metrics are reported as they are encountered and can take several minutes to show up in CloudWatch.

## Task 7: Increase instance number

This time you will reconfigure Auto Scaling group to maintain two EC2 instances.

60. In the AWS Management Console, on the **Services** menu, click **EC2**.
61. In the left navigation pane, click **Auto Scaling Groups**.
62. Select your Auto Scaling Group and press **Action** in **Edit** tab.
63. In **Desired** and **Max** box insert 2 and click **Save**.

If you scale you group manually you have to configure this parameters of Minimum, Desired and Maximum number of instances that Auto Scaling Group should have at any time.

64. Observe **Activity history** and **Instances** tab for any changes.
65. When both instances in **Instances** tab will be in *InService* go back to your Load Balancer.
66. Select your load balancer and check in **Instances** tab if both servers are in *InService*.
67. When the status of both Instances is *InService*, click the **Description** tab.
68. Copy the DNS name value to your Clipboard.
69. Open a new browser window, paste the DNS Name value into the address bar, and press ENTER.
70. Press Refresh button few times.

By default Load Balancer use Round Robin to distribute a new connection to backend servers. It is possible to implement Sticky Sessions, but it’s not recommended option for auto scaled environments. Do you know why?

71. After all, change a configuration of an Auto Scaling Group to Max 3 instances.

## Task 8: Test Auto Scaling

Try the following experiment to learn more about Auto Scaling. The Desired size for your Auto Scaling group is 2 instances. Therefore, if you terminate the running instance, Auto Scaling must launch a new instance to replace it.

72. In the **Instances** tab, click Instance ID.

You will be taken to the Amazon EC2 console the Instances page.

73. Click **Actions**, select Instance State, and then click **Terminate**. When prompted for confirmation, click **Yes, Terminate**.
The instance will change to shutting-down.

74. In the left navigation pane, select **Auto Scaling Groups** and then select our AS group and the Instances tab.

You will see the initial instance status as Terminating. Soon thereafter you will see a new instance appear with a status of Pending or InService. The default cooldown for the Auto Scaling group is 300 seconds (5 minutes), so it may take about 5 minutes until you see the scaling activity

75. Return to the **Activity History** tab.

All scaling activities are logged here. After the scaling activity starts. Click the triangles to view entries for the launch and termination of the first instance and then an entry for the launch of the new instance.

76. When a new instance will be in *InService*, check if your application is running.
77. Open a new browser window, paste the ELB’s DNS Name value into the address bar, and press ENTER.


## Task 9: Scaling Policies for AutoScaling

This time you will use ScalingPolicies to scale your application based on CPU utilization.

78. Go back yo your AutoScaling configuration. 
79. Click the **Scaling Policies** tab.
80. Click **Add policy**.
81. Click **Create a simple scaling policy**.
82. Set a name: studentX_UP
83. Click **Create new alarm**
84. Create a policy for Average CPU Utilization is >= 30%.
85. For at least **1** consecutive period of  **1 minute**.
86. Name of the alarm: studentX_alarmUP
87. Click Create Alarm
88. For Take the action select **Add 1 instances**.
89. For And then wait set **30 seconds**.
90. Click **Create**.

Add a second Policy studentX_DOWN for Average CPU Utilization < 20%, alarm name studentX_alarmDOWN and take action of **Remove 1 Instances** with wait time **30 seconds.**

90. Login over SSH into two instances created by AutoScaling group. 
91. On both instances install a test tool:

`` sudo yum install stress -y ``

92. On both instances run a stress command: 

``
sudo stress --cpu 100 
``

93. Observe Activity History and Instances tabs for any changes.

When the cpu utilisation will go above the created alarm, a new instance will be added. 

94. Stop a stress command by pressing CTRL+C.
95. Observe Activity History and Instances tabs for any changes.


## END YOUR LAB

Follow these steps to close the console, end your lab.

96. In the AWS Management Console, on the **Services menu**, click **EC2**. 
97. In the left navigation pane, click **Auto Scaling Groups**.
98. Select your AS group and click **Actions**, select **Delete**, click **Yes, Delete**. 
99. In the left navigation pane, click **Launch Configurations*.
100. Select your configuration and click **Actions**, select **Delete launch configuration**, click **Yes, Delete**.
101. In the left navigation pane, click **Load Balancers**.
102. Select your ELB and click **Actions**, select **Delete**, click **Yes, Delete**.

<br><br>

<center><p>&copy; 2019 Chmurowisko Sp. z o.o.<p></center>


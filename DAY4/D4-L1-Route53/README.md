<img src="../../img/logo.png" alt="Chmurowisko logo" width="200" align="right">
<br><br>
<br><br>
<br><br>

# Introduction to Amazon Route 53

## LAB Overview

#### This lab will give you a basic understanding of Amazon Route 53 and will demonstrate the steps required to get started with Route 53.

## Task 1: Create DNS Records For Amazon EC2 Instances
In this section, you will create a record in the hosted zone that points to an EC2 instance.

1. On the **Services** menu, click **EC2**.
2. In the **Description** tab of your studentX_01 instance, copy the **Public IPs** value to your text editor.
3. Return to the **Route53** Console. (Services menu > Route53).
4. In the navigation pane on the left, click **Hosted zones**.
5. Click the domain name: **becomecloud.ninja**.
6. In the **Create Record Set** window on the right, configure the following:
   * **Name**: studentX 
   * **Type**: A-IPv4 address 
   * **Alias**: No 
   * **TTL (Seconds)**: 60 
   * **Value**: Paste the Public IP value that you copied to your text editor 
   * **Routing Policy**: Simple 
   * Click **Create**

7.  Paste the domain name into a new browser tab and press **Enter**.

## Task 2: Add a Route 53 Health Check to an Amazon EC2 Web Server

In this section, you will add a Route 53 Health Check to an EC2 Web server. Route 53 health checks monitor
the health and performance of your web applications, web servers, and other resources. In case your EC2
instance is terminated or becomes unavailable for any reason, having a health check in place allows you to
use DNS Failover and alarms to ensure that your website or application is always reachable by your end
users. It also ensures that you are notified about its current state.

8. In the **Route 53 Management Console**, in the navigation pane on the left, click **Health checks**.
9. Click **Create health check**.
10. For **Step 1: Configure health check**, configure the following:
    * **Name:** StudentX_HC
    * **What to monitor:** Endpoint
    * **Specify endpoint by**: IP address
    * **Protocol**: HTTP
    * **IP address**: Paste the Public IP value you copied to your text editor
    * **Port**: 80
    * Click **Next**
11. For **Step 2: Get notified when health check fails**, configure the following:
    * **Create alarm**: Yes
    * **Send notification to**: New SNS topic
    * **Topic name**: StudentX_HCFail
    * **Recipient email addresses**: Enter your email address.
    * Click **Create health check**.
12. Check your email and **Confirm subscription**.

## Task 3: Configure a DNS Failover to an Amazon S3 Static Website

In this section, you will revise the simple DNS record that you initially pointed to the EC2 server and turn it
into a Primary Failover record. You will also create a Secondary Failover record pointing to an Amazon S3
static website.

In your own account and configurations, you can use any endpoint as you backup. In this lab, you use an
Amazon S3 static website feature for a simple, reliable, and low-cost way to deploy a backup website.

13. In the **Route 53 Management Console**, click **Hosted zones**.
14. Click your domain name.
15. Find and select your dns entry.
16. In the **Edit Record Set** window on the right, configure the following:
    * **Routing Policy**: Failover
    * **Failover Record Type**: Primary
    * **Associate with Health Check**: Yes
    * **Health Check to Associate**: StudentX_HC
    * Click **Save Record Set**

Now that your primary endpoint is configured, you can also configure your secondary or backup endpoint. 
To begin, you need to know what that endpoint is. 

17. On the **Services** menu, click **S3**. 
18. Click +Create bucket button. 
19. Paste the name: **studentX.becomecloud.ninja** 
20. Select Region: **EU (Ireland)** 
21. Click **Create.** 
22. Click the **Properties** tab. 
23. Click **Static website hosting**. 
24. Select **Use this bucket to host a website**, and set **index.html** for index and error document. 
25. Click **Save**. 
26. Select **Static website hosting** again, and copy the **Endpoint**: address to your text editor. 
27. Back to **Overview** tab and select **Upload**. 
28. Select **[index.html](index.html)** file from laboratory materials. 
29. Click **Next**. 
30. In **Manage public permissions** select **Grant public read access to this object(s)** and click **Upload**. 
31. Make sure you have public access on your S3 bucket. 
32. Go back to the **Route 53 Management Console**. (Services menu > Route 53) 
33. Click **Hosted zones** and click your domain name**.** 
34. Click **Create Record Set**. 
35. In the **Create Record Set** window on the right, configure the following: 
    * **Name**: studentX 
    * **Type**: A-IPv4 address 
    * **Alias**: Yes 
    * **Alias Target:** select the S3 website Endpoint (e.g. s3-website) - If you don't see the target, repeat the step above for creating a record set. 
    * **Routing Policy**: Failover 
    * **Failover Record Type**: Secondary 
    * Click **Create**. 

Now you have a health check that is checking your primary endpoint, and a secondary endpoint in case the primary endpoint becomes unreachable. 

36. In the navigation pane on the left, click **Health checks**. 
37. The status should be **Healthy**.

## Task 4: Test the Health Check and Failover

In this section, you will stop your EC2 instance and cause your health check to return an Unhealthy status.
Based on this status, your DNS configuration will failover to the secondary endpoint.

38. In **AWS Management Console**, on the **Services** menu, click **EC2**. 
39. In the navigation pane on the left, click **Instances**.
40. Find and select your instance.
41. In **Actions** menu, click **Instance State** > **Stop**. 
42. Return to the **Route 53 Management Console** (Services menu > Route 53). 
43. In the navigation menu on the left, click **Health checks**.
44. Select health check you created.
45. Click the **Monitoring** tab. 
46. Click the refresh every few seconds till the **Status** displays *Unhealthy*. 
47. Open the url of your website once again. 

You should get a content of the static site hosted on the S3.



## Task 5: Weighted routing

In this section, you will create weighted dns routing to your endpoints.

48. Power on your EC2 Instance and make sure that an application is running. 

49. Return to the **Route 53 Management Console** (Services menu > Route 53). 

50. In the **Route 53 Management Console**, click **Hosted zones**. 

51. Click the domain name: **becomecloud.ninja**. 

52. Find your DNS entries created in task 3. 

53. For both records change the Routing Policy to **Weighted** and set **Weight:** 50%. 

54. Save both records and try to test the configuration in web browser (eventually clean DNS cache on your 

    computer). 

## END LAB

Congratulations! You have now successfully completed this laboratory.

<br><br>

<center><p>&copy; 2019 Chmurowisko Sp. z o.o.<p></center>
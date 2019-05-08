<img src="../../img/logo.png" alt="Chmurowisko logo" width="200" align="right">
<br><br>
<br><br>
<br><br>

# Introduction to Amazon Aurora

## LAB Overview

#### This lab introduces you to Amazon Aurora using the AWS Management Console.

## Task 1: Create new DB Subnet Group
DB subnet group defines which subnets and IP ranges the DB instance can use in the VPC you selected. During Aurora instance creation is possible to let a wizard create a subnet group automatically. But for our lab, we want to have a full control of which subnets will be selected for Aurora cluster.

1. In the AWS Management Console, on the **Services** menu, click **RDS**.
2. In the left navigation pane, click **Subnet groups**.
3. Click **Create DB Subnet Group**.
4. On **Create DB subnet group**, step configure the following:

* **Name**: StudentX-DBSG
* **Description**: Your name
* **VPC**: Select your VPC created in LAB-VPC
* Click **Add all the subnets related to this VPC**

It is the fastest way, select all and then remove unnecessary. If you followed VPC-LAB instructions correctly,
fours subnet should appear in **Subnets in this subnet group**. Now you need to remove the public subnets
by clicking **Remove** button. You should remove 10.X.0.0/24 and 10.X.1.0/24 and leave 10.X.10.0/24 and
10.X.11.0/24.

* Click **Remove** button for 10.X.0.0/24 (where X indicates your student number)
* Click **Remove** button for 10.X.1.0/24

5. Click **Create**.

## Task 2: Create a Aurora Cluster

In this task, you will create an Amazon Aurora cluster

6. In the left navigation pane, click **Databases**.
7. Click **Create database** button.
8. On **Create database**, select
   * Engine type: **Amazon Aurora**
   * Edition: **Amazon Aurora with MySQL compatibility**
   * Version: **Leave suggested option**
   * Database Location: **Regional**
   * Database features: **One writer and multiple readers**
   * Template: **Production**
   * DB cluster identifier: **StudentX-cluster**
   * DB instance performance type: **Burstable**
   * DB instance size: **db.t2.small**
   * Multi-AZ deployment: **Create an Aurora Replica/Reader node in a different AZ (recommended for scaled availability)**
   * Virtual Private Cloud (VPC): **Select your VPC**
   * Expand **Additional connectivity configuration**
   * Subnet group: **Select group created in Task 1**
   * VPC security group: **Choose existing**
   * Existing VPC security groups: 
     * Select: **StudentX_DB**
     * Deselect: **default**
   * Expand **Addotional configuration**
   * Initial database name: **studentXdb**
   * Delection protection: **Unselect**
9. Click **Create database**.
10. Wait until **Successfully created database studentX-mysql.** green information appear.
11. Click **View credential details**.
12. Copy **Master username**, **Master password** and **Endpoint** values to the notepad.

This is the only time you will be able to view this password. However you can modify your database to create a new password at any time.

## Task 3: Test your DB cluster

You will now connect to Aurora database from your EC2 server. 

13. Connect to your  laboratory EC2 instance over SSH.
14. Go you website folder: 

```bash
cd /var/www/html
```

15. Create a new file **auroradb.php**:

```bash
sudo nano auroradb.php
```



16. Paste the following code ( code of the file [db.php](db.php))

```php
<?php
$servername = "enter your ENDPOINT";
$database = "studentXdb";
$username = "admin";
$password = "enter master password";
// Create connection
$conn = mysqli_connect($servername, $username, $password, $database);
// Check connection
if ($conn->connect_error) {
   die("Connection failed: " . $conn->connect_error);
}
  echo "<h1>Great!</h1><br>Connected successfully to:<b> $servername</b>";
?>
```

17. Provide correct values for: **servername**, **database** and **password**
18. Press CTRL+O, ENTER to save your document. 
19. Press CTRL+X to exit the Nano editor.
20. Open a new browser window, and then paste the public DNS value into the address bar and add tested.php.

Example: http://ec2-34-240-160-241.eu-west-1.compute.amazonaws.com/auroradb.php

## Task 4: Test your DB instance with cli (optional)

21. Connect to your  laboratory EC2 instance over SSH.

22. Install mysql tool:

 ```shell
 yum install mysql -y
 ```

23. Connect to the database:

```bash
mysql -u admin -p -h enter_db_entpoint
```

24. List databases:

```my
show databases;
```

## Task 5: Test failover

It is possible to manually switch cluster node roles. Check the following steps. 

25. Find your database cluster end expand it.
29. Select you **Reader** node.
30. Click **Actions** button and select **Failover**
31. Click **Failover** to confirm.
32. Click refresh button and verify changes. 

## END LAB

This is the end of this lab. Go over following steps to remove database cluster.

30. In the AWS Management Console, on the **Services** menu, click **RDS**.
34. In the left navigation pane, click **Databases**.
35. Find and expand your cluster.
36. Click on **Reader** node, select **Actions** button and choose **Delete**
37. Confirm by typing **delete me** and click **Delete**
38. Do the same with **Writer** node.
39. Skip final snapshot.

<br><br>

<center><p>&copy; 2019 Chmurowisko Sp. z o.o.<p></center>
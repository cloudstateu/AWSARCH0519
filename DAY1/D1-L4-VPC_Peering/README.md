<img src="../../img/logo.png" alt="Chmurowisko logo" width="200" align="right">
<br><br>
<br><br>
<br><br>

# Create VPC Peering Connection

## LAB Overview

#### In this Lab, you will create a VPC peering between two VPCs. You will work in pair with another student. Peering connection needs two side action: Request connection and Accept. One student will Request connection and second will accept.

## Task 1: Creating a VPC Peering Connection (Requestor)
In this task one student (Requestor) will create VPC Peering connection. 

1. In the **AWS Management Console**, on the **Services** menu, click **VPC**.
2. In the navigation pane on the left, click **Peering Connections**.
3. Click **Create Peering Connection**.
4. In the **Create Peering Connection** window set the following:
   * **Peering connection name tag**: Student(your_number)_Student(neighbor_number)
   * **VPC (Requester)**: Select your VPC
   * **Account**: My account
   * **Region**: This region
   * **VPC (Acepter)**: Neighbor's VPC
5. Click **Create Peering Connection** and **OK**.

## Task 2: Accept reguest for peering connection (Accepter)

Request for peering connection is made only once. After creation another side needs to accept request.

6. In the **AWS Management Console**, on the **Services** menu, click **VPC**.
7. In the navigation pane on the left, click **Peering Connections**.
8. Look for peering connection created in Task 1 with a status **Pending Acceptance**.
9. Select and click **Actions** button.
10. Click **Accept Request**.
11. Confirm by clicking **Yes, Accept** and **Close**.

At this moment a peering connection is established. But peered VPC doesn't now how to route traffic to the other end. Both sides, Requestor and Accepter need to add proper entry to the routing tables.



## Task 3: Edit Route Table (Requester and Accepter)

12. In the **AWS Management Console**, on the **Services** menu, click **VPC**.
13. In the navigation pane on the left, click **Route Tables**.
14. Find and select your routing table correlated with Public Subnets: **StudentX_RTP**.
15. Switch to the **Routes** tab and click **Edit routes**.
16. Click **Add route**.
17. Click the **Destination** field and enter the CIDR block of VPC you peered with (Ex. 10.2.0.0/16).
18. Click the **Target** field.
19. Chose **Peering Connection** and select connection created in previous steps.
20. Click **Save routes** and **Close**.

You have now fully configured peering connection with proper routing entries. Now you can test it by establish a connection between virtual machines using private ip addresses.

 

## END LAB

<br><br>

<center><p>&copy; 2019 Chmurowisko Sp. z o.o.<p></center>
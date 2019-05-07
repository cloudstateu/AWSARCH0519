  <img src="../../img/logo.png" alt="Chmurowisko logo" width="200" align="right">
  <br><br>
  <br><br>
  <br><br>


# ECS Scaling

## LAB Overview

#### This lab will demonstrate:
* Creating service using ECS
* Autoscaling ECS service 



## Task 1: Create an ECS Cluster

In this task you will create ECS Cluster.

1. In the AWS Management Console, on the **Services** menu, click **ECS**.
2. Click **Create Cluster**.
3. Choose "EC2 Linux + Networking" option.
4. Click **Next step**.
5. Enter a name for your cluster, e.g. "Student-X-Cluster".
6. Choose "On-demand instance".
7. Choose "t3.micro" as your instance type.
8. Set number of instances to 1.
9. Leave the rest unchanged and click **Create**.

Wait until the cluster is ready.

10. Click **View cluster"
11. Click **ECS Instances** and check, if there is an instance active.



## Task 2: Prepare a Task definition

It this task you'll prepare a task definition for the service.

1. Click **Task definitions**.
2. Click **Create new Task Definition**.
3. Choose "EC2" and click **Next step**.
4. Enter a name for your task definition, e.g. "Student-X-TaskDefinition"
5. In the "Task size" area enter 256 for "Task memory" and 256 for "Task CPU".
6. Click **Add container**.
7. Enter a name for your container, e.g. "Student-X-Container".
8. Paste "jfusterm/stress:latest" as the "Image". 
9. Set "Memory Limits" to "Soft limit" and 128.
10. In the "ENVIRONMENT" area set Command to "--cpu, 8". Do not copy/paste quotation marks.
11. Click **Add**.
12. Click **Create**.



## Task 3: Setting up the service

In this task, you will set up a service with *stress* command run inside.


1. Click **Clusters**.
2. Find your cluster and click on its name.
3. Select **Services**.
4. Click **Create**.
5. As a "Launch type" select "EC2".
6. Set your task definition.
7. Select your cluster.
8. Enter a name for the service, e.g. "Student-X-Service".
9. Set "service type" to "Replica".
10. Set "Number of tasks" to 2.
11. Click **Next step**.
12. Set "Load balancer" to "None".
13. Click **Next step**.
14. Set "Service Auto Scaling" to "Do not adjust the srvice's desired count".
15. Click **Next step**.
16. Review setting and click **Create service**.
17. Click **View Service**.

Now you should have two instances of the task running.



## Task 4: Turning on Auto Scaling

In this task, you will set up the auto scaling for the service.


1. Click **Clusters**.
2. Find your cluster and click on its name.
3. Select **Services**.
4. Find your service and click on its name.
5. Click **Update**.
6. Click **Next step**.
7. Click **Next step**.
8. On the "Service Auto Scaling" part set "Service Auto Scaling" to "Configure Service Auto Scaling to adjust your service’s desired count".
9. Set "Minimum number of tasks" to 2.
10. Set "Desired number of tasks" to 2.
11. Set "Maximum number of tasks" to 12.
12. Click **Add scaling policy**.
13. Set "Scaling policy type" to "Step scaling".
14. Enter a name for the policy, e.g. "Student-X-ScaleOut-Policy".
15. Select "Create new alarm".
16. Enter a name for the alarm, e.g. "Student-X-ScaleOut-Alarm".
17. Select "CPU Utilization" for "ECS service metric".
18. Set "Alarm threshold" to "Average" of CPUUtilization ">=" and value to 40 for 1 consecutove period of "5 minutes". 
19. Set "Scaling action" to "Add" 6 tasks.
20. Click **Save**.
21. Click **Save**.
22. Click **Next step**.
23. Click **Update Service**.
24. Click **View service**.
25. Click **Events** and wait for new autoscaling events. Refresh the Event table from time to time. Observer the amount of Desired and Running tasks.

If you want, you can open **CloudWatch** service and look into the alram created a moment ago. 

After several minutes there should be 7 tasks running on your cluster. Check "Desired count", it should be set to 8 tasks.

26. Click **your cluster name**.
27. Click **Metrics** and look at "CpuUtilization".



## Task 5: Adding EC2 instance to the cluster

In this task, you will spin up a new EC2 instance into the cluster.


1. Click **Clusters**.
2. Find your cluster and click on its name.
3. Click **ECS Instances**.
4. Click **Scale ECS Instances".
5. Enter 2 as "Desired number of instances".
6. Click **Scale**.

Wait until a new instance is active.

7. Select **Services**.
8. Find your service and click on its name.
9. Check how hany task instances are running now.

## END LAB

This is the end of this laboratory. 

Follow these steps to close the console, end your lab, and delete the table.

1. In the AWS Management Console, on the **Services** menu, click **ECS**.
2. Click **Clusters**.
3. Find your cluster and click on its name.
4. Click **Delete Cluster**.
5. Click **Delete**.

<br><br>

<center><p>&copy; 2019 Chmurowisko Sp. z o.o.<p></center>
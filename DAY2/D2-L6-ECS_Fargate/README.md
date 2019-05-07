<img src="../../img/logo.png" alt="Chmurowisko logo" width="200" align="right">
<br><br>
<br><br>
<br><br>

# Create container based application with AWS ECS Fargate

## LAB Overview

#### This lab leads you through the steps to run a simple Mario Bros game as website. You will use provided docker image and run it using Amazon ECS service.

## Task 1: Create ECS Cluster

In this step you will verify a content of the Amazon ECR.

1. On the **Services** menu, click **ECS**.
2. In the navigation pane on the left, click **Repositories**.

You should find there one repository called “mario”.

3. In the navigation pane on the left, click **Clusters**.
4. Click **Create cluster** button.

**Note:** You will find tree options. Two options with classic EC2 machines, where virtual machines will be created in ECS Cluster. Third option (Fargate) is a serverless approach.

5. Select option **Networking only (Powered by AWS Fargate)** and **Next step**.
6. Provide all informations: 
   * **Cluster name:** studentXcluster,
   * **Create VPC**: leave unselected.

7. Click **View cluster**.

## Task 2: Create a task definition

In this section, you will create and run task that will spin up our docker container with an application.

8. In the navigation pane on the left, click **Task Definitions**.
9. Then **Create new Task Definition**, select **FARGATE** and click **Next step**.
10. Provide all necessary information:

* **Task Definition Name:** StudentX_task
* **Task memory:** 1GB
* **Task CPU:** 0.5 vCPU

11. In **Container Definition** select **Add Container.**
12. Provide following information: 

* **Container name**: studentX_container
* **Image**: 094104221953.dkr.ecr.eu-west-1.amazonaws.com/mario
* **Port mappings:** 8080

13. Rest of the container configuration leave default and click **Add**. 
14. Under the task definition windows leave the rest of configuration default and click **Create**. 
15. Click **View task definition**. 

You can review the configuration. Eventually you can also specify the config in the form of json template.

## Task 3: Run a task

Almost all of the configuration is ready, now you can run your task and test the application.

16. In the navigation pane on the left, click **Clusters**. 
17. Select your cluster and switch to **Tasks** tab. 
18. Click **Run new Task** and provide the following configuration. 

* **Launch type:** Fargate
* **Task definition:** select your task created in previous task.
* **Cluster**: select your cluster 
* **Service name:** studentX_mario
* **Number of tasks:** 1
* **Cluster VPC:** use your vpc
* **Subnets:** select your Public subnets
* **Security groups**: make sure that port 8080 is opened
* Click **Auto Assign Public IP**

19. Leave the rest and click **Run Task**
20. Wait until the service will be in **RUNNING** state 
21. Click on your task and look for **Public IP** 
22. Open a new windows in web browser and paste the address with :8080 at the end. 

## END LAB

This is the end of the lab. You can remove an ECS cluster.







<br><br>

<center><p>&copy; 2019 Chmurowisko Sp. z o.o.<p></center>

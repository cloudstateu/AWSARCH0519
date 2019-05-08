<img src="../../img/logo.png" alt="Chmurowisko logo" width="200" align="right">
<br><br>
<br><br>
<br><br>

# Introduction to DynamoDB

## LAB Overview

#### In this tutorial, you create a DynamoDB table and use AWS SDK for Python (Boto 3) to write a simple programs to perform the following actions:

* Load sample data in JSON format.
* Perform create, read, update, and delete operations on the table.
* Run simple queries.

## Task 1: Create DynamoDB table
In this task you will create DynamoDB table and key needed to retrieve data.

1. In the AWS Management Console, on the **Services** menu, click **DynamoDB**.
2. Click **Create table**.
3. Enter a name for your table, e.g. "student-x-table".
4. Name your Primary key as **year** and set the type to **Number**.
5. Check **Add sort key**.
6. Name your Sort key as **title** and set the type to **String**.
7. Leave the rest as it and click **Create**.

Your DynamoDB table will be ready almost immediately.

## Task 2: Prepare your virtual machine.

8. Make sure you laboratory machine can connect to the DynamoDB Service.

In this case you must add IAM Role to the virtual machine with the policy that grant access to the DynamoDB Service. For this laboratory use IAM Policy **AmazonDynamoDBFullAccess**.

9. Connect to your  laboratory EC2 instance over SSH.
10. Perform a yum install update.

```bash
sudo yum update -y
```

11. Launch Python, and then use the **version** command to find what Python versions are installed.

```bash
python --version
```

12. Install Python 3.4, if it's not already installed.

```bash
sudo yum install python34 -y
```

13. Use the **which** command to confirm that the install was successful.

```bash
which python34 
/usr/bin/python3.4
```

**Use virtualenv to create the Python environment**

14. Create a directory to hold your virtualenv environments, and then use the **cd** command to make it your current directory. In the following example, the environments are stored in the **venv** directory, under the **ec2-user** directory.

```bash
[ec2-user ~]$ pwd
/home/ec2-user
[ec2-user ~]$ mkdir venv
[ec2-user ~]$ cd venv
[ec2-user ~]$ pwd
/home/ec2-user/venv
```

15. Use the **virtualenv** command to create the **python34** environment.

```bash
[ec2-user ~]$ virtualenv -p /usr/bin/python3.4 python34
Running virtualenv with interpreter /usr/bin/python3.4
Using base prefix '/usr'
New python executable in python34/bin/python3.4
Also creating executable in python34/bin/python
Installing setuptools, pip...done.
```

16. Activate the environment by using the **source** command on the **activate** file in the **bin** directory, which is under your project directory.

```bash
source python34/bin/activate
```

17. Use the **which** command to verify that you are now referencing the new environment.

```bash
[ec2-user ~]$ which python
~/venv/python34/bin/python # python34 is now the default
```

18. Use the **pip** command to install Boto 3 from within the **python34** environment.

```bash
pip install boto3
```

19. Run Python using the **python** executable.

```bash
[ec2-user ~]$ python
Python 3.4.3 (default, Apr 1 2015, 18:10:40)
[GCC 4.8.2 20140120 (Red Hat 4.8.2-16)] on linux
Type "help", "copyright", "credits" or "license" for more information.
```

## Task 3: Load Sample Data

In this step, you populate your table with sample data. This scenario uses a sample data file that contains information about a few thousand movies from the Internet Movie Database (IMDb). The movie data is in JSON format, as shown in the following example. For each movie, there is a `year`, a `title`, and a JSON map named `info`.

20. Download the sample data archive:

```bash
wget https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/samples/moviedata.zip
```

21. Extract the data file from the archive.

```bash
unzip moviedata.zip
```

22. Create a loaddata.py program:

```bash
nano loaddata.py
```

23. Paste the following code (or use a file [loaddata.py](load data.py)):

```python

#
#  Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
#  This file is licensed under the Apache License, Version 2.0 (the "License").
#  You may not use this file except in compliance with the License. A copy of
#  the License is located at
# 
#  http://aws.amazon.com/apache2.0/
# 
#  This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
#  CONDITIONS OF ANY KIND, either express or implied. See the License for the
#  specific language governing permissions and limitations under the License.
#
from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal

dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')

# Paste the correct name of the table
table = dynamodb.Table('studentX-table')

with open("moviedata.json") as json_file:
    movies = json.load(json_file, parse_float = decimal.Decimal)
    for movie in movies:
        year = int(movie['year'])
        title = movie['title']
        info = movie['info']

        print("Adding movie:", year, title)

        table.put_item(
           Item={
               'year': year,
               'title': title,
               'info': info,
            }
        )
```

24. Paste the correct table name.
25. Press CTRL+O, ENTER to save your document. 
26. Press CTRL+X to exit the Nano editor.
27. Load the data with the program (make sure you have **moviedata.json** in the same folder):

```bash
python loaddata.py
```

28. When the program will end go to AWS Console and check content of your DynamoDB table.

## Task 4: Create a new item

In this step, you add a new item to the your table.

29. Back to ssh session of your laboratory machine.
30. Create additem.py:

```bash
nano additem.py
```

31. Paste the following code (or use a file [additem.py](additem.py))

```python

#
#  Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
#  This file is licensed under the Apache License, Version 2.0 (the "License").
#  You may not use this file except in compliance with the License. A copy of
#  the License is located at
# 
#  http://aws.amazon.com/apache2.0/
# 
#  This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
#  CONDITIONS OF ANY KIND, either express or implied. See the License for the
#  specific language governing permissions and limitations under the License.
#
from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if abs(o) % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')

# Paste the correct name of the table
table = dynamodb.Table('studentX-table')

title = "The Big New Movie"
year = 2019

response = table.put_item(
   Item={
        'year': year,
        'title': title,
        'info': {
            'plot':"Nothing happens at all.",
            'rating': decimal.Decimal(0)
        }
    }
)

print("PutItem succeeded:")
print(json.dumps(response, indent=4, cls=DecimalEncoder))
```

32. Paste the correct table name.
31. Press CTRL+O, ENTER to save your document. 
32. Press CTRL+X to exit the Nano editor.
33. To run the program, type the following command:

```bash
python additem.py
```

## Task 5: Read an Item from table

You can use the `get_item` method to read the item from the table. You must specify the primary key values, so you can read any item from your table if you know its `year` and `title`.

36. Create readitem.py

```bash
nano readitem.py
```

37. Paste the following code (or use a file [readitem.py](readitem.py))

```python

#
#  Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
#  This file is licensed under the Apache License, Version 2.0 (the "License").
#  You may not use this file except in compliance with the License. A copy of
#  the License is located at
# 
#  http://aws.amazon.com/apache2.0/
# 
#  This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
#  CONDITIONS OF ANY KIND, either express or implied. See the License for the
#  specific language governing permissions and limitations under the License.
#
from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')

# Paste the correct name of the table
table = dynamodb.Table('studentX-table')

title = "The Big New Movie"
year = 2019

try:
    response = table.get_item(
        Key={
            'year': year,
            'title': title
        }
    )
except ClientError as e:
    print(e.response['Error']['Message'])
else:
    item = response['Item']
    print("GetItem succeeded:")
    print(json.dumps(item, indent=4, cls=DecimalEncoder))


```

38. Paste the correct table name.
37. Press CTRL+O, ENTER to save your document. 
38. Press CTRL+X to exit the Nano editor.
39. To run the program, type the following command:

```bash
python readitem.py
```

## Task 6: Update na item

You can use the `update_item` method to modify an existing item. You can update values of existing attributes, add new attributes, or remove attributes.

In this example, you perform the following updates:

- Change the value of the existing attributes (`rating`, `plot`). 
- Add a new list attribute (`actors`) to the existing `info` map.

42. Create updateitem.py

```bash
nano updateitem.py
```

43. Paste the following code (or use a file [updateitem.py](updateitem.py))

```python

#
#  Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
#  This file is licensed under the Apache License, Version 2.0 (the "License").
#  You may not use this file except in compliance with the License. A copy of
#  the License is located at
# 
#  http://aws.amazon.com/apache2.0/
# 
#  This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
#  CONDITIONS OF ANY KIND, either express or implied. See the License for the
#  specific language governing permissions and limitations under the License.
#
from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')

# Paste the correct name of the table
table = dynamodb.Table('studentX-table')

title = "The Big New Movie"
year = 2019

response = table.update_item(
    Key={
        'year': year,
        'title': title
    },
    UpdateExpression="set info.rating = :r, info.plot=:p, info.actors=:a",
    ExpressionAttributeValues={
        ':r': decimal.Decimal(5.5),
        ':p': "Everything happens all at once.",
        ':a': ["Larry", "Moe", "Curly"]
    },
    ReturnValues="UPDATED_NEW"
)

print("UpdateItem succeeded:")
print(json.dumps(response, indent=4, cls=DecimalEncoder))
```

44. Paste the correct table name.
43. Press CTRL+O, ENTER to save your document. 
44. Press CTRL+X to exit the Nano editor.
45. To run the program, type the following command:

```bash
python updateitem.py
```

48. Next, check the chenges by running:

```bash
python readitem.py
```

## Task 7: Query data

The program included in this step retrieves all movies released in the year 1985.

49. Create queryitem.py

```bash
nano queryitem.py
```

50. Paste the following code (or use a file [queryitem.py](queryitem.py))

```python

#
#  Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
#  This file is licensed under the Apache License, Version 2.0 (the "License").
#  You may not use this file except in compliance with the License. A copy of
#  the License is located at
# 
#  http://aws.amazon.com/apache2.0/
# 
#  This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
#  CONDITIONS OF ANY KIND, either express or implied. See the License for the
#  specific language governing permissions and limitations under the License.
#
from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')

# Paste the correct name of the table
table = dynamodb.Table('studentX-table')

print("Movies from 1985")

response = table.query(
    KeyConditionExpression=Key('year').eq(1985)
)

for i in response['Items']:
    print(i['year'], ":", i['title'])


```

51. Paste the correct table name.
49. Press CTRL+O, ENTER to save your document. 
50. Press CTRL+X to exit the Nano editor.
51. To run the program, type the following command:

```bash
python queryitem.py
```



## END LAB

This is the end of the lab. Remove DynamoDB table:

55. In the AWS Management Console, on the **Services** menu, click **DynamoDB**.
53. Select your table and click **Delete tables**
54. Confirm by clicking **Delete**

<br><br>

<center><p>&copy; 2019 Chmurowisko Sp. z o.o.<p></center>
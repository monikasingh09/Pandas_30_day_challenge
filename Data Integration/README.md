
Que 1) Write a solution to find all the pairs (actor_id, director_id) where the actor has cooperated with the director at least three times.

Return the result table in any order.

data = [[1, 1, 0], [1, 1, 1], [1, 1, 2], [1, 2, 3], [1, 2, 4], [2, 1, 5], [2, 1, 6]]

actor_director = pd.DataFrame(data, columns=['actor_id', 'director_id', 'timestamp']).astype({'actor_id':'int64', 'director_id':'int64', 'timestamp':'int64'})

![image](https://github.com/user-attachments/assets/1d15d790-f4a1-4e82-96f0-04be8e9b7d7a)


![image](https://github.com/user-attachments/assets/8afe29af-59a5-43d0-92e5-6eed253aaf50)



Que 2) Write a solution to show the unique ID of each user, If a user does not have a unique ID replace just show null.

Return the result table in any order.

data = [[1, 'Alice'], [7, 'Bob'], [11, 'Meir'], [90, 'Winston'], [3, 'Jonathan']]

employees = pd.DataFrame(data, columns=['id', 'name']).astype({'id':'int64', 'name':'object'})

data = [[3, 1], [11, 2], [90, 3]]

employee_uni = pd.DataFrame(data, columns=['id', 'unique_id']).astype({'id':'int64', 'unique_id':'int64'})

![image](https://github.com/user-attachments/assets/cddaf522-bf68-42ae-a374-966dd7ef7c42)

![image](https://github.com/user-attachments/assets/bb93546b-398c-4180-a691-47e64c999d5c)


Que 3) Write a solution to find the number of times each student attended each exam.

Return the result table ordered by student_id and subject_name.

data = [[1, 'Alice'], [2, 'Bob'], [13, 'John'], [6, 'Alex']]

students = pd.DataFrame(data, columns=['student_id', 'student_name']).astype({'student_id':'Int64', 'student_name':'object'})

data = [['Math'], ['Physics'], ['Programming']]

subjects = pd.DataFrame(data, columns=['subject_name']).astype({'subject_name':'object'})

data = [[1, 'Math'], [1, 'Physics'], [1, 'Programming'], [2, 'Programming'], [1, 'Physics'], [1, 'Math'], [13, 'Math'], [13, 'Programming'], [13, 'Physics'], [2, 'Math'], [1, 'Math']]

examinations = pd.DataFrame(data, columns=['student_id', 'subject_name']).astype({'student_id':'Int64', 'subject_name':'object'})


![image](https://github.com/user-attachments/assets/d558acf5-ac71-40fd-b0bb-848c66271eeb)

![image](https://github.com/user-attachments/assets/f2692433-883a-4d1e-a910-be9c733501ca)


Que 4) Write a solution to find managers with at least five direct reports.

Return the result table in any order.

data = [[101, 'John', 'A', None], [102, 'Dan', 'A', 101], [103, 'James', 'A', 101], [104, 'Amy', 'A', 101], [105, 'Anne', 'A', 101], [106, 'Ron', 'B', 101]]

employee = pd.DataFrame(data, columns=['id', 'name', 'department', 'managerId']).astype({'id':'Int64', 'name':'object', 'department':'object', 'managerId':'Int64'})


![image](https://github.com/user-attachments/assets/e39e8844-b4f8-4fe1-b78b-7b8c37358268)

![image](https://github.com/user-attachments/assets/17dc2622-67d9-4e69-9fbf-17b9319b021e)


Que 5) Write a solution to find the names of all the salespersons who did not have any orders related to the company with the name "RED".

Return the result table in any order.

data = [[1, 'John', 100000, 6, '4/1/2006'], [2, 'Amy', 12000, 5, '5/1/2010'], [3, 'Mark', 65000, 12, '12/25/2008'], [4, 'Pam', 25000, 25, '1/1/2005'], [5, 'Alex', 5000, 10, '2/3/2007']]

sales_person = pd.DataFrame(data, columns=['sales_id', 'name', 'salary', 'commission_rate', 'hire_date']).astype({'sales_id':'Int64', 'name':'object', 'salary':'Int64', 'commission_rate':'Int64', 'hire_date':'datetime64[ns]'})

data = [[1, 'RED', 'Boston'], [2, 'ORANGE', 'New York'], [3, 'YELLOW', 'Boston'], [4, 'GREEN', 'Austin']]

company = pd.DataFrame(data, columns=['com_id', 'name', 'city']).astype({'com_id':'Int64', 'name':'object', 'city':'object'})

data = [[1, '1/1/2014', 3, 4, 10000], [2, '2/1/2014', 4, 5, 5000], [3, '3/1/2014', 1, 1, 50000], [4, '4/1/2014', 1, 4, 25000]]

orders = pd.DataFrame(data, columns=['order_id', 'order_date', 'com_id', 'sales_id', 'amount']).astype({'order_id':'Int64', 'order_date':'datetime64[ns]', 'com_id':'Int64', 'sales_id':'Int64', 'amount':'Int64'})


![image](https://github.com/user-attachments/assets/e972c6dd-9d26-4640-9495-b6d5d8ea54f7)

![image](https://github.com/user-attachments/assets/4781a8a2-496c-4ca8-989a-7a54cd2af863)









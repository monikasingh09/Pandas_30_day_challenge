Que 1) Write a solution to calculate the total time in minutes spent by each employee on each day at the office. Note that within one day, an employee can enter and leave more than once. The time spent in the office for a single entry is out_time - in_time.

Return the result table in any order.

data = [['1', '2020-11-28', '4', '32'], ['1', '2020-11-28', '55', '200'], ['1', '2020-12-3', '1', '42'], ['2', '2020-11-28', '3', '33'], ['2', '2020-12-9', '47', '74']]

employees = pd.DataFrame(data, columns=['emp_id', 'event_day', 'in_time', 'out_time']).astype({'emp_id':'Int64', 'event_day':'datetime64[ns]', 'in_time':'Int64', 'out_time':'Int64'})



![image](https://github.com/user-attachments/assets/5c2afb03-f048-439e-8a7a-f1bfbfac0748)


![image](https://github.com/user-attachments/assets/d3e0f9fb-84a3-4a71-b1b5-1db635698525)


Que 2) Write a solution to find the first login date for each player.

Return the result table in any order.

data = [[1, 2, '2016-03-01', 5], [1, 2, '2016-05-02', 6], [2, 3, '2017-06-25', 1], [3, 1, '2016-03-02', 0], [3, 4, '2018-07-03', 5]]

activity = pd.DataFrame(data, columns=['player_id', 'device_id', 'event_date', 'games_played']).astype({'player_id':'Int64', 'device_id':'Int64', 'event_date':'datetime64[ns]', 'games_played':'Int64'})


![image](https://github.com/user-attachments/assets/ec56c00b-e422-416c-aec1-9ae491acb892)

![image](https://github.com/user-attachments/assets/e029f874-8f78-4b2b-97be-a987bd55fd14)


Que 3) Write a solution to calculate the number of unique subjects each teacher teaches in the university.

Return the result table in any order.

data = [[1, 2, 3], [1, 2, 4], [1, 3, 3], [2, 1, 1], [2, 2, 1], [2, 3, 1], [2, 4, 1]]

teacher = pd.DataFrame(data, columns=['teacher_id', 'subject_id', 'dept_id']).astype({'teacher_id':'Int64', 'subject_id':'Int64', 'dept_id':'Int64'})

![image](https://github.com/user-attachments/assets/cd7b7714-6bb6-4c90-bd91-ea8722c39859)

![image](https://github.com/user-attachments/assets/f3f55d8e-dd5c-43f9-a50e-3696bad85f85)


Que 4 ) Write a solution to find all the classes that have at least five students.

Return the result table in any order.

data = [['A', 'Math'], ['B', 'English'], ['C', 'Math'], ['D', 'Biology'], ['E', 'Math'], ['F', 'Computer'], ['G', 'Math'], ['H', 'Math'], ['I', 'Math']]

courses = pd.DataFrame(data, columns=['student', 'class']).astype({'student':'object', 'class':'object'})

![image](https://github.com/user-attachments/assets/35252c19-dea2-4f37-b69c-a92c2897231f)

![image](https://github.com/user-attachments/assets/cd3c6e69-134a-44b3-a545-3945602114a1)



Que 5) Write a solution to find the customer_number for the customer who has placed the largest number of orders.

The test cases are generated so that exactly one customer will have placed more orders than any other customer

![image](https://github.com/user-attachments/assets/94a0457c-e4b6-4274-905d-c8032f44b5c4)

![image](https://github.com/user-attachments/assets/417c2316-7097-42c8-a219-0c7398b98307)


Que 6) Write a solution to find for each date the number of different products sold and their names.

The sold products names for each date should be sorted lexicographically.

Return the result table ordered by sell_date.

data = [['2020-05-30', 'Headphone'], ['2020-06-01', 'Pencil'], ['2020-06-02', 'Mask'], ['2020-05-30', 'Basketball'], ['2020-06-01', 'Bible'], ['2020-06-02', 'Mask'], ['2020-05-30', 'T-Shirt']]

activities = pd.DataFrame(data, columns=['sell_date', 'product']).astype({'sell_date':'datetime64[ns]', 'product':'object'})

![image](https://github.com/user-attachments/assets/6afcb05a-b83a-4c24-b393-3ce86e5043f0)

![image](https://github.com/user-attachments/assets/75a96304-7587-4102-9ba2-3a51454b9ee7)



Que 7) For each date_id and make_name, find the number of distinct lead_id's and distinct partner_id's.

Return the result table in any order.

data = [['2020-12-8', 'toyota', 0, 1], ['2020-12-8', 'toyota', 1, 0], ['2020-12-8', 'toyota', 1, 2], ['2020-12-7', 'toyota', 0, 2], ['2020-12-7', 'toyota', 0, 1], ['2020-12-8', 'honda', 1, 2], ['2020-12-8', 'honda', 2, 1], ['2020-12-7', 'honda', 0, 1], ['2020-12-7', 'honda', 1, 2], ['2020-12-7', 'honda', 2, 1]]

daily_sales = pd.DataFrame(data, columns=['date_id', 'make_name', 'lead_id', 'partner_id']).astype({'date_id':'datetime64[ns]', 'make_name':'object', 'lead_id':'Int64', 'partner_id':'Int64'})

![image](https://github.com/user-attachments/assets/d43e7b37-6f60-40ca-84eb-1fe28d51b136)

![image](https://github.com/user-attachments/assets/2642ce87-95d5-43ae-9fd0-73fbc2473ba5)





























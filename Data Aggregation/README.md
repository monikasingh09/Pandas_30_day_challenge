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




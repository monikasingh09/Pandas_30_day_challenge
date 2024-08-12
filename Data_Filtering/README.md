
Que1 ) Find out Big Countries : 

![image](https://github.com/user-attachments/assets/f08b53d8-0a3b-49ba-8b31-463aed047968)

name is the primary key (column with unique values) for this table.
Each row of this table gives information about the name of a country, the continent to which it belongs, its area, the population, and its GDP value.
 

A country is big if:

it has an area of at least three million (i.e., 3000000 km2), or
it has a population of at least twenty-five million (i.e., 25000000).
Write a solution to find the name, population, and area of the big countries.

Return the result table in any order.


## Code ##

![image](https://github.com/user-attachments/assets/032e4d50-1857-4101-b8ff-885005573c4f)



![image](https://github.com/user-attachments/assets/bf8b09cf-aa8f-4ccb-9700-93060f3784bd)


Que2: Write a solution to find the ids of products that are both low fat and recyclable.
Return the result table in any order.
data = [['0', 'Y', 'N'], ['1', 'Y', 'Y'], ['2', 'N', 'Y'], ['3', 'Y', 'Y'], ['4', 'N', 'N']]
products = pd.DataFrame(data, columns=['product_id', 'low_fats', 'recyclable']).astype({'product_id':'int64', 'low_fats':'category', 'recyclable':'category'})

![image](https://github.com/user-attachments/assets/cc6cbb03-5807-4e20-a459-c137a8a3279b)

![image](https://github.com/user-attachments/assets/8b9635c7-f5e5-4164-8e3f-fe2ae35ce246)



Que 3) Write a solution to find all customers who never order anything.

Return the result table in any order

data = [[1, 'Joe'], [2, 'Henry'], [3, 'Sam'], [4, 'Max']]
customers = pd.DataFrame(data, columns=['id', 'name']).astype({'id':'Int64', 'name':'object'})
data = [[1, 3], [2, 1]]
orders = pd.DataFrame(data, columns=['id', 'customerId']).astype({'id':'Int64', 'customerId':'Int64'})

![image](https://github.com/user-attachments/assets/e6ba33a5-724d-4f97-a0a6-fb85a43e91a8)


![image](https://github.com/user-attachments/assets/f8e63386-4597-4fc1-8fb6-b9e73dc52d44)



Que 4) Write a solution to find all the authors that viewed at least one of their own articles.

Return the result table sorted by id in ascending order.

data = [[1, 3, 5, '2019-08-01'], [1, 3, 6, '2019-08-02'], [2, 7, 7, '2019-08-01'], [2, 7, 6, '2019-08-02'], [4, 7, 1, '2019-07-22'], [3, 4, 4, '2019-07-21'], [3, 4, 4, '2019-07-21']]
views = pd.DataFrame(data, columns=['article_id', 'author_id', 'viewer_id', 'view_date']).astype({'article_id':'Int64', 'author_id':'Int64', 'viewer_id':'Int64', 'view_date':'datetime64[ns]'})


Que 5) Write a solution to find all the authors that viewed at least one of their own articles.

Return the result table sorted by id in ascending order

data = [[1, 3, 5, '2019-08-01'], [1, 3, 6, '2019-08-02'], [2, 7, 7, '2019-08-01'], [2, 7, 6, '2019-08-02'], [4, 7, 1, '2019-07-22'], [3, 4, 4, '2019-07-21'], [3, 4, 4, '2019-07-21']]
views = pd.DataFrame(data, columns=['article_id', 'author_id', 'viewer_id', 'view_date']).astype({'article_id':'Int64', 'author_id':'Int64', 'viewer_id':'Int64', 'view_date':'datetime64[ns]'})


![image](https://github.com/user-attachments/assets/e694b965-ea20-4e04-a3bd-c762a0b87c4c)

![image](https://github.com/user-attachments/assets/fccd2113-6bfc-4bbf-bf5d-63fea608612b)







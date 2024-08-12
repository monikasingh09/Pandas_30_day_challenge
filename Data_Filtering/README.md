
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




# contents

- Creating a table and inserting data
- Querying the table
- Aggregating data
- Project: Design a store database

# Creating a table and inserting data

```
/** Grocery list:
Bananas (4)
Peanut Butter (1)
Dark Chocolate Bars (2)
**/

CREATE TABLE groceries (id INTEGER PRIMARY KEY, name TEXT, quantity INTEGER );

INSERT INTO groceries VALUES (1, "Bananas", 4);
INSERT INTO groceries VALUES (2, "Peanut Butter", 1);
INSERT INTO groceries VALUES (3, "Dark chocolate bars", 2);
SELECT * FROM groceries;
```

[Demo of "Creating a table and inserting data" | Computer programming | Khan Academy](https://www.khanacademy.org/computer-programming/demo-of-creating-a-table-and-inserting-data/4836832584728576)

[Exercise of "Challenge: Book list database" | Computer programming | Khan Academy](https://www.khanacademy.org/computer-programming/exercise-of-challenge-book-list-database/5800810009919488)

# Querying the table

```
CREATE TABLE groceries (id INTEGER PRIMARY KEY, name TEXT, quantity INTEGER, aisle INTEGER);
INSERT INTO groceries VALUES (1, "Bananas", 4, 7);
INSERT INTO groceries VALUES(2, "Peanut Butter", 1, 2);
INSERT INTO groceries VALUES(3, "Dark Chocolate Bars", 2, 2);
INSERT INTO groceries VALUES(4, "Ice cream", 1, 12);
INSERT INTO groceries VALUES(5, "Cherries", 6, 2);
INSERT INTO groceries VALUES(6, "Chocolate syrup", 1, 4);

SELECT * FROM groceries WHERE aisle > 5 ORDER BY aisle;
```

[DEMO of "Querying the table" | Computer programming | Khan Academy](https://www.khanacademy.org/computer-programming/demo-of-querying-the-table/4962674790957056)

[Exercise of "Challenge: Box office hits database" | Computer programming | Khan Academy](https://www.khanacademy.org/computer-programming/exercise-of-challenge-box-office-hits-database/4872605031792640)

# Aggregating data

```
CREATE TABLE groceries (id INTEGER PRIMARY KEY, name TEXT, quantity INTEGER, aisle INTEGER);
INSERT INTO groceries VALUES (1, "Bananas", 56, 7);
INSERT INTO groceries VALUES (2, "Peanut Butter", 1, 2);
INSERT INTO groceries VALUES (3, "Dark Chocolate Bars", 2, 2);
INSERT INTO groceries VALUES (4, "Ice cream", 1, 12);
INSERT INTO groceries VALUES (5, "Cherries", 6, 2);
INSERT INTO groceries VALUES (6, "Chocolate syrup", 1, 4);

SELECT aisle, SUM(quantity) FROM groceries GROUP BY aisle;
```

[Demo of "Aggregating data" | Computer programming | Khan Academy](https://www.khanacademy.org/computer-programming/demo-of-aggregating-data/6304343452876800)

[(1) Exercise of "Challenge: TODO list database stats" | Computer programming | Khan Academy](https://www.khanacademy.org/computer-programming/exercise-of-challenge-todo-list-database-stats/4680807361609728)

```
@anifacc
2017-05-11
```

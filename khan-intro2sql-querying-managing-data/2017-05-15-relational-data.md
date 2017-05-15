# JOINing related tables

```
CREATE TABLE students (id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    phone TEXT,
    birthdate TEXT);

INSERT INTO students (first_name, last_name, email, phone, birthdate)
    VALUES ("Peter", "Rabbit", "peter@rabbit.com", "555-6666", "2002-06-24");
INSERT INTO students (first_name, last_name, email, phone, birthdate)
    VALUES ("Alice", "Wonderland", "alice@wonderland.com", "555-4444", "2002-07-04");
    
CREATE TABLE student_grades (id INTEGER PRIMARY KEY,
    student_id INTEGER,
    test TEXT,
    grade INTEGER);

INSERT INTO student_grades (student_id, test, grade)
    VALUES (1, "Nutrition", 95);
INSERT INTO student_grades (student_id, test, grade)
    VALUES (2, "Nutrition", 92);
INSERT INTO student_grades (student_id, test, grade)
    VALUES (1, "Chemistry", 85);
INSERT INTO student_grades (student_id, test, grade)
    VALUES (2, "Chemistry", 95);
    
SELECT * FROM student_grades;

/* cross join */
SELECT * FROM student_grades, students;

/* implicit inner join */
SELECT * FROM student_grades, students
    WHERE student_grades.student_id = students.id;
    
/* explicit inner join - JOIN */
SELECT students.first_name, students.last_name, students.email, student_grades.test, student_grades.grade FROM students
    JOIN student_grades
    ON students.id = student_grades.student_id
    WHERE grade > 90;
```

[Demo of "JOINing related tables" | Computer programming | Khan Academy](https://www.khanacademy.org/computer-programming/demo-of-joining-related-tables/6193675710038016)  

[Exercise of "Challenge: Bobby's Hobbies" | Computer programming | Khan Academy](https://www.khanacademy.org/computer-programming/exercise-of-challenge-bobbys-hobbies/6692630919184384)

# Joining related tables with left outer joins

```
CREATE TABLE students (id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    phone TEXT,
    birthdate TEXT);

INSERT INTO students (first_name, last_name, email, phone, birthdate)
    VALUES ("Peter", "Rabbit", "peter@rabbit.com", "555-6666", "2002-06-24");
INSERT INTO students (first_name, last_name, email, phone, birthdate)
    VALUES ("Alice", "Wonderland", "alice@wonderland.com", "555-4444", "2002-07-04");
    
CREATE TABLE student_grades (id INTEGER PRIMARY KEY,
    student_id INTEGER,
    test TEXT,
    grade INTEGER);

INSERT INTO student_grades (student_id, test, grade)
    VALUES (1, "Nutrition", 95);
INSERT INTO student_grades (student_id, test, grade)
    VALUES (2, "Nutrition", 92);
INSERT INTO student_grades (student_id, test, grade)
    VALUES (1, "Chemistry", 85);
INSERT INTO student_grades (student_id, test, grade)
    VALUES (2, "Chemistry", 95);

CREATE TABLE student_projects (id INTEGER PRIMARY KEY,
    student_id INTEGER,
    title TEXT);
    
INSERT INTO student_projects (student_id, title)
    VALUES (1, "Carrotapault");
   
/* outer join RIGHT OUTER JOIN or FULL OUTER JOIN*/  
SELECT students.first_name, students.last_name, student_projects.title
    FROM students
    LEFT OUTER JOIN student_projects
    ON students.id = student_projects.student_id;
```

[Demo of "Joining related tables with left outer joins" | Computer programming | Khan Academy](https://www.khanacademy.org/computer-programming/demo-of-joining-related-tables-with-left-outer-joins/5401817933217792)

[Exercise of "Challenge: Customer's orders" | Computer programming | Khan Academy](https://www.khanacademy.org/computer-programming/exercise-of-challenge-customers-orders/4564348727787520)

```
CREATE TABLE customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT);
    
INSERT INTO customers (name, email) VALUES ("Doctor Who", "doctorwho@timelords.com");
INSERT INTO customers (name, email) VALUES ("Harry Potter", "harry@potter.com");
INSERT INTO customers (name, email) VALUES ("Captain Awesome", "captain@awesome.com");

CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    item TEXT,
    price REAL);

INSERT INTO orders (customer_id, item, price)
    VALUES (1, "Sonic Screwdriver", 1000.00);
INSERT INTO orders (customer_id, item, price)
    VALUES (2, "High Quality Broomstick", 40.00);
INSERT INTO orders (customer_id, item, price)
    VALUES (1, "TARDIS", 1000000.00);

SELECT customers.name, customers.email, orders.item, orders.price FROM customers 
    LEFT OUTER JOIN orders 
    ON customers.id = orders.customer_id;
    
SELECT customers.name, customers.email, SUM(orders.price) AS total_price FROM customers 
    LEFT OUTER JOIN orders 
    ON customers.id = orders.customer_id 
    GROUP BY customers.name 
    ORDER BY total_price DESC;
```

---

# Joining tables to themselves with self-joins

```
CREATE TABLE students (id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    phone TEXT,
    birthdate TEXT,
    buddy_id INTEGER);

INSERT INTO students 
    VALUES (1, "Peter", "Rabbit", "peter@rabbit.com", "555-6666", "2002-06-24", 2);
INSERT INTO students 
    VALUES (2, "Alice", "Wonderland", "alice@wonderland.com", "555-4444", "2002-07-04", 1);
INSERT INTO students 
    VALUES (3, "Aladdin", "Lampland", "aladdin@lampland.com", "555-3333", "2001-05-10", 4);
INSERT INTO students 
    VALUES (4, "Simba", "Kingston", "simba@kingston.com", "555-1111", "2001-12-24", 3);
    
SELECT id, first_name, last_name, buddy_id FROM students;

/* self join */
SELECT students.first_name, students.last_name, buddies.email as buddy_email
    FROM students
    JOIN students buddies
    ON students.buddy_id = buddies.id;
```

[Demo of "Joining tables to themselves with self-joins" | Computer programming | Khan Academy](https://www.khanacademy.org/computer-programming/demo-of-joining-tables-to-themselves-with-self-joins/5598725297471488)

[Exercise of "Challenge: Sequels in SQL" | Computer programming | Khan Academy](https://www.khanacademy.org/computer-programming/exercise-of-challenge-sequels-in-sql/5363377975918592)

```
CREATE TABLE movies (id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    released INTEGER,
    sequel_id INTEGER);

INSERT INTO movies 
    VALUES (1, "Harry Potter and the Philosopher's Stone", 2001, 2);
INSERT INTO movies 
    VALUES (2, "Harry Potter and the Chamber of Secrets", 2002, 3);
INSERT INTO movies 
    VALUES (3, "Harry Potter and the Prisoner of Azkaban", 2004, 4);
INSERT INTO movies 
    VALUES (4, "Harry Potter and the Goblet of Fire", 2005, 5);
INSERT INTO movies 
    VALUES (5, "Harry Potter and the Order of the Phoenix ", 2007, 6);
INSERT INTO movies 
    VALUES (6, "Harry Potter and the Half-Blood Prince", 2009, 7);
INSERT INTO movies 
    VALUES (7, "Harry Potter and the Deathly Hallows – Part 1", 2010, 8);
INSERT INTO movies 
    VALUES (8, "Harry Potter and the Deathly Hallows – Part 2", 2011, NULL);

SELECT movies.title, copy.title as sequel_title
    FROM movies
    LEFT OUTER JOIN movies copy
    ON movies.sequel_id = copy.id;
```

# Combining multiple joins

```
CREATE TABLE students (id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    phone TEXT,
    birthdate TEXT);

INSERT INTO students (first_name, last_name, email, phone, birthdate)
    VALUES ("Peter", "Rabbit", "peter@rabbit.com", "555-6666", "2002-06-24");
INSERT INTO students (first_name, last_name, email, phone, birthdate)
    VALUES ("Alice", "Wonderland", "alice@wonderland.com", "555-4444", "2002-07-04");
INSERT INTO students (first_name, last_name, email, phone, birthdate)
    VALUES ("Aladdin", "Lampland", "aladdin@lampland.com", "555-3333", "2001-05-10");
INSERT INTO students (first_name, last_name, email, phone, birthdate)
    VALUES ("Simba", "Kingston", "simba@kingston.com", "555-1111", "2001-12-24");
    
CREATE TABLE student_projects (id INTEGER PRIMARY KEY,
    student_id INTEGER,
    title TEXT);
    
INSERT INTO student_projects (student_id, title)
    VALUES (1, "Carrotapault");
INSERT INTO student_projects (student_id, title)
    VALUES (2, "Mad Hattery");
INSERT INTO student_projects (student_id, title)
    VALUES (3, "Carpet Physics");
INSERT INTO student_projects (student_id, title)
    VALUES (4, "Hyena Habitats");
    
CREATE TABLE project_pairs (id INTEGER PRIMARY KEY,
    project1_id INTEGER,
    project2_id INTEGER);

INSERT INTO project_pairs (project1_id, project2_id)
    VALUES(1, 2);
INSERT INTO project_pairs (project1_id, project2_id)
    VALUES(3, 4);
    
SELECT a.title, b.title FROM project_pairs
    JOIN student_projects a
    ON project_pairs.project1_id = a.id
    JOIN student_projects b
    ON project_pairs.project2_id = b.id;

SELECT * FROM student_projects;
```

[Demo of "Combining multiple joins" | Computer programming | Khan Academy](https://www.khanacademy.org/computer-programming/demo-of-combining-multiple-joins/5142368354107392)


[Exercise of "Challenge: FriendBook" | Computer programming | Khan Academy](https://www.khanacademy.org/computer-programming/exercise-of-challenge-friendbook/5074696580956160)

```
CREATE TABLE persons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname TEXT,
    age INTEGER);
    
INSERT INTO persons (fullname, age) VALUES ("Bobby McBobbyFace", "12");
INSERT INTO persons (fullname, age) VALUES ("Lucy BoBucie", "25");
INSERT INTO persons (fullname, age) VALUES ("Banana FoFanna", "14");
INSERT INTO persons (fullname, age) VALUES ("Shish Kabob", "20");
INSERT INTO persons (fullname, age) VALUES ("Fluffy Sparkles", "8");

CREATE table hobbies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    person_id INTEGER,
    name TEXT);
    
INSERT INTO hobbies (person_id, name) VALUES (1, "drawing");
INSERT INTO hobbies (person_id, name) VALUES (1, "coding");
INSERT INTO hobbies (person_id, name) VALUES (2, "dancing");
INSERT INTO hobbies (person_id, name) VALUES (2, "coding");
INSERT INTO hobbies (person_id, name) VALUES (3, "skating");
INSERT INTO hobbies (person_id, name) VALUES (3, "rowing");
INSERT INTO hobbies (person_id, name) VALUES (3, "drawing");
INSERT INTO hobbies (person_id, name) VALUES (4, "coding");
INSERT INTO hobbies (person_id, name) VALUES (4, "dilly-dallying");
INSERT INTO hobbies (person_id, name) VALUES (4, "meowing");

CREATE table friends (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    person1_id INTEGER,
    person2_id INTEGER);

INSERT INTO friends (person1_id, person2_id)
    VALUES (1, 4);
INSERT INTO friends (person1_id, person2_id)
    VALUES (2, 3);
    
SELECT persons.fullname, hobbies.name as hobby_name
    FROM persons
    JOIN hobbies
    ON persons.id = hobbies.person_id;

SELECT a.fullname, b.fullname FROM friends
    JOIN persons a
    ON a.id = friends.person1_id
    JOIN persons b
    ON b.id = friends.person2_id;
```

# Project: Famous People

```
/* Create table about the people and what they do here */

CREATE TABLE singers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname TEXT,
    songs TEXT,
    areas TEXT);

INSERT INTO singers (fullname, songs, areas) VALUES ("Jack Zhou", "Ting Ma Ma De Hua", "Taiwan");
INSERT INTO singers (fullname, songs, areas) VALUES ("Stefanie Sun", "Kai Shi Dong Le", "Singapore");
INSERT INTO singers (fullname, songs, areas) VALUES ("Jolin Cai", "Wu Niang", "Taiwan");
INSERT INTO singers (fullname, songs, areas) VALUES ("Jiaju Huang", "Xi Huan Ni", "Hongkong");
INSERT INTO singers (fullname, songs, areas) VALUES ("Junjie Lin", "Xiao Jiu Wo", "Singapore");
INSERT INTO singers (fullname, songs, areas) VALUES ("G.E.M", "Zai Jian", "Hongkong");
INSERT INTO singers (fullname, songs, areas) VALUES ("Dan Gibson", "Nature's Path", "U.S.A");

CREATE TABLE gossips (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    person_id INTEGER, 
    name TEXT);
    
INSERT INTO gossips (person_id, name) VALUES(3, "Jack Zhou");
INSERT INTO gossips (person_id, name) VALUES(1, "Jolin Cai");


SELECT * FROM singers;
SELECT * FROM gossips;

SELECT singers.fullname, gossips.name 
    FROM singers 
    LEFT OUTER JOIN gossips
    ON singers.id = gossips.person_id;
```

["Project: Famous people" | Computer programming | Khan Academy](https://www.khanacademy.org/computer-programming/spin-off-of-project-famous-people/5624326230179840)


```
@anifacc
2017-05-15
```
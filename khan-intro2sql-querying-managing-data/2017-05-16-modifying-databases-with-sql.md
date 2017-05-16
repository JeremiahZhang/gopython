# Changjing rows with UPDATE and DELETE

```
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT);

CREATE TABLE diary_logs (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    date TEXT,
    content TEXT
    );

/* After user submitted their new diary log */
INSERT INTO diary_logs (user_id, date, content) VALUES (1, "2015-04-01",
    "I had a horrible fight with OhNoesGuy and I buried my woes in 3 pounds of dark chocolate.");

INSERT INTO diary_logs (user_id, date, content) VALUES (1, "2015-04-02",
    "We made up and now we're best friends forever and we celebrated with a tub of ice cream.");

SELECT * FROM diary_logs;

UPDATE diary_logs SET content = "I had a horrible fight with OhNoesGuy" WHERE id = 1;

SELECT * FROM diary_logs;

DELETE FROM diary_logs WHERE id = 1;

SELECT * FROM diary_logs;
```

[Demo of "Changing rows with UPDATE and DELETE" | Computer programming | Khan Academy](https://www.khanacademy.org/computer-programming/demo-of-changing-rows-with-update-and-delete/5716934373736448)

```
CREATE table documents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    content TEXT,
    author TEXT);

INSERT INTO documents (author, title, content)
    VALUES ("Puff T.M. Dragon", "Fancy Stuff", "Ceiling wax, dragon wings, etc.");
INSERT INTO documents (author, title, content)
    VALUES ("Puff T.M. Dragon", "Living Things", "They're located in the left ear, you know.");
INSERT INTO documents (author, title, content)
    VALUES ("Jackie Paper", "Pirate Recipes", "Cherry pie, apple pie, blueberry pie.");
INSERT INTO documents (author, title, content)
    VALUES ("Jackie Paper", "Boat Supplies", "Rudder - guitar. Main mast - bed post.");
INSERT INTO documents (author, title, content)
    VALUES ("Jackie Paper", "Things I'm Afraid Of", "Talking to my parents, the sea, giant pirates, heights.");

SELECT * FROM documents;

UPDATE documents SET author = "Jackie Draper" WHERE author = "Jackie Paper";

SELECT * FROM documents;

DELETE FROM documents WHERE title LIKE "%Things I'm Afraid Of%";

SELECT * FROM documents;
```

[Exercise of "Challenge: Dynamic Documents" | Computer programming | Khan Academy](https://www.khanacademy.org/computer-programming/exercise-of-challenge-dynamic-documents/5793470690951168)

# Altering tables after creation

```
/* What we used to originally create the table */
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT);

CREATE TABLE diary_logs (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    date TEXT,
    content TEXT
    );

/* After user submits a diary log */
INSERT INTO diary_logs (user_id, date, content) VALUES (1, "2015-04-02",
    "OhNoesGuy and I made up and now we're best friends forever and we celebrated with a tub of ice cream.");

ALTER TABLE diary_logs ADD emotion TEXT default "unknown";

INSERT INTO diary_logs (user_id, date, content, emotion) VALUES (1, "2015-04-03",
    "We went to Disneyland!", "happy");

SELECT * FROM diary_logs;
```

[Demo of "Altering tables after creation" | Computer programming | Khan Academy](https://www.khanacademy.org/computer-programming/demo-of-altering-tables-after-creation/4579960598364160)

```
CREATE TABLE clothes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT,
    design TEXT);

INSERT INTO clothes (type, design)
    VALUES ("dress", "pink polka dots");
INSERT INTO clothes (type, design)
    VALUES ("pants", "rainbow tie-dye");
INSERT INTO clothes (type, design)
    VALUES ("blazer", "black sequin");

ALTER TABLE clothes ADD price INTEGER;

SELECT * FROM clothes;

UPDATE clothes SET price = 10 WHERE id = 1;
UPDATE clothes SET price = 20 WHERE id = 2;
UPDATE clothes SET price = 30 WHERE id = 3;

SELECT * FROM clothes;

INSERT INTO clothes (type, design, price)
    VALUES ("T-shirt", "ONLY", 40);

SELECT * FROM clothes;
```

[Exercise of "Challenge: Clothing alterations" | Computer programming | Khan Academy](https://www.khanacademy.org/computer-programming/exercise-of-challenge-clothing-alterations/6296981685993472)

# Make your SQL safer

[Make your SQL safer (article) | Khan Academy](https://www.khanacademy.org/computing/computer-programming/sql/modifying-databases-with-sql/a/make-your-sql-safer)

## Avoiding bad updates/deletes

> Before you issue an UPDATE, run a SELECT with the same WHERE to make sure you're updating the right column and row.
For example, before running:

`UPDATE users SET deleted = true WHERE id = 1;`

> You could run:

`SELECT id, deleted FROM users WHERE id = 1;`

> Once you decide to run the update, you can use the LIMIT operator to make sure you don't accidentally update too many rows:

`UPDATE users SET deleted = true WHERE id = 1 LIMIT 1;`

> Or if you were deleting:

`DELETE users WHERE id = 1 LIMIT 1;`

## Using transcations

```
BEGIN TRANSACTION;
UPDATE people SET husband = "Winston" WHERE user_id = 1;
UPDATE people SET wife = "Winnefer" WHERE user_id = 2;
COMMIT;
```

> If the database is unable to issue both those UPDATE commands for some reason, then it will rollback the transaction and leave the database how it was when it started.

> For example, the following commands create a row denoting that a user earned a badge, and then update the user's recent activity to describe that:

```
INSERT INTO user_badges VALUES (1, "SQL Master", "4pm");
UPDATE user SET recent_activity = "Earned SQL Master badge" WHERE id = 1;
```

> At the same time, another user or process might be awarding the user a second badge:

```
INSERT INTO user_badges VALUES (1, "Great Listener", "4:05pm");
UPDATE user SET recent_activity = "Earned Great Listener badge" WHERE id = 1;
````

> These commands could now actually be issued in this order:

```
INSERT INTO user_badges VALUES (1, "SQL Master");
INSERT INTO user_badges VALUES (1, "Great Listener");
UPDATE user SET recent_activity = "Earned Great Listener badge" WHERE id = 1;
UPDATE user SET recent_activity = "Earned SQL Master badge" WHERE id = 1;
```

> Their recent activity would now be "Earned SQL Master badge" even though the most recently inserted badge was "Great listener". That's not the end of the world, but it's also probably not what we expected.
Instead, we could run those in a transaction, to guarantee that no other transactions happen in the middle:

```
BEGIN TRANSACTION;
INSERT INTO user_badges VALUES (1, "SQL Master");
UPDATE user SET recent_activity = "Earned SQL Master badge" WHERE id = 1;
COMMIT;
```

## Making backups

## Replication

## Granting privileges

---

# Project

[Spin-off of "Project: App impersonator" | Computer programming | Khan Academy](https://www.khanacademy.org/computer-programming/spin-off-of-project-app-impersonator/5957060391665664)

---

```
@anifacc
2017-05-16
```

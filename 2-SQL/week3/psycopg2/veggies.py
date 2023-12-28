import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect(
    """
    dbname=week3 user=postgres host=localhost port=5432
    """
)

# auto commit our changes to the database
conn.set_session(autocommit=True)

# a cursor object.
cur=conn.cursor()

cur.execute(
    """
    DROP TABLE IF EXISTS veggies
    """
)

cur.execute(
    """
    CREATE TABLE veggies(
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        colour TEXT NOT NULL
    )
    """
)

cur.execute(
    """
    INSERT INTO veggies VALUES 
    (1,'carrot','orange'),
    (2,'onion','yellow'),
    (3,'zucchini','green'),
    (4,'squash','yellow'),
    (5,'pepper','red'),
    (6,'onion','red')
    """
)

# run
cur.execute(
    """
    SELECT * FROM veggies
    """
)


# access to the result set
# retrieve query results
records=cur.fetchall()

# print(records)

cur.execute(
    """
    select colour,name from veggies
    """
)

veggie_records=cur.fetchall()
for v in veggie_records:
    print(v[0],v[1])

print()

cur.execute(
    """
    select colour, name from veggies order by name, colour
    """
)

veggie_records=cur.fetchall()
for i,v in enumerate(veggie_records):
    print(str(i+1)+".",v[0].capitalize(),v[1].capitalize())
# save file.

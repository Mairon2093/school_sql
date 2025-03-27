database = "school_db"
user = "school"
password = "School1234*"
host = "79.174.88.238"
port = "15221"

conn = psycopg2.connect(
    database = database,
    user = user,
    password = password,
    host = host,
    port = port
)

cur = conn.cursor()
migration = ""
with open("migrations.sql") as f:
    migration = f.read()

# KFC parser
Script for filling the database with information about KFC restaurants

## How to run
1. `Clone` this repository and open its directory.
```shell
git clone https://github.com/Moroes/KFC_parser.git
```
2. `Run` the script
```shell
python main.py
```

## How to use
After running the script, the database is filled, from which you can get the 
**Example**
SQL query to get restaurants where you can have breakfast at 8.45
```sql
SELECT * FROM restaurants WHERE city = 'Новосибирск' and start_breakfast_time < '08:45:00' and end_breakfast_time > '08:45:00'
```
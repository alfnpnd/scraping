!pip install psycopg2 requests
import psycopg2
import requests

def fetch_data_from_db() -> list:
    conn = psycopg2.connect(
        dbname="",
        user="",
        password="",
        host="",
        port=""
    )

    cur = conn.cursor()
    cur.execute("SELECT * FROM ")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    return rows

def insert_data_into_crm(data: list) -> None:
    crm_url = ""
    crm_headers = {
        "Content-Type": "application/json",
        "Authorization": ""
    }

    for row in data:
        crm_data = {
            "field1": row[0],
            "field2": row[1],
            "field3": row[2],
            # Add more fields as needed
        }

        response = requests.post(crm_url, json=crm_data, headers=crm_headers)
        if response.status_code != 201:
            print(f"Error inserting data into CRM: {response.text}")

def main():
    data = fetch_data_from_db()
    insert_data_into_crm(data)

if __name__ == "__main__":
    main()

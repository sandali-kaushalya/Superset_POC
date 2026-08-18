import json
import pymysql

GEOJSON_FILE = "/data/finland_municipalities_2026.geojson"

with open(GEOJSON_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

conn = pymysql.connect(
    host="saga-dw",
    port=3306,
    user="root",
    password="root",
    database="dw",
    charset="utf8mb4",
)

cursor = conn.cursor()

cursor.execute("DELETE FROM finland_municipalities")

count = 0

for feature in data["features"]:
    properties = feature["properties"]

    code = str(properties["kunta"]).zfill(3)
    name = properties["nimi"]

    # Store the complete GeoJSON Feature
    geojson = json.dumps(feature, ensure_ascii=False)

    cursor.execute(
        """
        INSERT INTO finland_municipalities
        (municipality_code, municipality_name, geojson)
        VALUES (%s, %s, %s)
        """,
        (code, name, geojson),
    )

    count += 1

conn.commit()

cursor.close()
conn.close()

print(f"Loaded {count} municipalities.")
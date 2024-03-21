import pandas as pd
import json
import random
import pymysql

# MySQL database connection details
host = 'localhost'
user = 'root'
password = ''
database = 'data1'

# Connect to the database
connection = pymysql.connect(host=host, user=user, password=password, database=database)
cursor = connection.cursor()

# SQL query to fetch data from the database table
sql_query = 'SELECT * FROM data'

# Execute the query and fetch all rows
cursor.execute(sql_query)
rows = cursor.fetchall()

# Convert fetched data to a DataFrame
columns = [col[0] for col in cursor.description]
df = pd.DataFrame(rows, columns=columns)

# Close the database connection
connection.close()

# Split the DataFrame into chunks of 10000 rows
chunk_size = 500
chunks = [df[i:i+chunk_size] for i in range(0, len(df), chunk_size)]

for i, chunk in enumerate(chunks, start=1):
    # Transform data to match JSON format
    nodes = []
    edges = []
    edge_id_counter = 1  # Start edge IDs from 1

    for index, row in chunk.iterrows():
        # Node for gene1
        nodes.append({
            "data": {
                "id": str(row['gene1']),
                "selected": False,
                "NodeType": "miRNA",
                "Type": "miRNA",
                "Quality": 200,
                "name": str(row['gene1'])
            },
            "position": {
                "x": random.uniform(0, 300000),  # Adjust range as needed
                "y": random.uniform(0, 300000)    # Adjust range as needed
            },
            "selected": False
        })

        # Node for gene2
        nodes.append({
            "data": {
                "id": str(row['gene2']),
                "selected": False,
                "NodeType": "miRNA",
                "Type": "miRNA",
                "Quality": 200,
                "name": str(row['gene2'])
            },
            "position": {
                "x": random.uniform(0, 300000),  # Adjust range as needed
                "y": random.uniform(0, 300000)    # Adjust range as needed
            },
            "selected": False
        })

        # Edge from gene1 to gene2
        edges.append({
            "data": {
                "id": "D" + str(edge_id_counter),
                "source": str(row['gene1']),
                "selected": False,
                "target": str(row['gene2']),
                "predict_gi": str(row['predict_gi']),
                "max": row['max'],
                "interaction": "cc"
            }
        })

        # Edge from gene2 to gene1
        edges.append({
            "data": {
                "id": "E" + str(edge_id_counter),
                "source": str(row['gene2']),
                "selected": False,
                "target": str(row['gene1']),
                "predict_gi": str(row['predict_gi']),
                "max": row['max'],
                "interaction": "cc"
            }
        })

        edge_id_counter += 1  # Increment edge ID counter

    # Convert DataFrame to JSON
    json_data = {
        "format_version": "1.0",
        "generated_by": "cytoscape-3.2.0",
        "target_cytoscapejs_version": "~2.1",
        "data": {
            "selected": True,
            "__Annotations": [],
            "shared_name": "I-RegulonNetwork",
            "SUID": 52,
            "name": "I-RegulonNetwork"
        },
        "elements": {
            "nodes": nodes,
            "edges": edges
        }
    }

    # Save JSON data to a file
    output_file_path = f'newdata{i}.json'
    with open(output_file_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

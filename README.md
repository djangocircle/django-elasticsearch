# django-elasticsearch

Curl command to test api:
```
curl --header "Content-Type: application/json"  --request POST  --data '{"index":"project_1","payload": {"test": true}}' http://localhost:8000/ingest
```

Reponse
```
{
    "status": true,
    "data": {
        "_index": "temp_project",
        "_type": "_doc",
        "_id": "406eb3a2-769f-4b71-b331-cb64852844d3",
        "_version": 1,
        "result": "created",
        "_shards": {
            "total": 2,
            "successful": 1,
            "failed": 0
        },
        "_seq_no": 24,
        "_primary_term": 1
    },
    "message": "Document inserted successfully"
}
```
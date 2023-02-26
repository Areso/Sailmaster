#curl -X POST -H "Content-type: application/json" -d '{ "Charname": "test1", "Race": 1, "Gender": 1, "Avatar": 1001 }' localhost:6199/char_create
curl -X POST -H "Content-type: application/json" -d @char_create.json localhost:6199/char_create

import json 

with open("core.json", "r") as file:
    text = file.read()
    result = json.loads(text)
    result["name"] = "Ali"
    print(result)
  
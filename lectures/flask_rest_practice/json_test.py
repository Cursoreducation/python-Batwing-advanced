import json

data = """
    {
        "name": "abc",
        "email": "test@test.com"
    }
"""

result = json.loads(data)
print(result)
print(type(result))


with open("data.json", "r") as f:
    result = json.load(f)
    print(result)
    print(type(result))

def describe(data):
    if isinstance(data, int):
        return f"Integer: {data}"
    elif isinstance(data, float):
        return f"Float: {data}"
    elif isinstance(data, str):
        return f"String: '{data}'"
    elif isinstance(data, list):
        return f"List of length {len(data)}: {data}"
    else:
        return "Unsupported data type"


print(describe(10))
print(describe(15.6))
print(describe("harivarshan"))
print(describe([1, 2, 3, 4, 5]))

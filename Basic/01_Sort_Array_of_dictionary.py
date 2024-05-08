data = [
    {
      "value": 24,
      "valueUnit": "Hours",
      "refund": 0,
      "isPercent": True
    },
    {
      "value": 48,
      "valueUnit": "Hours",
      "refund": 50,
      "isPercent": True
    },
    {
      "value": 72,
      "valueUnit": "Hours",
      "refund": 100,
      "isPercent": True
    }
]

sorted_data = sorted(data, key=lambda x: x["value"], reverse=True)

print(sorted_data)

# Prettify JSON

This program loads json from text file and perform pretty output

# Quickstart

## Example of file with data

test.json
```javascript
[{"WorkingHours":[{"Hours":"09:30-22:30","DayOfWeek":"monday"},{"Hours":"09:30-22:30","DayOfWeek":"вторник"},{"Hours":"09:30-22:30","DayOfWeek":"среда"}]}]'''
```
## Example of  script launch on Linux, Python 3.5:
```$ python pprint_json.py test.json```

## Output 

---
[
  {
    "WorkingHours": [
      {
        "DayOfWeek": "понедельник",
        "Hours": "09:30-22:30"
      },
      {
        "DayOfWeek": "вторник",
        "Hours": "09:30-22:30"
      },
      {
        "DayOfWeek": "среда",
        "Hours": "09:30-22:30"
      }
    ]
  }
]
---


# Project Goals

-The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)

# Prettify JSON

Эта программа загружает json из текстового файла и выводит его на экран

# Quickstart

Example of script launch on Linux, Python 3.5:

```#!bash

#test.json
[{"WorkingHours":[{"Hours":"09:30-22:30","DayOfWeek":"понедельник"},{"Hours":"09:30-22:30","DayOfWeek":"вторник"},{"Hours":"09:30-22:30","DayOfWeek":"среда"}]}]

$ python pprint_json.py test.json
[{u'WorkingHours': [{u'DayOfWeek': u'\u043f\u043e\u043d\u0435\u0434\u0435\u043b\u044c\u043d\u0438\u043a',
                     u'Hours': u'09:30-22:30'},
                    {u'DayOfWeek': u'\u0432\u0442\u043e\u0440\u043d\u0438\u043a',
                     u'Hours': u'09:30-22:30'},
                    {u'DayOfWeek': u'\u0441\u0440\u0435\u0434\u0430',
                     u'Hours': u'09:30-22:30'}]}]

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)

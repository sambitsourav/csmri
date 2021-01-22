test_str = '2021-01-21T16:24:35.842324502-05:00'
from datetime import datetime
test_str = test_str.split('.')[0]
timestamp = datetime.strptime(test_str,"%Y-%m-%dT%H:%M:%S")
print(timestamp)
print(type(timestamp))
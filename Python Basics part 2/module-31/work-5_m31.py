import requests
import re

text = requests.get('http://www.columbia.edu/~fdc/sample.html').text
res = re.findall(r'>.+</h3', text)
result = list(map(lambda x: x[1:-5], res))
print(result)
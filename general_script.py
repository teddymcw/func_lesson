import requests

r = requests.get("http://www.reddit.com/r/Python/comments/1dvc7s/how_to_do_functional_programming_in_python/")

print(r.url)
print(r)
r.text 
r.encoding 
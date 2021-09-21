#This python code used to get the details of Timeline_of_human_vacciness 
import requests

url = "https://en.wikipedia.org:443/wiki/Timeline_of_human_vaccines"
token="eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBJZCI6IjE6NDQ4NjY2NjAxNDQ0OmFuZHJvaWQ6ZjQ0Y2RlNWZjMjU3OTc5NyIsImV4cCI6MTYzMjc0NDQ0OCwiZmlkIjoiYzJ4WFIwWHc2amhkblpjUDIzNCIsInByb2plY3ROdW1iZXIiOjU1ODY2NjYwMTc0Tlgw.AB2LPV8wRQIhAO03xyOZJLN1nP9OgZVAjPghC1j7Ln3Cr4-Xlf1upH9aAiB1lwa_muihNZQ5LiwdG8xsnWPqUny5lDfyFHxLezb8zA"
headers = {"Accept-Encoding": "gzip, deflate", "Accept": "*/*", "Accept-Language": "en", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36", "Connection": "close"}
requests.get(url, headers=headers)

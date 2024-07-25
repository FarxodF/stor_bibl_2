import requests


response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
if response.status_code == 200:
    data = response.json()
    print(f"Title: {data['title']}")
    print(f"Body: {data['body']}")
else:
    print("Ошибка при запросе данных")
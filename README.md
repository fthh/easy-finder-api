
# Запуск

## Без докера

```sh
poetry install
poetry shell
cd src
uvicorn app.main:app --reload --port 9001
```

## С докером

```sh
docker build -t easy-job-find-api .
docker run --name easy-job-api -d -p 9001:9001 easy-job-find-api
```


```sh
docker stop easy-job-api
docker rm easy-job-api
```

http:127.0.0.1:9001/docs

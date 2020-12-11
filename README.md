SQL 検索エンジン
=====


SQLを保存、実行データを検索し表示する  


実行
-----

- Dockerized

```sh
docker build -t dev.local/searcher .
docker run -p 8080:8080 dev.local/searcher
```

- ローカルでの起動

```sh
pipenv install
yarn install
yarn build

# 初回起動時に python から searcher.initialize を実行する

source .env
pipenv run start
```


試しにクエリを投げる

```sh
# クエリの実行
curl -X POST -H "Content-Type: application/json" -d '{"query": "SELECT name FROM user LIMIT 1", "placeholder": []}' localhost:8080/api/v1/query/execute
curl -X POST -H "Content-Type: application/json" -d '{"query": "SELECT name FROM user LIMIT ?", "placeholder": [5]}' localhost:8080/api/v1/query/execute

# クエリの保存
curl -X POST -H "Content-Type: application/json" -d '{"query": "SELECT name FROM user LIMIT 1", "name": "get first user name"}' localhost:8080/api/v1/query/save

# クエリの読み込み
curl -X POST -H "Content-Type: application/json" -d '{"name": "get first user name"}' localhost:8080/api/v1/query/load

# 保存済みクエリの検索
curl -X POST -H "Content-Type: application/json" -d '{"name": "user"}' localhost:8080/api/v1/query/search

# 保存済みクエリの一覧
curl -X GET -H "Content-Type: application/json" localhost:8080/api/v1/query/list
```


TODO
-----

- [x] 検索
- [x] SQLiteで検索クエリの保存
- [ ] クエリのビジュアライズ


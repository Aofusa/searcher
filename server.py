import json
from searcher import searcher


from flask import Flask, render_template, request, jsonify


app = Flask(__name__, static_folder='./dist/static', template_folder='./dist')
app.config["JSON_AS_ASCII"] = False


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')


@app.route('/api/v1/query/execute', methods=['POST'])
def query_execute():

    if request.method == 'POST':
        data = request.data.decode('utf-8')
        data = json.loads(data)

        if 'query' not in data \
            or 'placeholder' not in data:
            return jsonify({"code": "error"})

        query = str(data['query'])
        placeholder = tuple([x for x in data['placeholder']])
        res = searcher.select(query, placeholder)

        return jsonify({"code": "ok", "result": res})

    return jsonify({"code": "error"})


@app.route('/api/v1/query/save', methods=['POST'])
def query_save():

    if request.method == 'POST':
        data = request.data.decode('utf-8')
        data = json.loads(data)

        if 'query' not in data \
            or 'name' not in data:
            return jsonify({"code": "error"})

        query = str(data['query'])
        name = str(data['name'])
        searcher.register(name, query)

        return jsonify({"code": "ok"})

    return jsonify({"code": "error"})


@app.route('/api/v1/query/load', methods=['POST'])
def query_load():

    if request.method == 'POST':
        data = request.data.decode('utf-8')
        data = json.loads(data)

        if 'name' not in data:
            return jsonify({"code": "error"})

        name = str(data['name'])
        res = searcher.load(name)

        return jsonify({"code": "ok", "result": res})

    return jsonify({"code": "error"})


@app.route('/api/v1/query/search', methods=['POST'])
def query_search():

    if request.method == 'POST':
        data = request.data.decode('utf-8')
        data = json.loads(data)

        if 'name' not in data:
            return jsonify({"code": "error"})

        name = str(data['name'])
        res = searcher.search(name)

        return jsonify({"code": "ok", "result": res})

    return jsonify({"code": "error"})


@app.route('/api/v1/query/list', methods=['POST'])
def query_list():

    if request.method == 'POST':
        data = request.data.decode('utf-8')
        data = json.loads(data)
        res = searcher.list()

        return jsonify({"code": "ok", "result": res})

    return jsonify({"code": "error"})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)


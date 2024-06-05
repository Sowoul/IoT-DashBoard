from flask import Flask, render_template, request, jsonify, url_for, request
from dbmngr import DBManager

db = DBManager()
app = Flask(__name__)

def getOrDefault(key, default = None):
    if key in request.args:
        return int(request.args.get(key))
    else:
        return default

@app.route('/')
def index():
    data = get_data()
    return render_template('index.html', data=data)

@app.route('/post', methods=['POST'])
def post():
    if request.method == 'POST':
        idx=getOrDefault('idx', None)
        try:
            fuel,distance = request.form['data'].split(",")
        except:
            return jsonify({'status': 'failure'})
        if not fuel or not distance:
            return jsonify({'status': 'failure'})
        if int(fuel) > 100 or int(fuel) < 0:
            return jsonify({'status': 'failure'})
        db.add_at_idx(idx,{"fuel": fuel, "distance": distance})
        db.save()
        return jsonify({'status': 'success'})
    else:
        return jsonify({'status': 'failure'})

@app.route('/data', methods=['GET'])
def data():
    data = get_data()
    return jsonify(data)

@app.route('/clear', methods=['GET'])
def clear():
    db.clear()
    return jsonify({'status':'success'})

@app.route('/print', methods=['GET'])
def print_data():
    print(db.get_data())
    return jsonify(db.get_data())

@app.route('/current',methods=["GET"])
def print_current():
    return jsonify(db.get_last())

@app.route('/remove',methods=["GET"])
def rm_at_idx():
    idx = request.args.get('idx')
    if not idx:
        return jsonify({'status': 'failure'})
    db.remove_at_idx(int(idx))
    return jsonify({'status': 'success'})

@app.route('/home')
def home():
    return render_template('index.html')
def get_data():
    return db.get_data()

if __name__ == '__main__':
    app.run(debug=True, port=8080)
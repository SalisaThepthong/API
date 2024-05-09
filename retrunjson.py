from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/get_json_data', methods=['GET'])
def get_json_data():
    # สร้างข้อมูล JSON
    data = {
        'name': 'salisa',
        'tel': '0967500569',
        'age': '21'
    }
    # ส่งข้อมูล JSON กลับไปให้ผู้ใช้งาน
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

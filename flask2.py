from flask import Flask, request

app = Flask(__name__)

@app.route('/receive_params', methods=['POST'])
def receive_params():
    # รับข้อมูลพารามิเตอร์จาก URL
    params = request.args.to_dict()
    
    # พิมพ์ข้อมูลพารามิเตอร์ทั้งหมด
    for key, value in params.items(): 
        print(f'{key}: {value}')

    return 'Received parameters successfully!', 200
    
if __name__ == '__main__':
    app.run(debug=True, port=5000)
    
    #api post รับ params แล้ว print ออกมา 

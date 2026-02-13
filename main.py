from flask import Flask, request, jsonify

app = Flask(__name__)

device_ips = {f"phone{i}": [] for i in range(1, 6)}

@app.route('/')
def home():
    return "Running!"

@app.route('/get-all')
def get_all():
    return jsonify(device_ips)

@app.route('/update')
def update_ip():
    device_id = request.args.get('id')
    new_ip = request.args.get('ip')
    if device_id in device_ips:
        if new_ip not in device_ips[device_id]:
            device_ips[device_id].append(new_ip)
        return f"OK", 200
    return "Error", 400

@app.route('/reset-all')
def reset():
    global device_ips
    device_ips = {f"phone{i}": [] for i in range(1, 6)}
    return "Reset OK"

if __name__ == '__main__':
    app.run()

from flask import Flask, jsonify, request
import subprocess
import shlex

app = Flask(__name__)

def run_cli(args):
# args: list or string
if isinstance(args, str):
args = shlex.split(args)
try:
out = subprocess.check_output(["/usr/local/bin/minidsp"] + args, stderr=subprocess.STDOUT, timeout=5)
return out.decode('utf-8', errors='ignore')
except Exception as e:
return str(e)

@app.route('/status', methods=['GET'])
def status():
# Возвращаем preset, input, volume
preset = run_cli(['get', 'preset'])
inp = run_cli(['get', 'input'])
vol = run_cli(['get', 'master-volume'])
return jsonify({
'preset_raw': preset.strip(),
'input_raw': inp.strip(),
'volume_raw': vol.strip()
})

@app.route('/preset', methods=['GET','POST'])
def preset():
if request.method == 'GET':
return jsonify({'preset': run_cli(['get', 'preset']).strip()})
else:
data = request.get_json() or {}
p = data.get('preset')
if p is None:
return jsonify({'error': 'preset missing'}), 400
out = run_cli(['set', 'preset', str(p)])
return jsonify({'result': out.strip()})

@app.route('/input', methods=['GET','POST'])
def input_route():
if request.method == 'GET':
return jsonify({'input': run_cli(['get', 'input']).strip()})
else:
data = request.get_json() or {}
v = data.get('input')
if v is None:
return jsonify({'error': 'input missing'}), 400
out = run_cli(['set', 'input', str(v)])
return jsonify({'result': out.strip()})

@app.route('/volume', methods=['GET','POST'])
def volume_route():
if request.method == 'GET':
return jsonify({'volume': run_cli(['get', 'master-volume']).strip()})
else:
data = request.get_json() or {}
v = data.get('volume')
if v is None:
return jsonify({'error': 'volume missing'}), 400
out = run_cli(['set', 'master-volume', str(v)])
return jsonify({'result': out.strip()})

if __name__ == '__main__':
app.run(host='0.0.0.0', port=8080)

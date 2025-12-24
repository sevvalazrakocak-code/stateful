import os
import json
from flask import Flask, jsonify, render_template

app = Flask(__name__)
DATA_FILE = 'data.json'

# Yardımcı Fonksiyon: Beğeni sayısını dosyadan oku
def read_likes():
    if not os.path.exists(DATA_FILE):
        # Dosya yoksa oluştur ve 0 yaz
        with open(DATA_FILE, 'w') as f:
            json.dump({'likes': 0}, f)
        return 0
    
    with open(DATA_FILE, 'r') as f:
        data = json.load(f)
        return data.get('likes', 0)

# Yardımcı Fonksiyon: Beğeni sayısını dosyaya kaydet
def save_likes(count):
    with open(DATA_FILE, 'w') as f:
        json.dump({'likes': count}, f)

@app.route('/')
def home():
    return render_template('index.html')

# Mevcut sayıyı getiren API
@app.route('/api/get-likes', methods=['GET'])
def get_likes_api():
    count = read_likes()
    return jsonify({'likes': count})

# Beğeni artıran API (POST)
@app.route('/api/like', methods=['POST'])
def like_api():
    current_likes = read_likes()
    new_likes = current_likes + 1
    save_likes(new_likes)  # Dosyaya kalıcı olarak yaz
    return jsonify({'likes': new_likes})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

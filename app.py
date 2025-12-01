from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Path ke folder galeri
    GALLERY_FOLDER = os.path.join(app.root_path, 'static', 'images', 'gallery')
    
    # Cek apakah folder galeri ada — hindari error 500 saat deploy
    if not os.path.exists(GALLERY_FOLDER):
        gallery_files = []
    else:
        gallery_files = [
            f for f in os.listdir(GALLERY_FOLDER)
            if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))
        ]
    
    # Buat data galeri
    gallery_items = []
    for filename in gallery_files:
        # "valorant_tournament.jpg" → "Valorant Tournament"
        title = filename.split('.')[0].replace('_', ' ').title()
        img_url = url_for('static', filename=f'images/gallery/{filename}')
        gallery_items.append({
            "title": title,
            "img": img_url
        })

    return render_template('index.html', gallery=gallery_items)


# ✅ JALANKAN HANYA SAAT DI LOKAL (tidak akan jalan di cloud)
if __name__ == '__main__':
    # Di lokal: boleh pakai debug & port tetap
    app.run(debug=True, host='127.0.0.1', port=5000)
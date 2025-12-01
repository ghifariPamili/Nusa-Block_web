from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Path ke folder galeri
    GALLERY_FOLDER = os.path.join(os.path.dirname(__file__), 'static', 'images', 'gallery')
    
    # Ambil semua gambar
    gallery_files = [f for f in os.listdir(GALLERY_FOLDER) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    
    # Buat data galeri
    gallery_items = []
    for i, filename in enumerate(gallery_files, 1):
        # Jika nama file: "valorant_tournament.jpg" → jadi "Valorant Tournament"
        title = filename.split('.')[0].replace('_', ' ').title()
        img_url = url_for('static', filename=f'images/gallery/{filename}')
        gallery_items.append({
            "title": title,
            "img": img_url
        })

    return render_template('index.html', gallery=gallery_items)

if __name__ == '__main__':
    # 🔑 Wajib untuk Render: baca PORT dari environment variable
    port = int(os.environ.get("PORT", 5000))
    # ❌ Jangan pakai debug=True di production!
    app.run(host="0.0.0.0", port=port)
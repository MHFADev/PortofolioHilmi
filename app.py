import os
from flask import Flask, render_template, request, jsonify
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET")


@app.route('/')
def index():
    """Main portfolio page"""
    return render_template('index.html')


@app.route('/gallery/<gallery_type>')
def gallery(gallery_type):
    """Gallery pages for different project types"""
    if gallery_type not in ['coding']:
        return render_template('index.html')

    gallery_data = {
        'coding': {
            'title':
            'Album Proyek Web Development',
            'description':
            'Dokumentasi visual dari perjalanan pengembangan web saya menggunakan HTML, CSS, JavaScript, React, Next.js, dan Python. Setiap gambar menceritakan proses belajar dan menciptakan solusi digital.',
            'images': [{
                'url':
                'https://raw.githubusercontent.com/MHFADev/asset/refs/heads/main/Capture.PNG',
                'title':
                'Mengembangkan Website dengan React',
                'description':
                'Proses coding menggunakan Html, CSS, dan JavaScript, dan Python'
            }, {
                'url':
                'https://images.unsplash.com/photo-1547658719-da2b51169166?ixlib=rb-4.0.3&auto=format&fit=crop&w=1064&q=80',
                'title':
                'Kolaborasi Tim',
                'description':
                'Berdiskusi dengan teman tentang solusi coding'
            }, {
                'url':
                'https://images.unsplash.com/photo-1517694712202-14dd9538aa97?ixlib=rb-4.0.3&auto=format&fit=crop&w=1170&q=80',
                'title':
                'Debugging Session',
                'description':
                'Menyelesaikan masalah kode kompleks dengan Git'
            }]
        }
    }

    return render_template('gallery.html',
                           gallery_type=gallery_type,
                           data=gallery_data[gallery_type])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

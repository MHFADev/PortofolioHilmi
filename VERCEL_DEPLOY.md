# Panduan Deploy ke Vercel

Aplikasi Flask ini sudah disiapkan untuk di-deploy ke Vercel. Ikuti langkah-langkah berikut:

## Persiapan File

File-file berikut sudah dibuat:
- ✅ `vercel.json` - Konfigurasi Vercel
- ✅ `requirements.txt` - Dependencies Python

## Langkah-langkah Deploy

### 1. Persiapan Akun Vercel
1. Buat akun di [vercel.com](https://vercel.com)
2. Install Vercel CLI (opsional):
   ```bash
   npm i -g vercel
   ```

### 2. Deploy via Vercel Dashboard (Cara Termudah)

1. Login ke [vercel.com](https://vercel.com)
2. Klik "Add New Project"
3. Import repository Git Anda (GitHub/GitLab/Bitbucket)
4. Vercel akan otomatis mendeteksi konfigurasi
5. Klik "Deploy"

### 3. Deploy via Vercel CLI

Dari terminal, jalankan:
```bash
vercel
```

Ikuti instruksi interaktif yang muncul.

### 4. Deploy Production

```bash
vercel --prod
```

## Catatan Penting

### Database
⚠️ **Perhatian**: Aplikasi ini menggunakan PostgreSQL. Untuk Vercel, Anda perlu:

1. **Gunakan database eksternal** seperti:
   - Supabase (gratis)
   - Neon (gratis)
   - Railway
   - PlanetScale

2. **Set environment variable** di Vercel Dashboard:
   - `DATABASE_URL` - Connection string database Anda
   - `SESSION_SECRET` - Secret key untuk Flask session

### Environment Variables

Tambahkan di Vercel Dashboard → Settings → Environment Variables:
- `DATABASE_URL` - Database connection string
- `SESSION_SECRET` - Secret untuk session (buat string random)

### Batasan Vercel

- Vercel menggunakan **serverless functions**
- Setiap request berjalan dalam function terpisah
- Tidak ada persistent connections
- Waktu eksekusi maksimal: 10 detik (hobby plan)

## Alternatif: Deploy di Replit

Jika Anda ingin deployment yang lebih mudah dengan database terintegrasi, Anda bisa menggunakan Replit Publishing:

1. Aplikasi sudah berjalan di Replit
2. Database PostgreSQL sudah tersedia
3. Tinggal klik tombol "Publish" di Replit

## Troubleshooting

### Error: Module not found
- Pastikan semua dependencies ada di `requirements.txt`

### Error: Database connection failed
- Pastikan environment variable `DATABASE_URL` sudah di-set
- Gunakan connection string dengan SSL enabled

### Error: Cold start timeout
- Pertimbangkan upgrade ke Vercel Pro
- Atau gunakan platform lain seperti Railway atau Fly.io

## Resources

- [Vercel Python Docs](https://vercel.com/docs/functions/serverless-functions/runtimes/python)
- [Flask Deployment Guide](https://flask.palletsprojects.com/en/stable/deploying/)

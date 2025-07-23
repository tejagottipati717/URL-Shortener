# URL Shortener Project

This is a simple URL shortening service built using Python and Flask.  
It allows users to shorten long URLs, redirect using short codes, and view click analytics for each link.

---

## 🚀 Features

- 🔗 Shorten any valid URL to a 6-character alphanumeric code
- 📥 Redirect from the short code to the original long URL
- 📊 Track click count and creation timestamp for each short URL
- ✅ Validates input URLs (must be HTTP/HTTPS)
- 🧠 Thread-safe, in-memory storage (no database required)
- 🧪 Unit tested using `pytest`

---

## 📦 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

---

## ⚙️ Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/url-shortener.git
   cd url-shortener
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

---

## 💡 Usage

1. Start the Flask server:
   ```
   python -m flask --app app.main run
   ```

2. The API will be available at:  
   📍 `http://localhost:5000`

---

## 📬 API Endpoints

### ➕ Shorten a URL
```
POST /api/shorten
```
**Body:**
```
{
  "url": "https://www.example.com/very/long/url"
}
```
**Response:**
```
{
  "short_code": "abc123",
  "short_url": "http://localhost:5000/abc123"
}
```

---

### 🔁 Redirect to Original URL
```
GET /<short_code>
```
Redirects to the original long URL.  
Returns 404 if the short code is invalid.

---

### 📊 View Analytics
```
GET /api/stats/<short_code>
```
**Response:**
```
{
  "url": "https://www.example.com/very/long/url",
  "clicks": 5,
  "created_at": "2025-07-23T12:45:00"
}
```

---

## 🧪 Running Tests

To run all tests using `pytest`:

```
pytest
```

📝 All core features are tested: URL shortening, redirection, invalid cases, and analytics.

---

## 📁 Project Structure

```
url-shortener/
├── app/
│   ├── __init__.py
│   ├── main.py         # Main Flask routes
│   ├── storage.py      # In-memory URL storage with click tracking
│   └── utils.py        # Short code generation and URL validation
├── tests/
│   └── test_main.py    # Unit tests with pytest
├── requirements.txt
├── README.md
└── NOTES.md (optional)
```

---

## 📌 Notes

- This assignment was completed without a database; data is stored in memory and resets when the server restarts.
- Fully compatible with concurrency using `threading.Lock`.
- No user accounts or authentication as per instructions.
- Compliant with assignment specs from Retainsure.

---

## 📤 Deployment

This is a development-only version.

---

## 🧑‍💻 Author

- Name: **Teja Gottipati**
- GitHub: https://github.com/tejagottipati717
- Email: tejateja717@gmail.com

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).



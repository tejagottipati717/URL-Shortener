import threading
from datetime import datetime

class URLStore:
    def __init__(self):
        self.data = {}
        self.lock = threading.Lock()

    def save(self, short_code, original_url):
        with self.lock:
            self.data[short_code] = {
                "url": original_url,
                "clicks": 0,
                "created_at": datetime.utcnow().isoformat()
            }

    def get(self, short_code):
        return self.data.get(short_code)

    def increment_click(self, short_code):
        with self.lock:
            if short_code in self.data:
                self.data[short_code]["clicks"] += 1

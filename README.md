## 🔑 Google OAuth 2.0 + JWT Authentication Setup
```bash
---Packages---

itsdangerous
httpx
authlib
python-dotenv
PyJWT

📄.env Configuration
Create a .env file in the project root:

GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
GOOGLE_REDIRECT_URI=http://localhost:8000/auth/callback

SECRET_KEY=super_secret_change_me
JWT_EXPIRE_SECONDS=3600

📝 Replace your_google_client_id and your_google_client_secret with credentials 
from the Google Cloud Console.

---Middleware---

load_dotenv()

app.add_middleware(
    SessionMiddleware,
    secret_key=os.getenv("SECRET_KEY")
)
```

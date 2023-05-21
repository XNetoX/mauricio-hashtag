from config import AppConfig
from src.factory import create_app

app = create_app(AppConfig())


if __name__ == "__main__":
    app.run(debug=True, port=5001)

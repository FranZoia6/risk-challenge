from config import Config
from src import init_app

app = init_app(Config)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

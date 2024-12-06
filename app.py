from config import app
from routes.planets import planets_bp
from routes.films import films_bp

app.register_blueprint(planets_bp)
app.register_blueprint(films_bp)

if __name__ == '__main__':
    app.run(debug=True)
from Controllers import createBlueprint
from Models import createDatabase
from app import createApp, db

# configuration
DEBUG = True

app=createApp()
blueprint = createBlueprint()
app.register_blueprint(blueprint, url_prefix='/api/v1')





if __name__ == '__main__':
    app.run(debug=DEBUG,host="0.0.0.0")
from flask import Flask, render_template, jsonify, redirect
import pymongo
import scrape_mars

app = Flask(__name__)

mongo = pymongo(app, uri="mongodb://localhost:27017/mars")

@app.route("/" )
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)


@app.route('/scrape')
def scrape():
    mars = mongo.db.mars_db
    data = scrape_mars.scrape_all()
    mars.update({}, data, upsert=True)
    return "Scraping Successful!"


if __name__ == "__main__":
    app.run(debug=True)


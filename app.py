import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt

from flask import Flask, jsonify, render_template

#################################################
# Database Setup
#################################################
engine = create_engine(r"sqlite:///Data\great_resignation.db")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save reference to the table
linechartdata = Base.classes.linechartdata
databystatemarch2023 = Base.classes.databystatemarch2023
top5industryannualquitrates = Base.classes.top5industryannualquitrates
highestquitratesbystate = Base.classes.highestquitratesbystate
sectorquits = Base.classes.sectorquits

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
    """
    Render the main page of the webapp.
    """
    return render_template('index.html')

@app.route("/api/v1.0/industry_covid19")
def industry_covid19():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    """Return a list of all industry names"""
    # Query all
    results = session.query(top5industryannualquitrates.Industry).all()
    session.close()
    # Convert list of tuples into normal list
    all_industry = list(np.ravel(results))
    return jsonify(all_industry)

@app.route("/api/v1.0/quitrates_covid19_byindustry")
def quitrates_covid19_byindustry():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    """Return a list of quitrates in 2018-2022 by industry"""
    # Query all 
    results2 = session.query(top5industryannualquitrates.Industry, top5industryannualquitrates.column_2018, top5industryannualquitrates.column_2019, top5industryannualquitrates.column_2020, top5industryannualquitrates.column_2021, top5industryannualquitrates.column_2022).all()
    session.close()
    # Create a dictionary from the row data and append to a list of all_rates
    all_quitrates = []
    for Industry, column_2018, column_2019, column_2020, column_2021, column_2022 in results2:
        quitrates_covid19_dict = {}
        quitrates_covid19_dict["Industry"] = Industry
        quitrates_covid19_dict["2018"] = column_2018
        quitrates_covid19_dict["2019"] = column_2019
        quitrates_covid19_dict["2020"] = column_2020
        quitrates_covid19_dict["2021"] = column_2021
        quitrates_covid19_dict["2022"] = column_2022
        all_quitrates.append(quitrates_covid19_dict)

    return jsonify(all_quitrates)


if __name__ == "__main__":
    app.run(debug=True)

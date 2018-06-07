# Dependencies
import pandas as pd
import os
import numpy as np
from flask import (
    Flask,
    render_template,
    jsonify,
    request)

from flask_sqlalchemy import SQLAlchemy

# Store filepath in a variable
file_one = os.path.join("db", "Belly_Button_Biodiversity_Metadata.csv")
file_two = os.path.join("db", "belly_button_biodiversity_otu_id.csv")
file_three = os.path.join("db", "belly_button_biodiversity_samples.csv")
file_four = os.path.join("db", "metadata_columns.csv")

# Read our Data file with the pandas library
# Not every CSV requires an encoding, but be aware this can come up
metadata_df = pd.read_csv(file_one, encoding="ISO-8859-1")
otu_id_df = pd.read_csv(file_two, encoding="ISO-8859-1")
samples_df = pd.read_csv(file_three, encoding="ISO-8859-1")
columns_df = pd.read_csv(file_four, encoding="ISO-8859-1")

samples_names_list = list(samples_df.columns.values)
samples_names_list.pop(0)

# metadata_df = metadata_df.set_index("SAMPLEID")

# giving_value = metadata_df.loc["BA_940"]


df_filtered = metadata_df[(metadata_df["SAMPLEID"] == int(940)) & metadata_df["SAMPLEID"] == int(941)]

print(df_filtered["AGE"])

filtered_result = {
        "AGE": df_filtered["AGE"],
        "BBTYPE": df_filtered["BBTYPE"],
        "ETHNICITY": df_filtered["ETHNICITY"],
        "GENDER": df_filtered["GENDER"],
        "LOCATION": df_filtered["LOCATION"],
        "SAMPLEID": df_filtered["SAMPLEID"]
}

filtered_result_list = list(filtered_result)


# print(metadata_df.index.values)

otu_list = list(otu_id_df["lowest_taxonomic_unit_found"])

# Flask Setup
#################################################
app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome!"


@app.route("/names")
def names():
    return jsonify(samples_names_list)


@app.route("/otu")
def otu():
    return jsonify(otu_list)

@app.route("/metadata")
def metadata():
    return jsonify(filtered_result_list)

#run the app
if __name__ == '__main__':
    app.run(debug=True)


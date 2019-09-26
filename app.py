from flask import Flask, render_template
from flask import request
from get_top_data import GetTopValues

app = Flask(__name__)


@app.route("/top-<n>_hotels/<user_id>", methods=['GET'])
def get_top_n_hotels(n, user_id):
    if request.method == 'GET':
        top_n_hotels = GetTopValues().get_top_hotels(int(user_id), int(n), 1)
        if top_n_hotels is None:
            top_n_hotels = [{'hotel_id': "", 'count': "user_id doesn't exist"}]
        return render_template('record.html', n=n, name="Hotel",
                               records=top_n_hotels, colnames=['hotel_id', 'count'])


@app.route("/top-<k>_amenities/<user_id>", methods=['GET'])
def get_top_k_amenities(k, user_id):
    if request.method == 'GET':
        top_k_amenities = GetTopValues().get_top_amenities(int(user_id), int(k), 1)
        if top_k_amenities is None:
            top_k_amenities = [{'amenity_id': "", 'count': "user_id doesn't exist"}]
        return render_template('record.html', n=k, name="Amenity",
                               records=top_k_amenities, colnames=['amenity_id', 'count'])


@app.route("/top-<n>_hotels&top-<k>_amenities/<user_id>", methods=['GET'])
def get_top_n_k(n, k, user_id):
    if request.method == 'GET':
        top_n_hotels = GetTopValues().get_top_hotels(int(user_id), int(n), 2)
        top_k_amenities = GetTopValues().get_top_amenities(int(user_id), int(k), 2)

        if top_n_hotels is None:
            top_n_hotels = [{'hotel_id': "", 'count': "user_id doesn't exist"}]
        if top_k_amenities is None:
            top_k_amenities = [{'amenity_id': "", 'count': "user_id doesn't exist"}]
        return render_template('both_data.html', n=n, k=k,
                               records1=top_n_hotels,
                               colnames1=['hotel_id', 'count'],
                               records2=top_k_amenities,
                               colnames2=['amenity_id', 'count'])


if __name__ == '__main__':
    app.run(debug=True)


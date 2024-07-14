from flask import Flask, jsonify, request

app = Flask(__name__)

data = {}
id_counter = 1  # Memulai ID dari 1

@app.route('/', methods=['GET', 'POST'])
def manage_data():
    global id_counter  # Gunakan variabel global untuk counter ID
    if request.method == 'POST':
        req_data = request.json
        # Membuat ID yang selalu bertambah dan memastikan selalu dalam format tiga digit
        new_id = f"{id_counter:03}"  # Format ID menjadi tiga digit, misalnya "001"
        data[new_id] = {
            "id_pembuat": new_id,
            "nama_pembuat": req_data.get("nama_pembuat", ""),
            "fokus_penelitian": req_data.get("fokus_penelitian", ""),
            "tempat_penelitian": req_data.get("tempat_penelitian", ""),
            "periode_penelitian": req_data.get("periode_penelitian", ""),
            "tujuan_penelitian": req_data.get("tujuan_penelitian", ""),
            "prosedur_penelitian": req_data.get("prosedur_penelitian", [])
        }
        id_counter += 1  # Tambahkan counter setelah setiap entri
        return jsonify({"message": "Data added successfully", "id": new_id, "data": data[new_id]}), 201

    else:
        # Menampilkan semua data
        return jsonify(data)

@app.route('/<id>', methods=['GET', 'DELETE'])
def handle_data_by_id(id):
    if request.method == 'DELETE':
        # Menghapus data berdasarkan ID
        if id in data:
            del data[id]
            return jsonify({"message": "Data deleted successfully"}), 200
        else:
            return jsonify({"message": "Data not found"}), 404

    else:
        # Menampilkan data berdasarkan ID
        if id in data:
            return jsonify(data[id])
        else:
            return jsonify({"message": "Data not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)

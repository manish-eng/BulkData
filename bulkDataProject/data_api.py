from flask import Blueprint
from influxdb import InfluxDBClient
from flask import jsonify,request

main = Blueprint('main',__name__)

def create_influxDBClient():
    client = InfluxDBClient(host='localhost', port=8086, username='myuser', password='mypass' ssl=True, verify_ssl=True)
    return client

@main.route('/api/bulk-data', methods=['GET'])
def getAllData():
    try:
        client = create_influxDBClient()
        results = client.query('SELECT * FROM "bulk_ata"."data_center" ')
        return jsonify({'results':results})
    except Exception as e:
        return e

@main.route('/api/bulk-data', methods=['POST'])
def createEntry():
    try:
        client = create_influxDBClient()
        data = request.get_json()
        status = client.write_points(data)
        if status is True:
            return  'Status : 200 Record Inserted Successfully'
    except Exception as e:
        return e




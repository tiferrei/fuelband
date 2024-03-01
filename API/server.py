from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/v1.0/device/imprint', methods=["POST"])
def imprint():
    data = {
        "userDeviceId": "42424242424242",
        "din": "42424242424242",
        "udi": "42424242424242",
        "deviceName": "FuelBand",
        "deviceString": "FuelBand",
        "serialNo": "4242424242424242",
        "color": "GREEN",
        "firmwareVersion": "A0.46.2296a",
        "softwareVersion": "A0.46.2296a",
        "carrier": "telecom"

    }
    return jsonify(data)


@app.route('/v1.0/device/onetimetoken', methods=["GET"])
def onetimetoken():
    data = {"onetimetoken": "ABCDEF"}
    return jsonify(data)


events = []


@app.route('/plus/setup/ABCDEF', methods=["GET"])
def setup():
    global events
    print("Injecting setup complete event...")
    events.append({"status": "success",
                   "id": "setup",
                   "eventType": "setup_complete",
                   "payload": "{\"dailyGoal\": 2000.0, \"nextDailyGoal\": 2000.0, \"band_name\": \"FuelBand\"}"})
    return "Injecting setup complete event..."


@app.route('/events/connect/42424242424242', methods=["GET"])
def get_events():
    global events
    print("sending events: ", events)
    data = {"status": "success", "events": events}
    return jsonify(data)


@app.route('/events/connect/42424242424242/ack/<id>', methods=["POST"])
def ack_events(id):
    print("request POST data:", request.get_json())
    global events
    events = list(filter(lambda e: e["id"] != id, events))
    print("sending acked events: ", events)
    data = {"status": "success", "events": events}
    return jsonify(data)


@app.route('/map/getAccessToken', methods=["GET"])
def accesstoken():
    data = {"access_token": "accesstoken",
            "expires_in": "10000000",
            "refresh_token": "refreshtoken"}
    return jsonify(data)


@app.route('/plus/v1.0/remotelogs/email', methods=["POST"])
def email():
    return "OK"


@app.route('/v1.0/me/profile', methods=["GET"])
def profile():
    data = {"success": "true",
            "screenName": "John",
            "firstName": "John",
            "lastName": "Doe",
            "email": "john@example.com",
            "weight": 70.0,
            "height": 180.0,
            "gender": "male",
            "dateOfBirth": 315619200000,
            "dailyGoal": 2000.0,
            "pin": "",
            "deviceList": [{'deviceString': "FuelBand", 'deviceType': 'FUELBAND2'}]}
    return jsonify(data)

@app.route('/v1.0/me/challenge/dailygoal/list', methods=["GET"])
def daily_goal():
    data = {"success": "true",
            "dailyGoalList": [{"challengeId": "CHALLENGE", "startTime": int(request.args.get("startTime")), "endTime": int(request.args.get("endTime")), "targetValue": 2000.0}]}
    return jsonify(data)


@app.route('/v1.0/me/activities/summary/daily/<day>', methods=["GET"])
def daily_summary(day):
    data = {"success": "true",
            "summary": {}}
    return jsonify(data)


@app.route('/v1.0/me/device/42424242424242', methods=["GET", "PUT"])
def device_info():
    data = {"success": "true",
            "din": "42424242424242",
            "serialNumber": "4242424242424242",
            "deviceType": "FUELBAND2",
            "deviceSring": "FuelBand"}
    return jsonify(data)

@app.route('/v1.0/me/device/42424242424242/settings', methods=["GET"])
def device_prefs():
    data = {"success": "true",
            "preference": {
                "FUELBANDSTEPS": 1234,
                "FUELBANDCALORIES": 1000,
                "FUELBANDFUEL": 4321,   
                "FUELBANDISLEFTORIENTATION": 1,   
            }}
    return jsonify(data)


@app.route('/me/account', methods=["GET"])
def account():
    data = {"success": "true",
            "entity": {"firstName": "John",
                       "heightUnit": "cm",
                       "weightUnit": "kg"},
            "firstName": "John",
            "heightUnit": "cm",
            "weightUnit": "kg"}
    return jsonify(data)


@app.route('/v1.0/me/sync/lasttimestamp', methods=["GET"])
def sync_params():
    data = {"success": "true",
            "upmid": "UPMID",
            "plusid": "PLSUID",
            "lastSyncOffset": 0,
            "lastSyncTimeStamp": 0}
    return jsonify(data)


@app.route('/v1.0/me/challenge', methods=["POST"])
def challenge():
    data = {"success": "true",
            "result": "success",
            "challengeId": "CHALLENGE",
            "challengeType": request.get_json()["challengeType"],
            "dailyGoalDate": request.get_json()["dailyGoalDate"],
            "dstOffset": request.get_json()["dstOffset"],
            "targetValue": request.get_json()["targetValue"],
            "tzOffset": request.get_json()["tzOffset"]}
    return jsonify(data)


# TODO
# GET Important to allow data to be cleared before timestamp.
"/v1.0/me/sync/lasttimestamp"
# POST sync data.
"/v2.0/me/sync"

@app.route('/<path:path>', methods=["GET", "POST", "PUT"])
def catch_all(path):
    print("PATH:", path)
    print("DATA:", request.get_json())
    data = {"success": "true",
            "result": "success"}
    return jsonify(data)


if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=3000)

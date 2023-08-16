from flask import Flask, request, abort
import db

app = Flask(__name__)
paste_collection = db.get_paste_collection()

@app.route("/paste/<string:paste_id>", methods=['GET'])
def get_paste(paste_id):
    # TODO: create result type
    paste_result = db.get_paste(paste_collection, paste_id)
    if paste_result:
        return {"status":"ok", "result": paste_result}
    else:
        return {"status":"not_found", "result": None}
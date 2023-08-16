from flask import Flask, request, abort
import db

app = Flask(__name__)
paste_collection = db.get_paste_collection()

@app.route("/paste/<string:paste_id>", methods=['GET'])
def get_paste(paste_id):
    # TODO: create get result type
    paste_result = db.get_paste(paste_collection, paste_id)
    if paste_result:
        return {"status":"ok", "result": paste_result}
    else:
        return {"status":"not_found", "result": None}


# curl -X POST -d "content=test paste" -d "s3_key=" -d "expires=12341123" -d "is_exploading=false" -d "is_encrypted=false" 'http://127.0.0.1:5000/paste'
@app.route("/paste", methods=['POST'])
def insert_paste():
    content = request.form['content']
    expires = int(request.form['expires'])
    is_exploading = request.form['is_exploading'].lower() == 'true'
    is_encrypted = request.form['is_encrypted'].lower() == 'true'

    paste = db.create_paste(content=content, expires=expires, 
                            is_exploading=is_exploading, is_encrypted=is_encrypted)
    # TODO: create post result type
    insert_status, insert_result = db.insert_paste(paste_collection, paste)
    if insert_status:
        return {"status":"ok", "id":insert_result}
    else:
        return {"status":"error", "id":None}
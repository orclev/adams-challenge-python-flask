#!/usr/bin/python2
import json
import redis
from flask import Flask, abort
app = Flask(__name__)
pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)

@app.route("/users")
def users():
  return json.dumps([json.loads(item) for item in r.smembers('users')])

@app.route("/user/<userid>")
def user(userid):
  user = r.get('user:' + userid)
  return user if user != None else abort(404)
  
if __name__ == "__main__":
    app.run()

from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, snake_case_fallback_resolvers, ObjectType
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify

from api.queries import listKillTeams_resolver, getKillTeam_resolver

import os

from flask import Flask
from flask_cors import CORS
from api import db
app = Flask(__name__)
CORS(app)

db_url = os.getenv('DB_URL')
app.config["SQLALCHEMY_DATABASE_URI"] = db_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


query = ObjectType("Query")
query.set_field("listKillTeams", listKillTeams_resolver)
query.set_field("getKillTeam", getKillTeam_resolver)

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, query, snake_case_fallback_resolvers
)


@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code
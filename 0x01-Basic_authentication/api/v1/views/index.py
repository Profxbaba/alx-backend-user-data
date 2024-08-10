#!/usr/bin/env python3
"""Module defining index routes for the API."""

from flask import abort, Blueprint

app_views = Blueprint('app_views', __name__)

@app_views.route('/api/v1/unauthorized', methods=['GET'])
def unauthorized():
    """Endpoint that triggers a 401 Unauthorized error."""
    abort(401)

from chalice import Chalice, BadRequestError

'''
# Exception Types
# * BadRequestError - return a status code of 400
# * UnauthorizedError - return a status code of 401
# * ForbiddenError - return a status code of 403
# * NotFoundError - return a status code of 404
# * ConflictError - return a status code of 409
# * UnprocessableEntityError - return a status code of 422
# * TooManyRequestsError - return a status code of 429
# * ChaliceViewError - return a status code of 500
'''

app = Chalice(app_name='chalice-helloworld')

app.debug = True

CITIES_TO_STATE = {
    'seattle': 'WA',
    'portland': 'OR',
}

@app.route('/')
def index():
    return {'hello': 'world'}

@app.route('/resource/{value}', methods=['PUT'])
def put_test(value):
    return {"value": f"PUT {value}"}

@app.route('/resource/{value}', methods=['GET'])
def put_test(value):
    return {"value": f"GET {value}"}

@app.route('/resource/{value}', methods=['POST'])
def put_test(value):
    return {"value": f"POST {value}"}

'''
# Current Requests
current_request.query_params - A dict of the query params for the request.
current_request.headers - A dict of the request headers.
current_request.uri_params - A dict of the captured URI params.
current_request.method - The HTTP method (as a string).
current_request.json_body - The parsed JSON body (json.loads(raw_body))
current_request.raw_body - The raw HTTP body as bytes.
current_request.context - A dict of additional context information
current_request.stage_vars - Configuration for the API Gateway stage
'''

@app.route('/route_w_requests/')
def route_w_requests():
    request = app.current_request

    return {"value": request}

@app.route('/cities/{city}')
def state_of_city(city):
    try:
        return {'state': CITIES_TO_STATE[city]}
    except KeyError:
        raise BadRequestError("Unknown city '%s', valid choices are: %s" % (
            city, ', '.join(CITIES_TO_STATE.keys())))

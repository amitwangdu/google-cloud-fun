def hello_world(request):
    request_args = request.args
    request_jason = request.get_json(silent=True)
    if request_args and 'name' in request_args and 'lastname' in request_args:
        name = request_args['name']
        lastname = request_args['lastname']
    elif request_jason and 'name' in request_jason and 'lastname' in request_jason:
        name = request_jason['name']
        lastname = request_jason['lastname']
    else:
        name = 'World'
        lastname = ''
    return f'Hello {name} {lastname}'

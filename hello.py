def application_func(environ, start_response):
    status = '200 OK'
    response_headers = [
	('Content-type', 'text/plain')
    ]


    body = list(bytes(key + '\n', 'ascii') for key in environ['QUERY_STRING'].split('&'))
    start_response(status, response_headers)
    return body

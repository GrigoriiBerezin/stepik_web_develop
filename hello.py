def application(environ, start_response):
    status = '200 OK'
    response_headers = [
	('Content-type', 'text/plain')
    ]


    body = bytes('\r\n'.join(environ['QUERY_STRING'].split('&')), encoding='utf8')
    start_response(status, response_headers)
    return [body]

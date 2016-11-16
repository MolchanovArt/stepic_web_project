from cgi import parse


def application(environ, start_response):
    query = parse(environ['QUERY_STRING'], keep_blank_values=True)
    body = []
    for key, values in query.items():
        for item in values:
            body.append(key + "=" + item + "\r\n")

    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
    ]

    start_response(status, headers)
    return body

import requests


# Defining root URL for HTTP Requests
root_url = 'http://jsonplaceholder.typicode.com'

# Defining full URL for HTTP Requests
full_url = root_url + '/posts/1'


########################################################
# Sending HTTP Request and and getting HTTP Response
resp = requests.get(full_url)
########################################################


# Storing Integer HTTP Status Code from HTTP Response
resp_status_code_int = resp.status_code

# Converting Integer HTTP Status Code to String
resp_status_code_str = str(resp_status_code_int)

# Parsing JSON from HTTP Response
parsed_resp = resp.json()


# Printing HTTP Response
print 'HTTP Status Code:'
print resp_status_code_str

print
print 'HTTP Headers: '
print resp.headers

print
print 'HTTP Body: '
print parsed_resp

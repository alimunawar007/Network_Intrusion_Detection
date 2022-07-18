import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'src_bytes', 'dst_host_srv_rerror_rate', 'count', 'protocol_type_tcp',
       'protocol_type_udp'})

print(r.json())



from clarifai import rest
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

import json
from pprint import pprint

app = ClarifaiApp(api_key='')

model = app.models.get("general-v1.3")
response = model.predict_by_filename('C:\Users\greg\Documents\MycroftDevelopment\skill-smart-eye\TestImages\Butterfly.jpg',min_value=0.98)

j = json.dumps(response['outputs'][0],separators=(',',': '),indent=3)
jl = json.loads(j)

print type(jl)
index = 0

for each in jl['data']['concepts']:
    print jl['data']['concepts'][index]['name']
    index = index +1

import requests

API_ENDPOINT = 'https://api.lotlinx.com/photoai/v1/optimize'
#
# data = {
#         'values':[
#             {
#         "dealerId": "12345",
#         "vehicleImageSets": [
#             {
#                 "id": 55,
#                 "imageSet": [
#                     {
#                         "imageId": 91,
#                         "imageUrl": "https://img.lotlinx.com/vdn/7416/jeep_wrangler%20unlimited_2014_1C4BJWFG3EL326863_7416_339187295.jpg"
#                     },
#                     {
#                         "imageId": 97,
#                         "imageUrl": "https://img.lotlinx.com/vdn/7416/jeep_wrangler%20unlimited_2014_1C4BJWFG3EL326863_7416_5_339187295.jpg"
#                     }
#
#                 ]
#             }
#         ]
#     }
#     ]
# }
# r = requests.get(url=API_ENDPOINT, json = data, auth=('testaccount4', 'b784dd85d16b'))
# response_object = r.json()
#
#
#
# print(response_object)



body = {
        'values':[{
        'dealerId': "DEALER_ID",
        'vehicleImageSets':[
                {
                'id': "VEHICLE_ID",
                'images' : list()
                    }
                ]
            }
        ]
    }


images = [
    {
        "id": 0,
        "url": "https://img.lotlinx.com/vdn/7416/jeep_wrangler%20unlimited_2014_1C4BJWFG3EL326863_7416_339187295.jpg"
    },
    {
        "id": 1,
        "url": "https://img.lotlinx.com/vdn/7416/jeep_wrangler%20unlimited_2014_1C4BJWFG3EL326863_7416_2_339187295.jpg"
    },
    {
        "id": 2,
        "url": "https://img.lotlinx.com/vdn/7416/jeep_wrangler%20unlimited_2014_1C4BJWFG3EL326863_7416_3_339187295.jpg"
    },
    {
        "id": 3,
        "url": "https://img.lotlinx.com/vdn/7416/jeep_wrangler%20unlimited_2014_1C4BJWFG3EL326863_7416_4_339187295.jpg"
    },
    {
        "id": 4,
        "url": "https://img.lotlinx.com/vdn/7416/jeep_wrangler%20unlimited_2014_1C4BJWFG3EL326863_7416_5_339187295.jpg"
    }
]

for image in images:
    body['values'][0]['vehicleImageSets'][0]['images'].append({
        'imageId': image['id'],
        'imageUrl': image['url']
    })


print(body['values'][0]['vehicleImageSets'][0])


# import requests
#
# API_ENDPOINT = 'https://api.lotlinx.com/photoai/v1/optimize'
#
# data = {
#         'values':[
#             {
#         "dealerId": "12345",
#         "vehicleImageSets": [
#             {
#                 "id": 55,
#                 "imageSet": [
#                     {
#                         "imageId": 91,
#                         "imageUrl": "https://img.lotlinx.com/vdn/7416/jeep_wrangler%20unlimited_2014_1C4BJWFG3EL326863_7416_339187295.jpg"
#                     }
#                 ]
#             }
#         ]
#     }
#     ]
# }
# r = requests.post(url=API_ENDPOINT, data=data, auth=('testaccount4', 'b784dd85d16b'))
# response_object = r
#
# print(response_object)
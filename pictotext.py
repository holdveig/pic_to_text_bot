import base64
import json
import requests

def picture_to_text(path_to_picture):
    folder_id = "b1go1cpmpdmlcasa6f8b"  # paste here!

    def encode_file(filename):
      with open(filename, 'rb') as f:
          file_content = f.read()
      return base64.b64encode(file_content)

    image_base64 = encode_file(path_to_picture)

    body = {
        "folderId": folder_id,
        "analyze_specs": [{
            "content": image_base64.decode('utf-8'),
            "features": [{
                "type": "TEXT_DETECTION",
                "text_detection_config": {
                    "language_codes": ["*"]
                }
            }]
        }]
    }

    body = json.dumps(body)

    # paste here!
    key = "AQVNz20WL8ZSID002jT0vIxEBhfw3PtuMzI5fVJY"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Api-Key {}'.format(key),
    }


    api_endpoint_url = "https://vision.api.cloud.yandex.net" +\
                        "/vision/v1/batchAnalyze"

    response = requests.post(api_endpoint_url, 
                             headers=headers, data=body)

    a=response.text #тут я пытаюсь из ответа вытащить номер аудитории
    aspl=a.split("\n")
    nomer=""
    for i in aspl:
        if "text" in i:
            for j in i:
                if j in "0123456789":
                    nomer=nomer+j
    return(nomer)

def saving_pic(): 
    return 'Picture was saved successfully'
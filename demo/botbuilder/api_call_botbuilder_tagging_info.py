import requests
import json, os
url = "{0}:{1}".format(os.environ['HOSTNAME'] , "8000")

resp = requests.post('http://' + url + '/api/v1/type/service/botbuilder/tagging/',
                     json={
                        "cb_id": "cb0001",
                        "pos_type": "dict",
                        "proper_noun": {"tagdate": [1, "/hoya_model_root/chatbot/date.txt", False],
                                        "tagloc": [1, "/hoya_model_root/chatbot/loc.txt", False],
                                         "tagmenu": [3, "/hoya_model_root/chatbot/menu.txt", False]
                                        }

                     })
data = json.loads(resp.json())
print("evaluation result : {0}".format(data))


resp = requests.post('http://' + url + '/api/v1/type/service/botbuilder/tagging/',
                     json={
                        "cb_id": "cb0001",
                        "pos_type": "ngram",
                        "proper_noun": {}
                        })
data = json.loads(resp.json())
print("evaluation result : {0}".format(data))

import requests
import json, os

url = "{0}:{1}".format(os.environ['HOSTNAME'] , "8000")

# merge data sets to one
resp = requests.post('http://' + url + '/api/v1/type/wf/state/pre/detail/merge/type/seq2seq/nnid/nn00004/ver/5/node/text_merge_node/',
                     json={
                         "batchsize" : 10,
                         "merge_rule" : {"encode_node" : "data_encode_node",
                                         "decode_node": "data_decode_node"}
                     })
data = json.loads(resp.json())
print("evaluation result : {0}".format(data))


# convert data format to feed network
resp = requests.post('http://' + url + '/api/v1/type/wf/state/pre/detail/convert/type/auto/nnid/nn00004/ver/5/node/text_convert_node/',
                     json={
                         "batchsize" : 10
                     })
data = json.loads(resp.json())
print("evaluation result : {0}".format(data))
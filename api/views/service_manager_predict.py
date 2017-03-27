import json
from rest_framework.response import Response
from rest_framework.views import APIView
from cluster.service.service_predict_d2v import PredictNetD2V
from cluster.service.service_predict_w2v import PredictNetW2V
from cluster.service.service_predict_cnn import PredictNetCnn
from cluster.service.service_predict_renet import PredictNetRenet
from cluster.service.service_predict_wdnn import PredictNetWdnn
from cluster.service.service_predict_seq2seq import PredictNetSeq2Seq
from common.utils import *

class ServiceManagerPredict(APIView):
    """
    """
    def post(self, request, type, nnid, ver):
        """
        - desc : insert cnn configuration data
        """
        try:

            if(ver == 'active') :
                if(type == 'w2v') :
                    return_data = PredictNetW2V().run(nnid, request.data)
                elif(type == "d2v"):
                    return_data = PredictNetD2V().run(nnid, request.data)
                elif(type == "cnn"):
                    # TO-DO : need predict function for active taged version
                    raise Exception("on developing now !")
                elif (type == "wdnn"):
                    raise Exception("on developing now !")
                elif(type == "seq2seq"):
                    return_data = PredictNetSeq2Seq().run(nnid, request.data)
                elif (type == "renet"):
                    #return_data = PredictNetRenet().run(nnid, ver, request.FILES)
                    # TO-DO : need to create PredictNetRenet class first
                    raise Exception("on developing now !")
                else :
                    raise Exception ("Not defined type error")
            else :
                if (type == 'w2v'):
                    # TO-DO : need predict function for specific  version
                    raise Exception("on developing now !")
                elif (type == "d2v"):
                    # TO-DO : need predict function for specific  version
                    raise Exception("on developing now !")
                elif (type == "cnn"):
                    return_data = PredictNetCnn().run(nnid, ver, request.FILES)
                elif (type == "wdnn"):
                    return_data = PredictNetWdnn().run(nnid, ver, request.FILES)
                elif (type == "seq2seq"):
                    # TO-DO : need predict function for specific  version
                    raise Exception("on developing now !")
                elif (type == "renet"):
                    return_data = PredictNetRenet().run(nnid, ver, request.FILES)
                else:
                    raise Exception("Not defined type error")

            return Response(json.dumps(return_data))
        except Exception as e:
            return_data = {"status": "404", "result": str(e)}
            return Response(json.dumps(return_data))

    def get(self, request, type, nnid, ver):
        """
        - desc : get cnn configuration data
        """
        try:
            return_data = ""
            return Response(json.dumps(return_data))
        except Exception as e:
            return_data = {"status": "404", "result": str(e)}
            return Response(json.dumps(return_data))

    def put(self, request, type, nnid, ver):
        """
        - desc ; update cnn configuration data
        """
        try:
            return_data = ""
            return Response(json.dumps(return_data))
        except Exception as e:
            return_data = {"status": "404", "result": str(e)}
            return Response(json.dumps(return_data))

    def delete(self, request, type, nnid, ver):
        """
        - desc : delete cnn configuration data
        """
        try:
            return_data = ""
            return Response(json.dumps(return_data))
        except Exception as e:
            return_data = {"status": "404", "result": str(e)}
            return Response(json.dumps(return_data))
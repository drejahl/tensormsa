import json
from rest_framework.response import Response
from rest_framework.views import APIView
from master.workflow.preprocess.workflow_pre_convert import WorkFlowPreConvert as WFpreConvert

class WorkFlowPreConvert(APIView) :
    """

    """
    def post(self, request, nnid, ver, node, type):
        """
        - desc : insert data
        """
        try:
            input_data = json.loads(str(request.body, 'utf-8'))
            nodeid = ''.join([nnid, '_', ver, '_', node])
            input_data['type'] = type
            if (WFpreConvert().validation_check(input_data)):
                return_data = WFpreConvert().set_view_obj(nodeid, input_data)
            else :
                return_data = {'message' : 'data validation error'}
            return Response(json.dumps(return_data))
        except Exception as e:
            return_data = {"status": "404", "result": str(e)}
            return Response(json.dumps(return_data))

    def get(self, request, nnid, ver, node, type):
        """
        - desc : get data
        """
        try:
            return_data = ""
            return Response(json.dumps(return_data))
        except Exception as e:
            return_data = {"status": "404", "result": str(e)}
            return Response(json.dumps(return_data))

    def put(self, request, nnid, ver, node, type):
        """
        - desc ; update data
        """
        try:
            return_data = ""
            return Response(json.dumps(return_data))
        except Exception as e:
            return_data = {"status": "404", "result": str(e)}
            return Response(json.dumps(return_data))

    def delete(self, request, nnid, ver, node, type):
        """
        - desc : delete  data
        """
        try:
            return_data = ""
            return Response(json.dumps(return_data))
        except Exception as e:
            return_data = {"status": "404", "result": str(e)}
            return Response(json.dumps(return_data))

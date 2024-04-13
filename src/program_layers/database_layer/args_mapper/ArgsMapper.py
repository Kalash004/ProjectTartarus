from src.__models_for_all_layers.data_files.ParsedRequest import ParsedRequest
from src.program_layers.database_layer.RequestToDbObjMapper import RequestToDbObjMapper


class ArgsMapper:
    def __init__(self):
        pass

    def map(self, parsed_req: ParsedRequest):
        params = []
        req_params = parsed_req.parameters
        if "ID" in req_params.keys():
            params.append(self.get_id_param(parsed_req))
        for k, v in req_params.items():
            if k == "ID":
                continue
            self.check_attr_in_table(k, parsed_req)
            temp_param: list = []
            temp_param.append(k.lower())
            temp_param.append("=")
            temp_param.append(v)
            params.append(temp_param)

    @staticmethod
    def get_id_param(parsed_req):
        result = []
        obj = RequestToDbObjMapper().get_request_obj_type(parsed_req)
        primary_key_name = obj.find_primary_key_name()
        result.append(primary_key_name)
        result.append("=")
        result.append(parsed_req.parameters["ID"])
        return result

    @staticmethod
    def check_attr_in_table(key, parsed_req):
        obj = RequestToDbObjMapper().get_request_obj_type(parsed_req)
        structure = obj.get_structure()
        if key.lower() not in structure.keys():
            # TODO: Better handling
            raise Exception

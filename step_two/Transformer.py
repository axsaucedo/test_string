import numpy as np
from seldon_core.utils import *
from seldon_core.user_model import *
import logging

class Transformer():

    def predict_raw(self, request):
        """
        X is of shape np.array([[words for str1], [words for str2], ...])
        the return will just be np.array([first word from str1, first word from str2, etc])
        """
        logging.warning("INCOMING REQUEST")
        logging.warning(request)
        n = request["data"]["ndarray"]
        logging.warning(n)
        logging.warning(n[0])
        logging.warning(type(n[0]))
        (features, meta, datadef, data_type) = extract_request_parts_json(request)
        logging.warning("FEATURES:")
        logging.warning(features)
        logging.warning("DATA DEF:")
        logging.warning(datadef)
        client_response = client_predict(self, features, datadef.names, meta=meta)
        logging.warning("CLIENT RESPONE:")
        logging.warning(client_response)
        response = construct_response_json(self, False, request, client_response)
        logging.warning("RESPONSE:")
        logging.warning(response)
        return response


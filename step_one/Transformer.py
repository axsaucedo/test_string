import numpy as np
import logging

class Transformer():

    def predict(self, X, feature_names=[]):
        """
        X is of shape [str1, str2, str3, ...]
        the return is np.array([[words for str1], [words for str2], ...])
        """
        logging.warning(X)
        result = []
        for s in X:
            logging.warning(s)
            logging.warning(type(s))
            result.append(s.split())
        np_result = np.array(result)
        logging.warning(np_result)
        return np_result


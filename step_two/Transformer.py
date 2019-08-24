import numpy as np
import logging

class Transformer():

    def predict(self, X, feature_names=[]):
        """
        X is of shape np.array([[words for str1], [words for str2], ...])
        the return will just be np.array([first word from str1, first word from str2, etc])
        """
        logging.warning(X)
        result = []
        for s in X:
            logging.warning(s)
            logging.warning(type(s))
            result.append(s[0])
        np_result = np.array(result)
        logging.warning(np_result)
        return np_result


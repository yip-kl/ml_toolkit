from sklearn.compose import ColumnTransformer
from sklearn.feature_selection import SelectorMixin
from sklearn.base import BaseEstimator
from sklearn.utils.validation import check_is_fitted
import numpy as np
import pandas as pd

def get_feature_names(columnTransformer):
    """ Show header name after transformation for columnTransformer
    
    Parameters
    ----------
    columnTransformer: A sklearn ColumnTransformer object
    
    Returns
    -------
    output_features: A list containing the appropriate header name after transformation
    
    """

    output_features = []

    for name, pipe, features in columnTransformer.transformers_:
        if name!='remainder':
            for i in pipe:
                trans_features = []
                if hasattr(i,'categories_'):
                    trans_features.extend(i.get_feature_names(features))
                else:
                    trans_features = features
            output_features.extend(trans_features)

    return output_features

def get_selected_features(df_columns, pipeline):
    """ Show header name after transformation for feature selection pipeline
    
    Parameters
    ----------
    df_columns: DataFrame.columns of the dataframe before transformation
    pipeline: The sklearn Pipeline object used for feature selection
    
    Returns
    -------
    features: list
    
    """
    output = df_columns
    for step in pipeline.named_steps:
        support_mask = pipeline.named_steps[step].get_support()
        output = output[support_mask]
    
    return output

class CorrelationThreshold(BaseEstimator, SelectorMixin):
    """
    Feature Selection Transformer, which reviews pairwise Pearson's r of X variables, and exclude the 
    
    Parameters
    ----------
    threshold: Exclude variables whose r against ANY variable being above this number. Default = 1
    """    
    def __init__(self, threshold = 1): # no *args or **kwargs
        self.threshold = threshold
    
    def fit(self, X, y = None):
        
        # Validation
        X = self._validate_data(X, accept_sparse=('csr', 'csc'),
                                dtype=np.float64)
        
        # Create correlation matrix, and select the upper triangle
        cor_matrix = pd.DataFrame(X).corr().abs()
        self.upper_tri_ = cor_matrix.where(np.triu(np.ones(cor_matrix.shape),k=1).astype(np.bool))
        
        return self

    def _get_support_mask(self):
        check_is_fitted(self)
        return np.array([not any(self.upper_tri_[column] >= self.threshold) for column in self.upper_tri_.columns])
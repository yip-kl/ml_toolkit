import matplotlib.pyplot as plt
from sklearn.feature_selection import RFECV

def rfecv_graph(rfecv_obj, max_features, min_features, step):
    """ Plot cross-validation score against number of features selected for RFECV
    
    Parameters
    ----------
    rfecv_obj: Fitted RFECV class
    
    """
    
    print("Optimal number of features : %d" % rfecv_obj.n_features_)

    iteration_list = [i for i in range(max_features, max_features-len(rfecv_obj.cv_results_['mean_test_score'])*step, -step)]
    iteration_list.reverse()
    
    # Plot number of features VS. cross-validation scores
    plt.figure()
    plt.xlabel("Number of features selected")
    plt.ylabel("Cross validation score")
    plt.plot(
        iteration_list,
        rfecv_obj.cv_results_['mean_test_score'],
    )
    plt.show()

import matplotlib.pyplot as plt
from sklearn.feature_selection import RFECV

def rfecv_graph(rfecv_obj):
    """ Plot cross-validation score against number of features selected for RFECV
    
    Parameters
    ----------
    rfecv_obj: Fitted RFECV class
    
    """
    
    print("Optimal number of features : %d" % rfecv_obj.n_features_)

    # Plot number of features VS. cross-validation scores
    plt.figure()
    plt.xlabel("Number of features selected")
    plt.ylabel("Cross validation score")
    plt.plot(
        range(1, len(rfecv_obj.cv_results_['mean_test_score']) + 1),
        rfecv_obj.cv_results_['mean_test_score'],
    )
    plt.show()
    
def plot_roc_curve(fpr, tpr, label=None):
    """ Plot AUC-ROC curve
    
    Parameters
    ----------
    fpr, tpr: Variables returned by sklearn.metrics.roc_curve
    
    """    
    
    plt.plot(fpr, tpr, linewidth=2, label=label)
    plt.plot([0, 1], [0, 1], 'k--') # dashed diagonal
    plt.axis([0, 1, 0, 1])                                    
    plt.xlabel('False Positive Rate (Fall-Out)', fontsize=16) 
    plt.ylabel('True Positive Rate (Recall)', fontsize=16)    
    plt.grid(True)
    
def plot_precision_vs_recall(precisions, recalls):
    """ Plot Precision-Recall curve
    
    Parameters
    ----------
    precisions, recalls: Variables returned by sklearn.metrics.precision_recall_curve
    
    """    
    
    plt.plot(recalls, precisions, "b-", linewidth=2)
    plt.xlabel("Recall", fontsize=16)
    plt.ylabel("Precision", fontsize=16)
    plt.axis([0, 1, 0, 1])
    plt.grid(True)
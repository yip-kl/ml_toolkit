import pandas as pd

def count_bucket(bucket, score):
    """ Count instances by bucket
    
    Parameters
    ----------
    bucket: A list to separate the buckets e.g. bucket = [i / 10 for i in range(1, 11)]
    score: 1-D array that contains the numerical value
    
    Returns
    -------
    output: A dataframe that shows the number of instances per score bucket
    
    """
    
    output = [
        len([one_score for one_score in score if one_score <= bucket[0]])
    ]
    
    for index, threhold in enumerate(bucket[1:], 1):       
        users_in_between = len(score[np.logical_and(score> bucket[index-1], score <= bucket[index])])
        output.append(users_in_between)
        
    proportion = [i/sum(output) for i in output]
            
    return pd.DataFrame(zip(bucket, output, proportion), columns = ['bucket', 'count', 'proportion'])

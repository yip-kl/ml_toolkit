import pickle

def save_pickle(file_name,memory,save_to):
    filehandler = open('{}/{}'.format(save_to,file_name),"wb")
    pickle.dump(memory,filehandler)
    
def load_pickle(load_from, file_name):
    file = open('{}/{}'.format(load_from,file_name),'rb')
    return pickle.load(file)
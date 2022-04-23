import pickle

def save_pickle(memory, destination_file_name):
    filehandler = open(destination_file_name,"wb")
    pickle.dump(memory,filehandler)
    
def load_pickle(destination_file_name):
    file = open(destination_file_name,'rb')
    return pickle.load(file)
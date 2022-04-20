import os
import pickle

def find_no_doc_file(doc_path,id_of_user):

    no_of_txt=0
    arr = os.listdir(doc_path)
    #print(arr)
    for i in arr:
        if i.endswith(".txt") & i.startswith(id_of_user):
            no_of_txt +=1
    return no_of_txt

def tfidf_write(tfidf_matrix,index_file,index_word,doc_index,doc_path,id_of_user):

    ############### usind pickle to store tf_idf matrix save permenently in file ########
    pickle_variable = open(f'matrix.{id_of_user}', 'wb')
    pickle.dump(tfidf_matrix, pickle_variable)
    pickle.dump(index_file, pickle_variable,-1)
    pickle.dump(index_word, pickle_variable,-1)
    pickle.dump(doc_index, pickle_variable,-1)
    pickle.dump(doc_path, pickle_variable,-1)
    pickle_variable.close()

def tfidf_read(id_of_user):
    pkl_file = open(f'matrix.{id_of_user}', 'rb')
    tfidf = pickle.load(pkl_file)
    docs_dict = pickle.load(pkl_file)
    words_dict = pickle.load(pkl_file)
    doc_index = pickle.load(pkl_file)
    doc_path = pickle.load(pkl_file)
    pkl_file.close()
    return(tfidf,docs_dict,words_dict,doc_index,doc_path)
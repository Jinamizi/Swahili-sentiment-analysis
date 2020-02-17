from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.model_selection import KFold

from ml2 import Model,Model1,Model2

#given a list of file names, organize the data in a list
def organize_data(filenames):
    processed_data = []
    for filename in filenames:    
        with open(filename, "r") as file:
            for line in file.read().split('\n'):
                if len(line.split("\t")) == 2 and line.split("\t")[1] != "":
                    processed_data.append(line.split("\t"))
        
    return processed_data

def evaluate_model(inputs, outputs, model, n_folds):
    inputs_copy = np.array(inputs)
    outputs_copy = np.array(outputs)
    kf = KFold(n_splits = n_folds) #define the split
    scores = list()
    
    for train_index, test_index in kf.split(inputs):
        inputs_train, inputs_test = inputs_copy[train_index], inputs_copy[test_index]
        outputs_train, outputs_test = outputs_copy[train_index], outputs_copy[test_index]
        model.train(inputs_train, outputs_train)
        predictions = model.predict(inputs_test)
        accuracy = accuracy_score(outputs_test,predictions)
        scores.append(accuracy)
    return scores

if __name__ == '__main__':
    base_directory = "C:\\Users\\tonny\\Desktop\\project stuff\\IA-master\\ClassificacaoComentariosComNaiveBayes\\Datasets\\"
    file1 = base_directory + "imdb_labelled.txt"
    file2 = base_directory + "amazon_cells_labelled.txt"
    file3 = base_directory + "yelp_labelled.txt"
    files = [file1, file2, file3]
    data = data = organize_data(files)
    data = np.array(data)
    #specify the data
    X = data[:,0]
    #specify the target labels
    y = data[:,-1]
    #Split the data up in train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 42)
    model = Model1()
    model.train(X_train, y_train)
    predictions = model.predict(X_test)
    print("accuracy:", accuracy_score(y_test,predictions))
    cm = confusion_matrix(y_test, predictions)
    print(cm)
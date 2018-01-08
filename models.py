import numpy as np
import Model_preprocessing as MP
import Simple_perceptron_model as SP
from sklearn.model_selection import train_test_split
reload(SP)
reload(MP)


#get the dataset
# X_train, X_test, Y_train, Y_test, Improved_spam, Improved_spam_labels = MP.get_processed_dataset()
# # X = np.concatenate((X_train,X_test))
# # Y = np.concatenate((Y_train,Y_test))
#
# # split improved dataset
# Improved_spam_train, Improved_spam_test, Improved_spam_labels_train, Improved_spam_labels_test = train_test_split(Improved_spam, Improved_spam_labels, test_size = 0.5, random_state=0)
# X = np.concatenate((X_train,Improved_spam_train))
# Y = np.concatenate((Y_train,Improved_spam_labels_train))
# X_test = np.concatenate((X_test,Improved_spam_test))
# Y_test = np.concatenate((Y_test,Improved_spam_labels_test))

#for imprved spam only dataset
X,X_test,Y,Y_test = MP.get_processed_improved_dataset()

def model_usage_simple_perceptron():

    #get model classifier with 1 fold CV
    # classifier = SP.get_simple_perceptron_classifier(X,Y,X_test,Y_test, nb_epochs=1000, batch_size=100)

    # stratifier cv with 10 fold CV
    cvscores, classifiers = SP.get_acc_from_stratified_cross_val(X, Y)
    print cvscores
    cvscores = np.array(cvscores)
    print cvscores.mean()
    print cvscores.std()
    #select classifier with best score
    classifier = classifiers[np.argmax(np.array(cvscores))]


    # classifier_GS = SP.simple_perceptron_based_GridSearch(X_train,Y_train)
    # print classifier_GS.best_params_
    # print classifier_GS.best_score_
    # classifier = classifier_GS.best_estimator_


    # #predicting the training data
    # Y_pred = classifier.predict(Improved_spam_test)
    # Y_pred = (Y_pred > 0.5)
    # # print Y_pred
    #
    # # # #making confustion matrix
    # from sklearn.metrics import confusion_matrix
    # cm = confusion_matrix(Improved_spam_labels_test, Y_pred)
    #
    # print cm

    Y_pred = classifier.predict(X_test)
    Y_pred = (Y_pred > 0.5)
    # print Y_pred

    # # #making confustion matrix
    from sklearn.metrics import confusion_matrix
    cm = confusion_matrix(Y_test, Y_pred)

    print cm

# def model_usage_two_hidden_layer():
#
#     #get model classifier with 1 fold CV
#     # classifier = SP.get_simple_perceptron_classifier(X_train,Y_train,X_test,Y_test, nb_epochs=1000, batch_size=100)
#
#     # stratifier cv with 10 fold CV
#     cvscores, classifiers = SP.get_acc_from_stratified_cross_val(X, Y)
#     print cvscores
#     cvscores = np.array(cvscores)
#     print cvscores.mean()
#     print cvscores.std()
#     #select classifier with best score
#     classifier = classifiers[np.argmax(np.array(cvscores))]
#
#     # #predicting the training data
#     Y_pred = classifier.predict(Improved_spam)
#     Y_pred = (Y_pred > 0.5)
#     print Y_pred
#
#     # # #making confustion matrix
#     from sklearn.metrics import confusion_matrix
#     cm = confusion_matrix(Improved_spam_labels, Y_pred)
#
#     print cm

model_usage_simple_perceptron()
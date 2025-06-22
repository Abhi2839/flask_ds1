import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
(x_train,y_train) ,(x_test,y_test)=keras.datasets.mnist.load_data()
# print(len(x_train))
# print(x_train.shape)
# print(len(y_train))
# print(x_test)
# print(y_test)
# print(x_train[0].shape)  # to get dimension of dataset
# print(x_train[0])
# plt.matshow(x_train[0])
# plt.show()
# print(y_train[2])
# # first 5 elements
# print(y_train[:5])
# x_train=x_train/255 # to get more accuracy scaling is must 0-255
# x_test=x_test/255 
# to flatten the dataset means convert into 1D
x_train_flatten=x_train.reshape(len(x_train),28*28)
x_test_flatten=x_test.reshape(len(x_test),28*28)
# print(x_train_flatten.shape)
# print(x_test_flatten.shape)

# print(x_train_flatten[0])  # 1D array


#training the data using keras
model=keras.Sequential([
    keras.layers.Dense(10,input_shape=(784,),activation='sigmoid')
    # 10 is numbers of neuro
    # dense all input are connected to each neuron
])

model.compile(
    optimizer='adam', #diff optimizer techniques like rms,gradient,stochastic
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
#training the data
# model.fit(x_train_flatten,y_train,epochs=10)

#evaluating the acc
# model.evaluate(x_test_flatten,y_test)

# plt.matshow(x_test[0])
# plt.show()
y_predicted=model.predict(x_test_flatten)
print(y_predicted[0]) # print all 10 vals
print(np.argmax(y_predicted[0]))  # prediciting val

y_predicted_label=[np.argmax(i) for i in y_predicted]  # for integer conversion
print(y_predicted[:5])
print(y_test[:5])
#creating confusing matrix
cm=tf.math.confusion_matrix(labels=y_test,predictions=y_predicted_label)
print(cm)
#printing confusion matrix
plt.figure(figsize=(10,7))
sns.heatmap(cm,annot=True,fmt='d')  # fmt=format them as int annot=True write numbers in cell
plt.xlabel('Predicted')
plt.ylabel('Truth')
plt.show()

model1=keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)),
    keras.layers.Dense(100,activation='relu'),    #relu=max(0,x)
    keras.layers.Dense(10,activation='sigmoid')
])
model1.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
model1.fit(x_train,y_train,epochs=4)

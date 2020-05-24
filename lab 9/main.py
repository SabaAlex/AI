import tensorflow
from tensorflow.keras import models
import os


def define_model():
    model = models.Sequential()
    model.add(tensorflow.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
    model.add(tensorflow.keras.layers.MaxPooling2D((2, 2)))
    model.add(tensorflow.keras.layers.Dropout(0.25))
    model.add(tensorflow.keras.layers.Flatten())
    model.add(tensorflow.keras.layers.Dense(128, activation='relu'))
    model.add(tensorflow.keras.layers.Dropout(0.5))
    model.add(tensorflow.keras.layers.Dense(10))
    # compile model

    opt = tensorflow.keras.optimizers.SGD(lr=0.0001, momentum=0.9)
    model.compile(
        optimizer=opt,
        loss=tensorflow.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
        metrics=['accuracy']
    )

    return model


if __name__ == '__main__':
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
    (trainX, trainY), (testX, testY) = tensorflow.keras.datasets.mnist.load_data()
    # reshape dataset to have a single channel
    trainX = trainX.reshape((trainX.shape[0], 28, 28, 1))
    testX = testX.reshape((testX.shape[0], 28, 28, 1))
    models = define_model()
    models.fit(
        trainX,
        trainY,
        epochs=5,
        batch_size=128,
        validation_data=(testX, testY),
        verbose=1
    )

    loss, acc = models.evaluate(testX, testY)
    print('accuracy %.3f' % (acc * 100.0), 'loss %.3f' % loss)

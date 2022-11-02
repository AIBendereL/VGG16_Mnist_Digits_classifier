# VGG16 pre-trained weights and trained weights.

Because the models weights are too big to be uploaded on Github. Please use Pytorch to download the weights.

The 2 models weights needed to run the 2 main scripts.

1. (Train script) digits_classifier_train.py: **vgg16_weights.pth** - pre-trained weights
2. (Test script)  digits_classifier_test.py: **vgg16_weights_mnist_digits.pth** - trained weights

## How to get **vgg16_weights.pth** for the train script.

You can simply run the file download_weights.py in this folder to generate a vgg16 pre-trained weights.


## How to get **vgg16_weights_mnist_digits.pth** for the test script.

This is the weights you will get after training your model.

Therefore, after getting the vgg16 pre-trained weights, you can run the training script digits_classifier_train.py to generate this trained weights.

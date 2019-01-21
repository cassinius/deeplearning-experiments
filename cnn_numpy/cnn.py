import pickle # serialization
import numpy as np
from preprocessor import Preprocessor as img_prep #image preprocessing

DEFAULT_POOLING_LAYER_SIZE = 2
DEFAULT_WEIGHT_FILE = "./data/alpha_weights_unix.pkl"

# class for loading our saved model and classifying new images
class LiteOCR:

	def __init__(self, fn=DEFAULT_WEIGHT_FILE, pool_size=DEFAULT_POOLING_LAYER_SIZE):
		# load the weights from the picke file and the meta data
		# (so this is the data set)
		[weights, meta] = pickle.load(open(fn, "rb"), encoding="latin1")
		# list to store labels
		self.vocab = meta["vocab"]

		# how many rows and columns in an image
		self.img_rows = meta["img_side"] ; self.img_cols = meta["img_side"]

		# load our CNN
		self.CNN = LiteCNN()
		# with our saved weights
		self.CNN.load_weights(weights)
		# define the pooling layers size (set to a default of 2)
		self.CNN.pool_size = int(pool_size)


	# classify new image
	def predict(self, image):
		print(image.shape)
		# vectorize the image into the right shape for our network
		X = np.reshape(image, (1, 1, self.img_rows, self.img_cols))
		X = X.astype("float32")

		# make the prediction
		predicted_i = self.CNN.predict(X)
		# return the predicted label
		return self.vocab[predicted_i]



class LiteCNN:

	def __init__(self):
		# a place to store the layers
		self.layers = []
		# size of pooling area for max pooling
		self.pool_size = None

	def load_weights(self, weights):
		assert not self.layers, "Weights can only be loaded once!"
		for k in range(len(weights.keys())):
			self.layers.append(weights['layer_{}'.format(k)])

	def predict(self, X):
		# here is where the network magic happens at a high level
		h = self.cnn_layer(X, layer_i=1, border_mode="full"); X = h
		h = self.relu_layer(X); X = h;
		h = self.cnn_layer(X, layer_i=2, border_mode="valid"); X = h;
		h = self.relu_layer(X); X = h;
		h = self.maxpooling_layer(X); X = h
		h = self.dropout_layer(X, .25); X = h
		h = self.flatten_layer(X, layer_i=7); X = h
		h = self.dense_layer(X, fully, layer_i=10); X = h
		h = self.softmax_layer2D(X); X = h
		max_i = self.classify(X)
		return max_i[0]

	def maxpooling_layer(self, convolved_features):
		nb_features = convolved_features.shape[0]
		nb_images = convolved_features.shape[1]
		conv_dim = convolved_features.shape[2]
		res_dim = int(conv_dim / self.pool_size)

		# initialize our more dense feature list as empty
		pooled_features = np.zeros((nb_features, nb_images, res_dim, ))


	def cnn_layer(self, X, layer_i=0, border_mode = "full"):
		# we'll store our feature maps and bias value in these 2 vars
		features = self.layers[layer_i]["param_0"]
		bias = self.layers[layer_i]["param_1"]


	def relu_layer(self):
		print('RELU')


	def dropout_layer(self):
		print('dropout (is destiny)')


	def flatten_layer(self):
		print('flattening')


	def dense_layer(self):
		print('dense')


	def softmax_layer2D(self):
		print('softmax')


	def classify(self):
		print('classify')


LiteOCR()
from flask import Flask, request
import numpy as np 
import pickle 

app = Flask(__name__)

@app.route('/')
def home(): 
	return 'Home'

@app.route('/predict')
def predict():
	# get parameters to predict with from the URL 
	sepal_length = request.args['sepal_length']
	sepal_width = request.args['sepal_width']
	petal_length = request.args['petal_length']
	petal_width = request.args['petal_width']

	data = np.array([sepal_length, sepal_width, petal_length, petal_width]).reshape(1,4)
	class_predicted = int(classifier.predict(data)[0])
	output = "Predicted Iris Class: " + str(class_predicted)
	
	return output

def load_model():
	global classifier
	
	clf_file = open('models/classifier.pckl', 'rb')
	classifier = pickle.load(clf_file)
	clf_file.close()

if __name__ == "__main__":
	print("Starting Server...")
	# Call function that loads the model 
	load_model()
	# Run Server
	app.run()
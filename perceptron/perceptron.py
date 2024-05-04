#import util
PRINT = True

class PerceptronClassifier:
    """
    Perceptron classifier.
    
    Note that the variable 'datum' in this code refers to a counter of features
    (not to a raw samples.Datum).
    """
    def __init__( self, legalLabels, max_iterations):
        self.legalLabels = legalLabels
        self.type = "perceptron"
        self.max_iterations = max_iterations
        self.weights = {}
        for label in legalLabels:
            self.weights[label] = {}  # Changed from util.Counter() to empty dictionary

    def setWeights(self, weights):
        assert len(weights) == len(self.legalLabels)
        self.weights = weights  # Corrected the assignment operator to '=' instead of '=='
      
    def train( self, trainingData, trainingLabels, validationData, validationLabels ):
        """
        The training loop for the perceptron passes through the training data several
        times and updates the weight vector for each label based on classification errors.
        See the project description for details. 
        
        Use the provided self.weights[label] data structure so that 
        the classify method works correctly. Also, recall that a
        datum is a counter from features to values for those features
        (and thus represents a vector a values).
        """
        
        # self.features = trainingData[0].keys() # could be useful later
        # DO NOT ZERO OUT YOUR WEIGHTS BEFORE STARTING TRAINING, OR
        # THE AUTOGRADER WILL LIKELY DEDUCT POINTS.
        
        for iteration in range(self.max_iterations):
            print("Starting iteration ", iteration, "...")
            for i in range(len(trainingData)):
                actual = trainingLabels[i]
                bestGuess = self.classify([trainingData[i]])[0]
                if bestGuess != actual:
                    for feature in trainingData[i]:
                        if feature not in self.weights[actual]:
                            self.weights[actual][feature] = 0
                        if feature not in self.weights[bestGuess]:
                            self.weights[bestGuess][feature] = 0
                        self.weights[bestGuess][feature] -= trainingData[i][feature]
                        self.weights[actual][feature] += trainingData[i][feature]
        
    def classify(self, data):
        """
        Classifies each datum as the label that most closely matches the prototype vector
        for that label.  See the project description for details.
        
        Recall that a datum is a dictionary...
        """
        guesses = []
        for datum in data:
            vectors = {}
            for l in self.legalLabels:
                vectors[l] = sum(self.weights[l].get(feature, 0) * value for feature, value in datum.items())
            guesses.append(max(vectors, key=vectors.get))
        return guesses

  
    def findHighWeightFeatures(self, label):
        """
        Returns a list of the 100 features with the greatest weight for some label
        """
        "*** YOUR CODE HERE ***"
        raise NotImplementedError()

        return featuresWeights
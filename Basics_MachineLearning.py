import matplotlib.pyplot as plt
X = [[6], [8], [10], [14],   [18]]
y = [[7], [9], [13], [17.5], [18]]
plt.figure()
plt.title('Pizza price plotted against diameter')
plt.xlabel('Diameter in inches')
plt.ylabel('Price in dollars')
plt.plot(X, y, 'k.')
plt.axis([0, 25, 0, 25])
plt.grid(True)
plt.show()

#---------------------------------------------------------

from sklearn.linear_model import LinearRegression
# Training data
X = [[6], [8], [10], [14],   [18]]
y = [[7], [9], [13], [17.5], [18]]
# Create and fit the model
model = LinearRegression()
model.fit(X, y)
print ("A 12inch pizza should cost: {0:.2f}".format(model.predict([[12]])[0][0]))

#---------------------------------------------------------

from sklearn.linear_model import LinearRegression
X = [[6], [8], [10], [14],   [18]]
y = [[7], [9], [13], [17.5], [18]]
X_test = [[8],  [9],   [11], [16], [12]]
y_test = [[11], [8.5], [15], [18], [11]]
model = LinearRegression()
model.fit(X, y)
print("R-squared: {0:.4f}".format(model.score(X_test, y_test)))

#---------------------------------------------------------

from sklearn.linear_model import LinearRegression
X = [[6, 2], [8, 1], [10, 0], [14, 2], [18, 0]]
y = [[7],    [9],    [13],    [17.5],  [18]]
model = LinearRegression()
model.fit(X, y)
X_test = [[8, 2], [9, 0], [11, 2], [16, 2], [12, 0]]
y_test = [[11],   [8.5],  [15],    [18],    [11]]
predictions = model.predict(X_test)
for i, prediction in enumerate(predictions):
     print ('Predicted: {}, Target: {}'.format(prediction, y_test[i]))
print ('R-squared: {0:.2f}'.format(model.score(X_test, y_test)))
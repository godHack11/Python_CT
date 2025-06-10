# Feature Selection, Feature Extraction, Feature Encoding, Dimensionality Reduction, Principal Component Analysis, Linear Discriminant Analysis, t-SNE, Autoencoders

1. Feature Selection
Feature Selection is the process of choosing the most important variables (features) from a dataset that contribute the most to the predictive model.

Why it’s used:
	Reduces overfitting
	Improves accuracy
	Decreases training time
  
Types:
	Filter Methods: Select features based on statistics (e.g., correlation, chi-square).
	Wrapper Methods: Use algorithms (e.g., forward selection, backward elimination).
	Embedded Methods: Feature selection happens during model training (e.g., LASSO, Decision Trees).

2. Feature Extraction
Converts raw data into a set of features that better represent the underlying problem.

Example:
In image data, pixel intensities are raw data. From them, you might extract edges, shapes, or textures.

Difference from Feature Selection:
	Selection: Chooses from existing features.
	Extraction: Creates new features from existing data.

3. Feature Encoding
Converting categorical data into numerical form so that machine learning models can understand it.

Common Techniques:
	Label Encoding: Converts each category to a number.
	Example: Red=0, Green=1, Blue=2
	One-Hot Encoding: Creates separate binary columns for each category.
	Example: Color_Red, Color_Blue, Color_Green
	Ordinal Encoding: For categorical variables with order (e.g., Low < Medium < High).

4. Dimensionality Reduction
Reducing the number of input variables/features in a dataset while preserving as much information as possible.

Why it’s important:
	Reduces computation cost
	Improves model performance
	Helps visualize data
	Removes noise

5. Principal Component Analysis (PCA)
PCA is a linear technique for reducing the dimensionality of data while preserving variance.

How it works:
	Converts original features into principal components (new variables).
	First component captures the most variance, second captures the next most, etc.

Use cases:
	Noise reduction
	Visualizing high-dimensional data (in 2D or 3D)
	Speeding up ML algorithms

6. Linear Discriminant Analysis (LDA)
LDA is a supervised dimensionality reduction technique used when you have labeled data.

How it’s different from PCA:
	PCA focuses on maximizing variance (unsupervised).
	LDA focuses on maximizing class separability (supervised).

Use cases:
	Face recognition
	Text classification
	Multiclass classification

7. t-SNE (t-distributed Stochastic Neighbor Embedding)
t-SNE is a non-linear technique primarily used for visualization of high-dimensional data in 2D or 3D.

How it works:
	Preserves local relationships in data.
	Clusters similar data points together in the lower dimension.

Use cases:
	Visualizing embeddings
	Clustering patterns in data

t-SNE is not good for general-purpose dimensionality reduction for ML models, just for visualization.

8. Autoencoders
Autoencoders are a type of neural network that learns to compress and reconstruct data.                                                              

Structure:
	Encoder: Compresses the input into a lower-dimensional representation.
	Decoder: Reconstructs the input from that compressed representation.

Use cases:
	Image compression
	Anomaly detection
	Noise reduction
	Non-linear dimensionality reduction




                                                              

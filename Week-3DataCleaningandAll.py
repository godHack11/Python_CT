# Data Cleaning, Data Transformation, Data Normalization, Data Scaling, Data Encoding, Data Imputation, Handling Missing Data, 
# Data Reduction, Data Integration, Data Sampling

# Data Cleaning

# Process of fixing or removing incorrect, corrupted, or inconsistent data.
# Remove duplicates
# Correct errors and typos
# Handle missing values
# Fix data types and formats

⸻

# 2. Data Transformation

# Changing data into a suitable format or structure for analysis.
# Aggregation (e.g., sum sales by month)
# Normalization and scaling
# Encoding categorical variables
# Log transformation to reduce skewness

⸻

# 3. Data Normalization

# Rescales data to a common scale, usually [0, 1], without distorting differences.
# Example:
# x’ = \frac{x - \min(x)}{\max(x) - \min(x)}

⸻

# 4. Data Scaling

# Adjusting the range of features.
# Standardization (Z-score scaling):
# x’ = \frac{x - \mu}{\sigma}
# Centers data around mean 0 with std dev 1.
# Scaling helps algorithms sensitive to feature scale (e.g., SVM, KNN).

⸻

# 5. Data Encoding

# Convert categorical data into numerical format.
# Label encoding: Assign integer labels (0,1,2…)
# One-hot encoding: Create binary columns for categories
# Ordinal encoding: Encode ordered categories (e.g., low, medium, high)

⸻

# 6. Data Imputation

# Filling missing values with reasonable estimates.
# Mean/median/mode substitution
# Forward-fill or backward-fill (time series)
# Model-based imputation (e.g., KNN, regression)

⸻

# 7. Handling Missing Data

# Techniques to deal with gaps:
# Remove rows/columns with missing data (if small portion)
# Impute missing values (see above)
# Flag missingness as a separate category

⸻

# 8. Data Reduction

# Reducing dataset size while preserving important information.
# Feature selection (select most relevant variables)
# Dimensionality reduction (PCA, t-SNE)
# Sampling to reduce data points

⸻

# 9. Data Integration

# Combining data from multiple sources.
# Merging/joining tables
# Resolving schema conflicts
# Handling duplicate records

⸻

# 10. Data Sampling

# Selecting a subset of data for analysis.
# Random sampling
# Stratified sampling (maintain distribution of classes)
# Systematic sampling (every nth record)





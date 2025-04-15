# Home Goods Product Recommendation System: Amazon US Customer Reviews Dataset

## Project Overview

Amazon US relies heavily on intelligent recommendation systems to boost user engagement and drive conversions. This project focuses on predicting whether users will purchase home goods in four categories—Electronics, Furniture, Major Appliances, and Personal Care Appliances—based on customer interactions in the Amazon US Customer Reviews Dataset.

Using over 4 million reviews enriched with metadata like ratings, categories, and review text, we extract behavioral and engagement features to train personalized recommendation models. Our pipeline includes Neural Collaborative Filtering, deep learning models, and advanced feature engineering (e.g., sentiment analysis, text embeddings), all aimed at improving prediction accuracy and personalization.

By aligning model outputs with key business goals—like increasing conversion rates and user satisfaction—this project offers practical insights for optimizing Amazon's recommendation strategy.
---

## Project Pipeline

This project is organized into clearly structured notebooks (`step0` to `step8`) representing each major development stage:

### Step 0: Data Downloading
- Set up directory structure in Google Drive and configure the Kaggle API.
- Downloaded Amazon US Customer Reviews dataset (from Kaggle) specifically from `electronics`, `furniture`, `major appliances`, `personal care appliances` categories.
- Consolidate all individual category files into a single merged dataset, merged_reviews.csv, stored in the data directory.


### Step 1: Data Preprocessing
- Parsed and cleaned raw product data.
- Unnecessary columns like marketplace and review_id are dropped to reduce noise.
- Missing values in essential fields are removed or filled with defaults, and review dates are standardized.

### Step 2: Exploratory Data Analysis (EDA)
- Analyzed user and product activity distribution.
- Visualize the distribution of numerical features using histograms and box plots.
- Identify potential outliers and patterns in the data to guide feature engineering.

### Step 3: Feature Engineering
- Engineered features across user behavior, product attributes, and sentiment to capture preferences and engagement quality.
- Applied clustering, matrix factorization, and aggregation to understand user-product interactions and product appeal.
- Filtered users with at least five purchases over the past four years to create a high-quality dataset for modeling purchase intent.

### Step 4: Customer Segmentation
- Key features are selected from feature-engineered customer dataset containing behavioral and sentiment attributes and standardized to prepare for clustering
- PCA is applied to reduce dimensionality and improve both clustering performance and visualization
- The elbow method determines the optimal number of clusters (k = 4), followed by K-Means clustering
- Each cluster is profiled using summary statistics and visualizations to reveal distinct customer behavior patterns
- Insights are used to inform personalized top-k recommendation strategies, aligning suggestions with user segment characteristics

### Step 5: Model Development

#### 5.1 NCF with Custom Embeddings
- Built a neural collaborative filtering model with user and item embeddings.
- Trained separate NCF models for each cluster using tailored hyperparameters.

#### 5.2 NCF with Random Initialization
- Trained a baseline NCF model with randomly initialized embeddings for comparison.

#### 5.3 NCF with Negative Sampling
- Improved learning by generating negative examples from unpurchased items per user.

#### 5.4 Hybrid NCF Model (Custom + Random Embeddings)
- Combine custom and random embeddings to enhance model accuracy by leveraging both domain-specific features and random initialization.

#### 5.5 Analysis of Validation and Test Datasets
- Analyse the distribution of customer interactions in the validation and test datasets by cluster and  and evaluate the sparsity of customer activity.

### Step 6: Temporal Modeling with LSTM
- Explored sequence modeling via LSTM for capturing user temporal purchase history.
- Compared performance against simpler NCF architectures.

### Step 7: Evaluation
- Evaluated models on both validation and test datasets using metrics:
  - **RMSE**
  - **MSE**
  - **NDCG@10**
  - **Precision@10**
  - **Recall@10**
  - **F1@10**
---

## Folder Structure
### /data
- Contains all raw and intermediate csv files.
- Note that `electronics.csv`, `furniture.csv` and `merged_reviews.csv` are *(not available directly from the repository due to GitHub's file size limits. Please refer to this link: [Google Drive](https://drive.google.com/drive/folders/1pm8sn0FKTTkVw4NY_XIf4NNalzM51Iik?usp=sharing))*


### /notebooks
- Contains all project source codes used.

### Model Results
- Contains all Testing and Validation outputs from every model.

## Contributors
- Huin Hao Ze
- Kenneth Jeremy Prajogo
- Ng Xian Rui
- Parama Roy Poja
- Yuan Tianyi

## References

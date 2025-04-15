# Home Goods Product Recommendation System: Amazon US Customer Reviews Dataset

## Project Overview

Amazon US relies heavily on intelligent recommendation systems to enhance user experience, increase product visibility, and drive conversions. (Smith & Linden, 2017) In this project, we focus on building a personalized recommendation pipeline that predicts the likelihood of a user purchasing home goods across four key product categories: Electronics, Furniture, Major Appliances, and Personal Care Appliances. The analysis is grounded in the Amazon US Customer Reviews Dataset, a large-scale, publicly available dataset widely used for benchmarking in recommendation system research (McAuley et al., 2015)

The dataset consists of over 4 million verified reviews, enriched with metadata including star ratings, product categories, timestamps, and textual review content. To enable personalized predictions, we extract a diverse set of user behavior and engagement features, including purchasing frequency, review sentiment, helpfulness ratios, and category diversity. Additionally, we incorporate text-based signals through sentiment analysis and embedding techniques to capture the semantic richness of user-generated content which is an approach shown to significantly enhance recommendation quality (Dang et al., 2021)

To power personalized recommendations on Amazon US, we use a hybrid modeling pipeline. At the core of our approach is a Hybrid Neural Collaborative Filtering (NCF) model, which combines two pathways: one with custom embeddings built from user behavior and preferences, and another with random embeddings that are learned during training. Each pathway includes both a GMF (Generalized Matrix Factorization) component to capture straightforward interactions and a MLP (Multi-Layer Perceptron) to learn deeper, more complex relationships between users and products.

To further personalize results, we train a separate NCF model for each of the four customer segments identified during clustering. This allows each model to focus on a specific user group, making recommendations more tailored and effective.

In addition, we include a Long Short-Term Memory (LSTM) component to model the sequence of user purchases over time. This is especially helpful for capturing shopping patterns and predicting what a user might need next.

---
## Getting Started

1. **Create a folder** named `bt4222_group_6` in the root of your Google Drive (i.e., inside `My Drive`).
2. **Download and upload this repository** into that folder.

After this, your folder structure should look like this: <br>
- MyDrive/
  - bt4222_group_6/
    - bt4222_group_6_amazon/

This structure is important to ensure all Colab notebooks can correctly access data and modules via relative paths.

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
- Note that `electronics.csv`, `furniture.csv` and `merged_reviews.csv` are *not available directly from the repository due to GitHub's file size limits. Please refer to this link: [Google Drive](https://drive.google.com/drive/folders/1pm8sn0FKTTkVw4NY_XIf4NNalzM51Iik?usp=sharing)*


### /notebooks
- Contains all project source codes used.

### /Model\ Results
- Contains all Testing and Validation outputs from every model.

## Contributors
- Huin Hao Ze
- Kenneth Jeremy Prajogo
- Ng Xian Rui
- Parama Roy Poja
- Yuan Tianyi

## References
- Dang, C. N., Moreno-García, M. N., & De La Prieta, F. (2021). An Approach to Integrating Sentiment Analysis into Recommender Systems. Sensors, 21(16), 5666. https://doi.org/10.3390/s21165666
- McAuley, J., Pandey, R., & Leskovec, J. (2015). Inferring networks of substitutable and complementary products. Inferring Networks of Substitutable and Complementary Products. https://doi.org/10.1145/2783258.2783381
- Smith, B., & Linden, G. (2017). Two decades of recommender systems at Amazon.com. IEEE Internet Computing, 21(3), 12–18. https://doi.org/10.1109/mic.2017.72

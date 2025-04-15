# Home Goods Product Recommendation System: Amazon US Customer Reviews Dataset

## 📄 Project Overview

Amazon US relies heavily on intelligent recommendation systems to boost user engagement and drive conversions. This project focuses on predicting whether users will purchase home goods in four categories—Electronics, Furniture, Major Appliances, and Personal Care Appliances—based on customer interactions in the Amazon US Customer Reviews Dataset.

Using over 4 million reviews enriched with metadata like ratings, categories, and review text, we extract behavioral and engagement features to train personalized recommendation models. Our pipeline includes Neural Collaborative Filtering, deep learning models, and advanced feature engineering (e.g., sentiment analysis, text embeddings), all aimed at improving prediction accuracy and personalization.

By aligning model outputs with key business goals—like increasing conversion rates and user satisfaction—this project offers practical insights for optimizing Amazon's recommendation strategy.
---

## 🛠️ Project Pipeline

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
- Analyzed user and item activity distribution.
- Identified sparsity patterns and purchasing behavior trends.
- Visualized category distribution and temporal spikes.

### Step 3: Feature Engineering
- Created features such as user purchase frequency, time-of-day tendencies, and product category affinity.
- Engineered derived fields from timestamps and review metadata.
- Prepared input features for both segmentation and collaborative filtering models.

### Step 4: Customer Segmentation
- Performed K-Means clustering on engineered user features.
- Identified four distinct user personas:
  1. **Steady and Satisfied**
  2. **Critical and Disengaged**
  3. **High-Value Power Buyers**
  4. **Casual Optimists**
- Incorporated clusters into downstream modeling to personalize recommendations.

### Step 5: Model Development

#### 5.1 NCF with Custom Embeddings
- Built a neural collaborative filtering model with user and item embeddings.
- Trained separate NCF models for each cluster using tailored hyperparameters.

#### 5.2 NCF with Random Initialization
- Trained a baseline NCF model with randomly initialized embeddings for comparison.

#### 5.3 NCF with Negative Sampling
- Improved learning by generating negative examples from unpurchased items per user.

### Step 6: Temporal Modeling with LSTM
- Explored sequence modeling via LSTM for capturing user temporal purchase history.
- Compared performance against simpler NCF architectures.

### Step 7: Regression Analysis for Ensemble
- Performed regression on predictions from multiple NCF variants.
- Calculated optimal weights for ensemble recommendations per user segment.

### Step 8: Evaluation
- Evaluated models on both validation and test datasets using metrics:
  - **RMSE / MSE**
  - **Precision@10 / Recall@10 / F1@10**
  - **NDCG@10**
- Exported results to CSV for visualization and reporting.

---

## 📁 Folder Structure


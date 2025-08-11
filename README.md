# Task 5 - Exploratory Data Analysis (Titanic Dataset)

## 📌 Objective
Perform **Exploratory Data Analysis (EDA)** on the Titanic dataset to extract insights using visual and statistical exploration.

## 🛠 Tools Used
- **Python**
- **Pandas** – Data handling & preprocessing  
- **Matplotlib** & **Seaborn** – Data visualization  

## 📂 Files in this Repository
- `titanic_eda.py` → Python script for EDA  
- `train.csv` → Titanic dataset (training set from Kaggle)  
- `Titanic_EDA_Report.pdf` → Final PDF report containing all plots and insights  
- `plots/` → Folder with all generated plots  
- `README.md` → This documentation file  

## 📊 EDA Process
1. **Data Understanding**
   - Checked dataset info, description, and unique values
2. **Data Visualization**
   - Pairplot to see relationships between Age, Fare, and Survival
   - Heatmap for correlation between features
   - Histograms for Age & Fare
   - Boxplots comparing Age & Fare by survival
   - Scatterplot of Age vs Fare with survival status
3. **Observations**
   - Survivors generally paid higher fares
   - Higher survival rate in higher passenger classes
   - Age distribution shows majority between 20–40 years

## 📄 How to Run
1. Clone this repository:
   ```bash
   git clone <repo_url>
   cd Task5

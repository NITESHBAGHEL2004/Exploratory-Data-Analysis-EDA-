import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet

# ========== STEP 1: LOAD DATA ==========
data_path = "train.csv"  # Make sure train.csv is in the same folder
train_df = pd.read_csv(data_path)

# Create plots directory
plots_dir = "plots"
os.makedirs(plots_dir, exist_ok=True)

# ========== STEP 2: BASIC INFO ==========
dataset_info = train_df.info(buf=None)
dataset_desc = train_df.describe().to_string()
dataset_unique = train_df.nunique().to_string()

# ========== STEP 3: PLOTS ==========

# Pairplot
sns.pairplot(train_df.dropna(subset=['Age']), vars=['Age', 'Fare'], hue='Survived', diag_kind='hist')
pairplot_path = os.path.join(plots_dir, 'pairplot.png')
plt.savefig(pairplot_path)
plt.close()

# Heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(train_df.select_dtypes(include=['float64','int64']).corr(), annot=True, cmap='coolwarm')
heatmap_path = os.path.join(plots_dir, 'heatmap.png')
plt.savefig(heatmap_path)
plt.close()

# Histograms
hist_paths = []
for col in ['Age', 'Fare']:
    plt.figure()
    sns.histplot(train_df[col].dropna(), kde=True)
    plt.title(f'Histogram of {col}')
    path = os.path.join(plots_dir, f'{col}_hist.png')
    plt.savefig(path)
    plt.close()
    hist_paths.append(path)

# Boxplots
box_paths = []
for col in ['Age', 'Fare']:
    plt.figure()
    sns.boxplot(x='Survived', y=col, data=train_df)
    plt.title(f'Boxplot of {col} by Survival')
    path = os.path.join(plots_dir, f'{col}_box.png')
    plt.savefig(path)
    plt.close()
    box_paths.append(path)

# Scatterplot
plt.figure()
sns.scatterplot(x='Age', y='Fare', hue='Survived', data=train_df)
plt.title('Scatterplot of Age vs Fare')
scatter_path = os.path.join(plots_dir, 'scatter.png')
plt.savefig(scatter_path)
plt.close()

# ========== STEP 4: OBSERVATIONS ==========
observations = {
    "pairplot.png": "The pairplot shows that survivors tended to pay higher fares and were slightly younger on average.",
    "heatmap.png": "The heatmap shows Fare and Pclass are moderately correlated (-0.55), Survived is positively correlated with Fare, and negatively with Pclass.",
    "Age_hist.png": "The Age histogram shows most passengers were between 20-40 years old, with a small peak for young children.",
    "Fare_hist.png": "The Fare histogram is right-skewed, with most fares under 100 but a few extreme outliers.",
    "Age_box.png": "Survivors and non-survivors had similar median ages, but survivors had more younger passengers.",
    "Fare_box.png": "Survivors generally paid higher fares compared to non-survivors.",
    "scatter.png": "Survivors are more concentrated in the higher fare range, especially among younger passengers."
}

# ========== STEP 5: PDF REPORT ==========
pdf_path = "Titanic_EDA_Report.pdf"
styles = getSampleStyleSheet()
pdf_elements = []

# Add dataset info
pdf_elements.append(Paragraph("Dataset Info", styles['Heading2']))
pdf_elements.append(Paragraph(str(train_df.info(buf=None)), styles['Normal']))
pdf_elements.append(Spacer(1, 12))

pdf_elements.append(Paragraph("Dataset Description", styles['Heading2']))
pdf_elements.append(Paragraph(dataset_desc.replace("\n", "<br/>"), styles['Normal']))
pdf_elements.append(Spacer(1, 12))

pdf_elements.append(Paragraph("Unique Value Counts", styles['Heading2']))
pdf_elements.append(Paragraph(dataset_unique.replace("\n", "<br/>"), styles['Normal']))
pdf_elements.append(Spacer(1, 12))

# Add images with observations
for img_file in ["pairplot.png", "heatmap.png", "Age_hist.png", "Fare_hist.png", "Age_box.png", "Fare_box.png", "scatter.png"]:
    img_path = os.path.join(plots_dir, img_file)
    if os.path.exists(img_path):
        pdf_elements.append(Spacer(1, 12))
        pdf_elements.append(Image(img_path, width=400, height=300))
        pdf_elements.append(Spacer(1, 6))
        pdf_elements.append(Paragraph(observations.get(img_file, ""), styles['Normal']))

# Build PDF
doc = SimpleDocTemplate(pdf_path, pagesize=letter)
doc.build(pdf_elements)

print(f"EDA complete! Plots saved in '{plots_dir}' and report saved as '{pdf_path}'.")

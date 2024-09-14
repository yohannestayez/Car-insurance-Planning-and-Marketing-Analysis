import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns





# Main function to clean data

def display_descriptive_statistics(df):
    print("\nDescriptive Statistics:\n")
    display(df[['TotalPremium', 'TotalClaims', 'CalculatedPremiumPerTerm', 'SumInsured']].describe())

# Function to check Data Structure (data types)
def display_data_structure(df):
    print("\nData Structure:\n")
    display(df.dtypes)

# Function for Univariate Analysis of Numerical Variables
def plot_numerical_distribution(df):
    numerical_cols = ['TotalPremium', 'TotalClaims', 'CalculatedPremiumPerTerm', 'SumInsured']
    df[numerical_cols].hist(bins=20, figsize=(12, 8), color='skyblue', edgecolor='black')
    plt.suptitle('Histograms of Numerical Features')
    plt.show()

# Function for Univariate Analysis of Categorical Variables
def plot_categorical_distribution(df):
    categorical_cols = ['IsVATRegistered', 'Citizenship', 'LegalType', 'Title', 'Language', 
                        'Bank', 'AccountType', 'MaritalStatus', 'Gender', 'Province', 
                        'VehicleType', 'CoverType']

    # Set up the grid size for subplots (3 rows, 4 columns)
    n_rows, n_cols = 3, 4
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(16, 12))  # Adjust the figure size
    axes = axes.flatten()

    # Plot each categorical variable
    for i, col in enumerate(categorical_cols):
        sns.countplot(data=df, x=col, palette='Set2', ax=axes[i])
        axes[i].set_title(f'Distribution of {col}', fontsize=12)
        axes[i].tick_params(axis='x', rotation=45)

    plt.tight_layout()
    plt.show()

# Function for Correlation Matrix and Scatter Plot
def plot_correlation_and_scatter(df):
    # Correlation Matrix
    correlation_matrix = df[['TotalPremium', 'TotalClaims', 'CalculatedPremiumPerTerm', 'SumInsured']].corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Correlation Matrix')
    plt.show()

    # Scatter Plot
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='TotalPremium', y='TotalClaims', data=df, hue='Province', palette='viridis')
    plt.title('Scatter Plot of TotalPremium vs TotalClaims by Province')
    plt.show()

# Function to analyze trends over geography (Province)
def analyze_trends_by_province(df):
    grouped_data = df.groupby('Province')[['CoverType', 'CalculatedPremiumPerTerm']].agg(lambda x: x.value_counts().index[0])
    print("\nTrends Over Geography (Province):\n")
    display(grouped_data)

# Function for Outlier Detection (Box Plots)
def plot_outliers(df):
    numerical_cols = ['TotalPremium', 'TotalClaims', 'CalculatedPremiumPerTerm', 'SumInsured']
    plt.figure(figsize=(12, 8))
    for i, col in enumerate(numerical_cols):
        plt.subplot(2, 2, i + 1)
        sns.boxplot(x=df[col], palette='Set3')
        plt.title(f'Boxplot of {col}')
    plt.tight_layout()
    plt.show()

# Function for Custom Visualizations
def creative_visualizations(df):
    # Plot 1: Total Premium by VehicleType
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='VehicleType', y='TotalPremium', data=df, palette='husl')
    plt.xticks(rotation=45)
    plt.title('Total Premium Distribution by VehicleType')
    plt.show()

    # Plot 2: Total Claims Distribution by CoverType
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='CoverType', y='TotalClaims', data=df, palette='muted')
    plt.xticks(rotation=45)
    plt.title('Total Claims Distribution by CoverType')
    plt.show()

    # Plot 3: VehicleType vs CalculatedPremiumPerTerm
    plt.figure(figsize=(10, 6))
    sns.barplot(x='VehicleType', y='CalculatedPremiumPerTerm', data=df, palette='coolwarm')
    plt.xticks(rotation=45)
    plt.title('VehicleType vs CalculatedPremiumPerTerm')
    plt.show()
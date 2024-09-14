# Data Cleaning and Outlier Detection using IQR Method

## Overview
This notebook, `task1.ipynb`, is used to perform data cleaning and outlier detection using the Interquartile Range (IQR) method. It includes steps to handle missing values, remove duplicates, and detect outliers from a given dataset.

## Features
1. **Data Import**: Load the dataset into a pandas DataFrame.
2. **Data Cleaning**:
   - Handle missing values by either filling or dropping them.
   - Remove any duplicate rows to maintain data integrity.
3. **Outlier Detection** (Optional):
   - Calculate Q1 (25th percentile) and Q3 (75th percentile).
   - Compute the IQR and use it to detect and remove outliers.
4. **Error Handling**: The code is robust enough to handle common errors, such as unsupported operations on boolean values.

## Setup and Requirements

### Prerequisites
- Python 3.x
- Jupyter Notebook
- Required libraries:
  - `pandas`
  - `numpy`

### Install the required libraries
```bash
    pip install pandas numpy
```
### How to Run the Notebook
Clone this repository or download the task1.ipynb file.
Ensure you have the necessary libraries installed.
Open the notebook in Jupyter and run the cells step-by-step.
Ensure you have your dataset loaded properly in the correct format for processing.
### Common Errors and Fixes
If you encounter the following error:
TypeError: numpy boolean subtract, the `-` operator, is not supported...
This error is caused by trying to subtract boolean values. Ensure that the columns being processed contain numeric data, and modify the code to use logical operations where necessary.
Common Errors and Fixes
If you encounter the following error:

```
TypeError: numpy boolean subtract, the `-` operator, is not supported...
```
This error is caused by trying to subtract boolean values. Ensure that the columns being processed contain numeric data, and modify the code to use logical operations where necessary.

To fix it, use:

```
# Example fix for boolean subtraction error
IQR = np.logical_xor(Q3, Q1)
```
### Usage Instructions
Modify the dataset loading cell (df_cleaned = pd.read_csv(...)) to point to your dataset.
Customize the outlier detection logic as per your data requirements, especially if you're handling boolean columns or special data types.
### License
This project is open-source and available under the MIT License.


```
You can now select and paste it directly into your `README.md` file.
```



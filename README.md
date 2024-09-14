# Data Analysis Project

## Overview
This repository contains data analysis notebooks and modularized Python scripts for Exploratory Data Analysis (EDA). The notebooks in the `notebooks/` folder provide step-by-step analysis, while the `scripts/` folder contains reusable functions for EDA to keep the code modular and maintainable.

## Project Structure
The repository is structured as follows:

```
├── .vscode/
│   └── settings.json
├── .github/
│   └── workflows/
│       └── unittests.yml
├── .gitignore
├── requirements.txt
├── README.md
├── src/
│   └── __init__.py
├── notebooks/
│   ├──task1 EDA.ipynb
│   └── README.md
├── tests/
│   └── __init__.py
└── scripts/
    ├── __init__.py
    └── EDA_functions.py
```
### Key Components

- **notebooks/**: This folder contains the Jupyter notebooks used for data exploration and cleaning. The main file is `task1.ipynb` which includes the initial implementation of data import, cleaning, and outlier detection using the IQR method.
  
- **scripts/**: This folder contains Python scripts that modularize the functions used in the notebooks. The `eda_functions.py` file contains reusable functions such as handling missing values, detecting outliers, and other EDA tasks.

- **tests/**: This folder can be used for unit tests that ensure the functionality of the code in the `scripts/` directory.

### Running the Project

1. **Install dependencies**: Ensure you have Python 3.x installed and install the required packages using:

    ```bash
    pip install -r requirements.txt
    ```

2. **Running the Jupyter Notebook**:
    - Navigate to the `notebooks/` directory and open `task1.ipynb` in Jupyter Notebook.
    - Run the notebook cells sequentially for data cleaning and EDA.

3. **Using the Modular Functions**:
    - The `scripts/eda_functions.py` file contains reusable functions that were initially part of the notebook. You can import these functions in your Python code or notebooks as follows:
    ```python
    from EDA_functions import *
    ```

### Notebooks Breakdown
- **task1.ipynb**:
  - Loads data using `pandas`.
  - Performs data cleaning by handling missing values and removing duplicates.
  - Detects outliers using the IQR method.
  - Uses the modular functions defined in `eda_functions.py` for better code reuse and clarity.

### Scripts Breakdown
- **eda_functions.py**:
  - **`clean_data(df)`**: Cleans the input DataFrame by handling missing values and duplicates.
  - **`detect_outliers(df, column)`**: Detects and removes outliers from a specified column using the IQR method.
  - Additional functions for EDA tasks as needed.

### Testing
- If you have any unit tests in the `tests/` directory, you can run them using:
    ```bash
    python -m unittest discover -s tests
    ```

### GitHub Actions
- The project is set up with continuous integration using GitHub Actions. The workflow file `unittests.yml` ensures that the tests are automatically run on each push to the repository.

## License
This project is open-source and available under the MIT License.

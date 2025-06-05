# Data Explorer CLI Tool

A command-line tool to quickly load, summarize, and visualize data from CSV or Excel files. This tool helps in getting a quick overview of a dataset by providing descriptive statistics and generating basic plots.

## Features

- Loads data from CSV (`.csv`) and Excel (`.xlsx`, `.xls`) files.
- Displays comprehensive DataFrame information (similar to `df.info()`).
- Provides a summary of numerical columns (descriptive statistics like mean, std, min, max).
- Shows value counts for categorical columns.
- Generates and saves plots:
    - Histograms with Kernel Density Estimate (KDE) for numerical columns.
    - Bar plots for categorical columns.
- Allows users to specify the output directory for plots.
- Option to skip plot generation.

## Usage

To use the Data Explorer CLI tool, run the `data_explorer.py` script from your terminal.

**Basic Usage:**

```bash
python data_explorer.py <your_file.csv/xlsx>
```

**Examples:**

1.  **Load and process a CSV file (plots will be saved in the default 'plots' directory):**
    ```bash
    python data_explorer.py data.csv
    ```

2.  **Load and process an Excel file:**
    ```bash
    python data_explorer.py dataset.xlsx
    ```

3.  **Specify a custom directory for saving plots:**
    ```bash
    python data_explorer.py data.csv --plot-dir my_visualizations
    ```

4.  **Load data and summarize without generating plots:**
    ```bash
    python data_explorer.py data.csv --no-plots
    ```

## Dependencies

The script requires the following Python libraries:

-   pandas
-   matplotlib
-   seaborn

You can install them using pip:

```bash
pip install pandas matplotlib seaborn
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details (if a `LICENSE` file is added).
```

import argparse
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def load_data(file_path):
    """
    Loads data from a CSV or Excel file.
    """
    _, file_extension = os.path.splitext(file_path)
    if file_extension.lower() == '.csv':
        return pd.read_csv(file_path)
    elif file_extension.lower() in ['.xlsx', '.xls']:
        return pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file type. Please provide a CSV or Excel file.")

def summarize_data(df):
    """
    Generates a summary of the DataFrame.
    """
    print("\n--- DataFrame Info ---")
    df.info()

    print("\n--- Numerical Column Summary (df.describe()) ---")
    print(df.describe())

    print("\n--- Categorical Column Value Counts ---")
    for column in df.select_dtypes(include=['object', 'category']).columns:
        print(f"\n--- Value Counts for '{column}' ---")
        print(df[column].value_counts())

def generate_plots(df, output_dir="plots"):
    """
    Generates quick plots for numerical and categorical columns.
    Saves plots to a specified directory.
    """
    os.makedirs(output_dir, exist_ok=True)
    print(f"\n--- Generating Plots in '{output_dir}' ---")

    # Numerical plots (histograms)
    numerical_cols = df.select_dtypes(include=['number']).columns
    if not numerical_cols.empty:
        print("Generating histograms for numerical columns...")
        for col in numerical_cols:
            plt.figure(figsize=(8, 5))
            sns.histplot(df[col].dropna(), kde=True)
            plt.title(f'Histogram of {col}')
            plt.xlabel(col)
            plt.ylabel('Frequency')
            plt.tight_layout()
            plt.savefig(os.path.join(output_dir, f'{col}_histogram.png'))
            plt.close()
        print(f"Histograms saved to {output_dir}")
    else:
        print("No numerical columns found for histograms.")

    # Categorical plots (bar plots)
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns
    if not categorical_cols.empty:
        print("Generating bar plots for categorical columns...")
        for col in categorical_cols:
            plt.figure(figsize=(10, 6))
            df[col].value_counts().plot(kind='bar')
            plt.title(f'Bar Plot of {col}')
            plt.xlabel(col)
            plt.ylabel('Count')
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.savefig(os.path.join(output_dir, f'{col}_bar_plot.png'))
            plt.close()
        print(f"Bar plots saved to {output_dir}")
    else:
        print("No categorical columns found for bar plots.")

def main():
    parser = argparse.ArgumentParser(description="Data Explorer CLI Tool: Load CSV/Excel, summarize data, generate quick plots.")
    parser.add_argument("file_path", help="Path to the CSV or Excel file.")
    parser.add_argument("--no-plots", action="store_true", help="Do not generate plots.")
    parser.add_argument("--plot-dir", default="plots", help="Directory to save generated plots (default: 'plots').")

    args = parser.parse_args()

    try:
        print(f"Loading data from: {args.file_path}")
        df = load_data(args.file_path)
        print("Data loaded successfully.")

        summarize_data(df)

        if not args.no_plots:
            generate_plots(df, args.plot_dir)
            print("Plots generated successfully.")
        else:
            print("Plot generation skipped as requested.")

    except FileNotFoundError:
        print(f"Error: The file '{args.file_path}' was not found.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
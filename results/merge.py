import pandas as pd

def merge_csv(input_csv, output_csv, final_csv):
    df1 = pd.read_csv(input_csv)
    df2 = pd.read_csv(output_csv)
    
    merged_df = pd.merge(df1, df2, on='Title', how='outer')
    
    merged_df.to_csv(final_csv, index=False)
    
    print(f"Merged file saved as {final_csv}")

input_csv = 'input.csv'  
output_csv = 'output.csv'  
final_csv = 'final.csv'

merge_csv(input_csv, output_csv, final_csv)

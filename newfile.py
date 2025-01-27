import json
import csv

# Configuration: Input and Output filenames
INPUT_JSON = "/home/aru/Desktop/UCB_research/results/wikipedia_113_test.json"   # Replace with your input JSON file path
OUTPUT_CSV = "output.csv"   # Replace with desired output CSV path

def main():
    try:
        # Read JSON data from file
        with open(INPUT_JSON, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        
        # Process entries to extract titles and hidden_fruits
        results = []
        for entry in data:
            src = entry.get("src", "")
            # Extract title from "src" field
            title = "No Title Found"
            if "Title: " in src:
                title = src.split("Title: ")[1].split('\n')[0]
            # Extract hidden_fruits (empty list if missing)
            hidden_fruits = entry.get("hidden_fruits", [])
            results.append({"title": title, "hidden_fruits": hidden_fruits})
        
        # Write results to CSV
        with open(OUTPUT_CSV, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Title", "Hidden_Fruits"])
            for item in results:
                title = item['title']
                fruits_str = ",".join(item['hidden_fruits'])
                writer.writerow([title, fruits_str])
        
        print(f"Successfully generated CSV: {OUTPUT_CSV}")
    
    except FileNotFoundError:
        print(f"Error: File '{INPUT_JSON}' not found.")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{INPUT_JSON}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()
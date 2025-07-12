# Evaluating Docetl's operators

This repository contains code and data for an ongoing research project investigating the performance of language models on complex retrieval tasks like "needle in a haystack" problem. The project leverages [DocETL](https://github.com/ucbepic/docetl) for document extraction, transformation, and loading.

## Project Structure

```
fruits.yaml
main.ipynb
data/
    wikipedia.json
output/
    wikipedia_results.json
results/
```

- **main.ipynb**: Main Jupyter notebook containing the core data processing, Wikipedia article fetching, and experiment logic.
- **data/**: Stores the input JSON files with Wikipedia article data.
- **output/**: Contains output JSON files generated during experiments.
- **results/**: Contains CSV results, input/output data, and utility scripts.
- **fruits.yaml**: Yaml file used to run the experiment's pipeline.

## Project Overview

The goal of this project is to evaluate how well large language models can solve the "needle in a haystack" problem—retrieving or identifying a small, specific piece of information hidden within a large corpus of distractor text. We use Wikipedia articles as the base corpus, programmatically inject "needles" (e.g., random fruit names), and then test model retrieval capabilities.

### Key Steps

1. **Data Collection**: Fetches random Wikipedia articles and saves them as text files.
2. **Data Augmentation**: Randomly inserts "needle" words (e.g., fruit names) into articles.
3. **Preprocessing**: Cleans and processes articles, removing unwanted characters or formatting.
4. **Serialization**: Converts articles to JSON for downstream tasks.
5. **Evaluation**: Runs experiments to see if models can find the "needle" in the haystack.

## Usage

1. Run `main.ipynb` to fetch articles, inject needles, and generate datasets.
2. Use scripts in the `results/` folder to merge, analyze, and evaluate results.

## Status

This is an ongoing research project. Code and data formats may change as experiments evolve.

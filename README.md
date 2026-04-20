# Personality Type Detector

A simple machine learning project that determines a person's personality type (Introvert, Ambivert, Extrovert) based on three questions.

## What does this project do?

1. Trains a model on data from 1000 people
2. Creates a graph showing how the algorithm split people into groups
3. Runs a website where you can answer 3 questions and find out your personality type

## Project Files

| File | Description |
|------|-------------|
| `train_model.py` | Trains the model and creates a graph (run once) |
| `predict.py` | Console version for predictions |
| `app.py` | Web application (website with questions) |
| `requirements.txt` | List of required libraries |
| `kmeans_model.pkl` | Saved model (appears after training) |
| `scaler.pkl` | Saved scaler (appears after training) |
| `clusters.png` | Cluster graph (appears after training) |

## How to Run

### Step 1: Install Python
Download Python from the official website (version 3.8 or newer)

### Step 2: Install libraries
Open terminal (command prompt) in the project folder and run:
```bash
pip install -r requirements.txt

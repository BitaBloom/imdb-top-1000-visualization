# 🎥 IMDb Top 1000 Data Visualization

## Overview
This project focuses on analyzing and visualizing the IMDb Top 1000 movies dataset. Through various visualizations, the project highlights genre trends, popularity shifts over time, and the top contributors to these trends. The analysis utilizes a combination of static and interactive visualizations to provide insights into movie genres' evolution over the years.

## Features
- **Data Cleaning and Preprocessing**: Handles missing or malformed data and converts columns to appropriate types.
- **Genre Popularity Over Time**: Visualizes genre trends based on the total number of votes over the years.
- **Top Genres Analysis**: Plots the top 5 genres by total votes and their popularity trends.
- **Heatmap**: Displays the popularity of top genres over time in a heatmap format.
- **Top Movies Drill-down**: Analyzes the top movies driving the popularity spikes of specific genres and years.
- **Interactive Plot**: Uses Plotly to generate an interactive line plot of genre popularity over time.

## 📁 Project Structure
```
imdb-visualization/
🔸
├── code/                    # Code files for the project
│   └── code.py              # Main Python script
│
├── data/                    # Dataset files
│   └── imdb_top_1000.csv    # IMDb Top 1000 Movies dataset
│
├── reports/                 # Project documentation
│   └── report.pdf           # Detailed project report
│
├── requirements.txt         # Python dependencies
├── README.md                # Project overview and instructions
```

## 🛠️ Setup Instructions

### 1. Prerequisites
- **Python** (v3.8 or higher). Download from [python.org](https://www.python.org/downloads/).

### 2. Virtual Environment
Set up a virtual environment to manage dependencies:
- **Windows**:
  ```bash
  python -m venv myenv
  myenv\Scripts\activate
  ```
- **macOS/Linux**:
  ```bash
  python3 -m venv myenv
  source myenv/bin/activate
  ```

### 3. Install Dependencies
Install all required libraries:
```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Program
1. Place the dataset file (`imdb_top_1000.csv`) in the `data/` folder.
2. Execute the `code.py` script:
```bash
python code/code.py
```

---

## 🖋️ Results
- **Stacked Area Chart**: Displays total votes by genre over time.
- **Line Chart**: Visualizes the trends of the top 5 genres.
- **Heatmap**: Shows the intensity of genre popularity over the years.
- **Interactive Line Plot**: Analyzes genre popularity trends interactively.
- **Bar Chart**: Highlights top movies driving genre popularity.

---

## 📝 Documentation
- **Report**: See the detailed project report in the `reports/` folder.

---

## 🛠️ Troubleshooting
- Ensure all required files are in the correct folders (`code/`, `data/`, etc.).
- Missing dependencies? Run:
```bash
pip install -r requirements.txt
```
- Issues with the dataset? Ensure it's named correctly: `imdb_top_1000.csv`.

---

## 💡 Future Work
- Expand the dataset to include newer movies and TV shows.
- Explore machine learning techniques to predict genre popularity trends.

---

## 👩‍💻 Author
**Bita Nasserfarahmand**  
- [Email](mailto:bita.nf@gmail.com)

Feel free to contribute or reach out with questions!
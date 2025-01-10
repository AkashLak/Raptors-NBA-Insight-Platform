# Raptors (NBA) Insight Platform – Sports Analytics Tool 🏀📊

---

## 🚀 **Overview**
A **data-driven sports analytics tool** that leverages historical Raptors team statistics to forecast future performance and provide actionable insights for analysts and fans.

---

## 🔑 **Key Features:**

### 💾 **Relational Database (SQL)**
- Spearheaded the creation of a **relational database** using **SQL** to store **25 years of Raptors team statistics**.
  - Key metrics include **wins**, **losses**, and **rankings** with **year-by-year breakdowns**.
  - Enables **detailed trend analysis** over multiple seasons to understand patterns in team performance.

### 📈 **Data Visualization**
- Utilized **Plotly**, **Matplotlib**, and **Seaborn** to create **interactive visualizations**.
  - Showcases performance patterns, win-loss trends, and ranking dynamics for easy-to-understand insights.

### 🔮 **XGBoost Forecasting**
- Integrated **XGBoost** to forecast future **wins** based on historical time series data.
  - Achieved an **R² of 0.99** and **RMSE of 1.5**, providing **predictive insights** for analysts and decision-makers.

### ⚙️ **Model Optimization & Hyperparameter Tuning**
- **Grid Search** and **cross-validation** techniques used to optimize the model's performance and improve prediction accuracy:
  - **Hyperparameter Tuning** with **Grid Search** to identify the best set of model parameters.
  - Employed **Cross-validation** to ensure the model generalizes well across different subsets of data and reduces overfitting.

### 🏆 **Optimized Model Performance**
- Fine-tuned the **XGBoost model** using the best hyperparameters to achieve optimal performance:
  - Enhanced the model’s predictive power, helping analysts make more accurate forecasts based on historical data.

## 🎯 **Impact:**
- A powerful tool that transforms **historical data** into **predictive insights**, enabling sports analysts to better forecast future performance and trends of the Raptors.
- The platform offers a detailed breakdown of past performance while providing actionable predictions that assist with team strategies and decision-making.

## 🛠️ **Technologies Used:**
- **SQL** for database management
- **Plotly** and **Matplotlib** for data visualization
- **XGBoost** for predictive modeling
- **Python** for data analysis and manipulation
- **Grid Search** and **cross-validation** for hyperparameter tuning and model optimization

## 🚀 **Usage:**
- Ideal for sports analysts, enthusiasts, and anyone interested in deep data-driven insights into the Raptors' performance over the years.





***Final Result Website for User (Process steps below img):*** 
![Screenshot 2025-01-10 at 6 21 18 AM](https://github.com/user-attachments/assets/43003be5-892b-428e-8ede-eee12722ae93)


***Code for SQL database:***

<img width="562" alt="Screenshot 2025-01-06 at 1 41 42 PM" src="https://github.com/user-attachments/assets/65f74f7c-ffa9-4b8b-b4ee-bcce9345aeef" />
<img width="503" alt="Screenshot 2025-01-06 at 1 42 19 PM" src="https://github.com/user-attachments/assets/212fe76f-c841-4d54-a98f-b907565998a4" />
<img width="516" alt="Screenshot 2025-01-06 at 1 42 29 PM" src="https://github.com/user-attachments/assets/1434c701-0661-4141-84b5-4e7e089bd7e2" />


***Code for Jupyter Notebook: SQL querying, seaborn graphs, and interactive graphs(plotly)*** 
![Screenshot 2025-01-06 at 12 21 54 PM](https://github.com/user-attachments/assets/15e85272-bc43-492b-bfef-dbee401bbaa4)
![Screenshot 2025-01-06 at 12 22 06 PM](https://github.com/user-attachments/assets/d47da36d-c973-41bf-bcd5-e93041c37991)
![Screenshot 2025-01-06 at 12 22 20 PM](https://github.com/user-attachments/assets/51d02922-9a6c-47d7-829b-f7de3d469a70)
![Screenshot 2025-01-06 at 12 22 32 PM](https://github.com/user-attachments/assets/b0b7d824-828d-4382-8d1f-da3c11560f39)

***Code for XGBoost model development, training and hypertuning/optimization*** 
![Screenshot 2025-01-10 at 6 19 26 AM](https://github.com/user-attachments/assets/24810883-94a9-4389-9aed-2b6686bbd594)
![Screenshot 2025-01-10 at 6 01 43 AM](https://github.com/user-attachments/assets/db60603a-cf24-4e97-99ba-eed3ee761657)

***Code for graph comparisons between test data and predicted (persisting model)***
![Screenshot 2025-01-10 at 6 07 42 AM](https://github.com/user-attachments/assets/982af1b7-7679-435e-a2e9-c15d209442b3)









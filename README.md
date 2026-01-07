# 🎓 Learning Risk Evaluation Model

### **Executive Summary**
In the financial sector, minimizing "False Positives" (approving bad loans) is critical to profitability. This project is an end-to-end Machine Learning application designed to automate the credit risk assessment process.

By leveraging a **Random Forest Classifier**, this tool analyzes applicant demographics and loan characteristics to predict the likelihood of default in real-time.



### **⚙️ How It Works (The Architecture)**

The system operates on a three-stage pipeline: **Data Generation -> Model Training -> Deployment.**

#### **1. The Data Strategy**
To ensure robust training without external dependencies, the model is trained on a controlled **Synthetic Dataset** of 500 financial records.
* **Logic:** The data simulates real-world banking patterns (e.g., older applicants with smaller, short-term loans are statistically lower risk).
* **Features Used:**
    * `Age`: Applicant's age (18–75).
    * `Credit Amount`: Total value of the loan ($500–$15,000).
    * `Duration`: Repayment period (6–72 months).

#### **2. The Machine Learning Engine**
* **Algorithm:** Random Forest Classifier (Ensemble Method).
* **Why Random Forest?** Unlike simple Logistic Regression, Random Forest handles non-linear relationships between age and loan amount effectively. It aggregates multiple "Decision Trees" to reduce overfitting and improve prediction stability.
* **Performance:** The model learns specific "Risk Rules" (e.g., High Amount + Young Age + Long Duration = High Risk) and applies them to new, unseen data.

#### **3. The Deployment (Streamlit)**
The frontend is built using **Streamlit**, allowing non-technical stakeholders (Loan Officers) to interact with the model.
* **Input Layer:** Users adjust sliders for Age, Amount, and Duration.
* **Processing Layer:** Inputs are converted into a Pandas DataFrame to match the training schema.
* **Inference Layer:** The serialized model (`.pkl`) computes the probability and returns a binary classification (Good/Bad Risk).

---

### **📂 Project Structure**

* **`train_model.ipynb` (The Lab):**
    * Generates the synthetic training data.
    * Trains the Random Forest Classifier.
    * Serializes (saves) the trained model as a `.pkl` file.

* **`app.py` (The Interface):**
    * Loads the saved model artifact.
    * Renders the web-based user interface.
    * Handles user input and displays the prediction result.

* **`credit_model.pkl` (The Artifact):**
    * The binary file containing the trained model's logic and decision trees.

---

### **🚀 How to Run Locally**

1.  **Install Dependencies:**
    ```bash
    pip install streamlit pandas scikit-learn numpy
    ```

2.  **Train the Model:**
    Run the notebook `train_model.ipynb` to generate the `credit_model.pkl` file.

3.  **Launch the App:**
    ```bash
    python -m streamlit run app.py
    ```
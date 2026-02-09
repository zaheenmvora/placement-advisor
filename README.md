  #  Placement Advisor System (Rule-Based + ML Hybrid)

  An end-to-end Placement Preparation System that analyzes student skill profiles using a hybrid rule-based and machine learning approach to recommend suitable career domains, generate probability-based predictions, and suggest company-fit preparation paths.

  This project demonstrates a complete full-stack workflow including profile evaluation, domain scoring, ML classification, probability visualization, and Flask-based web deployment.

  ---

  ##  Project Overview

  Choosing the right career domain during placements can be challenging for students. This system assists students by evaluating their technical strengths and providing structured guidance.

  This system:

  - Analyzes technical skill ratings
  - Applies rule-based domain scoring
  - Uses machine learning classification for prediction
  - Displays probability-based recommendations
  - Calculates overall profile strength score
  - Suggests relevant companies
  - Generates preparation roadmap

  The project follows a modular and reproducible hybrid decision-making workflow suitable for placement analytics.

  ---

  ## System Architecture

  User Input → Profile Evaluation → Rule-Based Scoring → ML Classification → Probability Analysis → Company Mapping → Roadmap Generation → Web Output

  The design is modular, interpretable, and extendable.

  ---

  ##  Input Parameters

  - DSA Skill Level (1–5)
  - Python Skill Level (1–5)
  - Web Development Skill Level (1–5)
  - Machine Learning Skill Level (1–5)
  - Operating Systems Knowledge (1–5)
  - DBMS Knowledge (1–5)
  - CGPA

  ---

  ##  Machine Learning Approach

  ### 🔹 Problem Type
  Multi-Class Classification

  ### 🔹 Model Used
  Scikit-learn Classifier (e.g., Logistic Regression)

  ### 🔹 Why This Model?

  - Suitable for multi-class classification
  - Lightweight and efficient
  - Provides probability outputs
  - Interpretable decision boundaries
  - Ideal for skill-based domain prediction

  ---

  ##  Rule-Based Logic

  - SDE → High DSA + OS + DBMS
  - Data Science → High Python + ML
  - Web Dev → High Web + Python
  - Core CS → Strong theoretical foundation

  This ensures explainable and transparent recommendations.

  ---

  ##  Profile Strength Calculation

  Overall Score = Average of technical skill ratings  
  Converted to percentage (0–100%)  

  Displayed visually using a dynamic progress bar.

  ---

  ##  ML Prediction Output (Example)

  SDE: 0.58  
  Data Science: 0.23  
  Web Dev: 0.14  
  Core CS: 0.05  

  The highest probability domain is highlighted in the UI.

  ---

  ##  Company Fit Suggestions

  - SDE → Amazon, Google, Microsoft, Adobe
  - Data Science → Flipkart, JPMorgan, Zomato
  - Web Dev → Infosys, TCS Digital, Zoho
  - Core CS → Oracle, Qualcomm, Intel

  ---

  ##  Web Interface Features

  - Modern UI using HTML & CSS
  - Skill-based input form
  - Rule-based domain recommendation
  - ML probability visualization bars
  - Profile strength score display
  - Company-fit badges
  - Structured preparation roadmap

  ---

  ##  Project Structure

  placement-advisor/

    templates/
      ├── index.html
      └── result.html

    static/
      └── style.css

    app.py
    rule_engine.py
    ml_model.py
    requirements.txt
    Procfile
    README.md

  ---

  ##  Installation

  git clone https://github.com/yourusername/placement-advisor.git  
  cd placement-advisor  

  python -m venv venv  
  venv\Scripts\activate  

  pip install -r requirements.txt  

  ---

  ##  Running the Project

  python app.py  

  Open in browser:  
  http://127.0.0.1:5000  

  The system will:
  1. Accept student skill input
  2. Apply rule-based evaluation
  3. Generate ML-based prediction
  4. Display probability scores
  5. Suggest company-fit recommendations
  6. Show preparation roadmap

  ---

  ##  Model Capabilities

  - Multi-class domain prediction
  - Probability-based classification
  - Hybrid rule + ML reasoning
  - Dynamic UI visualization
  - Modular architecture

  ---

  ## 🛠 Technologies Used

  - Python
  - Flask
  - NumPy
  - Scikit-learn
  - HTML
  - CSS
  - Gunicorn

  ---

  ##  Key Concepts Demonstrated

  - Hybrid Decision Systems
  - Multi-Class Classification
  - Feature-Based Prediction
  - Rule-Based Scoring Logic
  - Web + ML Integration
  - Full-Stack Deployment

  ---

  ##  Future Enhancements

  - Company readiness scoring
  - Resume analysis module
  - Authentication & profile saving
  - Dashboard analytics
  - Deployment on cloud platform

  ---

  ## Disclaimer

  This project is developed for educational purposes only and does not guarantee placement outcomes.

  ---

  ## Author

  Zaheen M Vora  
  Computer Engineering Student | Aspiring Data Science and ML Engineer


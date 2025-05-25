#Resume Category Predictor
A web-based application that uses Natural Language Processing (NLP) and Machine Learning to automatically classify resumes into relevant job categories.

##Overview
Recruiters often deal with large volumes of resumes, making the screening process time-consuming and inconsistent. This project automates resume categorization to streamline the hiring workflow and reduce manual effort.

Users can upload a PDF resume, and the system will predict the most relevant job domain (e.g., Data Science, Web Development, HR) in real-time.

##Features
Upload resumes in PDF format

Instant job category prediction

Clean, responsive user interface

Preprocessing and noise removal for unstructured text

Easy to deploy and extend

Designed for integration into applicant tracking systems (ATS)

##Technology Stack
Backend: Python, Flask

Frontend: HTML

PDF Processing: pdfplumber

Text Cleaning: Regular expressions

Vectorization: TF-IDF

Modeling: Scikit-learn (Logistic Regression or SVM)

Encoding: LabelEncoder for category translation

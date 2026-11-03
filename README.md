# 💧 WaterBuddy – Your Daily Hydration Companion

## 📌 Project Overview

WaterBuddy is a Python-based web application developed using Streamlit. It helps users track their daily water intake and monitor their hydration progress throughout the day.

The application provides personalised daily water intake goals based on the user's age group. Users can log the amount of water they drink, view their progress in real time, and receive motivational messages as they reach hydration milestones.

The main aim of WaterBuddy is to encourage users to develop consistent and healthy hydration habits through a simple, interactive, and user-friendly interface.

## 🎯 Project Objectives

- To create an interactive web application using Python and Streamlit.
- To suggest daily water intake goals based on the user's age group.
- To allow users to record their daily water consumption.
- To calculate the total water intake and remaining water.
- To display hydration progress using visual indicators.
- To motivate users through milestone-based messages and mascot reactions.
- To provide a reset option for starting a fresh daily hydration record.

## ✨ Features

### 1. Age-Based Daily Water Goal

Users can select their age group, and WaterBuddy automatically suggests a daily water intake goal.

The suggested goals are:

| Age Group            | Suggested Daily Goal |
| -------------------- | -------------------- |
| Kids (6–12 years)    | 1600 ml              |
| Teens (13–18 years)  | 2000 ml              |
| Adults (19–50 years) | 2500 ml              |
| Seniors (65+ years)  | 1800 ml              |

Users can also manually adjust their daily water intake goal.

### 2. Quick Water Logging

Users can quickly record their water consumption through predefined buttons:

- 150 ml
- 250 ml
- 350 ml
- 500 ml

A custom input option is also available for entering any other quantity of water.

### 3. Real-Time Hydration Tracking

WaterBuddy automatically calculates and displays:

- **Total Intake:** The total amount of water consumed.
- **Remaining Water:** The amount required to reach the daily goal.
- **Goal Achievement:** The percentage of the daily target completed.

All calculations update whenever the user logs additional water.

### 4. Visual Progress Indicator

A progress bar provides a visual representation of the user's daily hydration progress. It updates automatically as more water is logged.

### 5. Motivational Messages and Mascot

WaterBuddy displays encouraging messages and mascot reactions at different hydration milestones.

These milestones include:

- 25% – A good start!
- 50% – Halfway there!
- 75% – Almost at your goal!
- 100% – Daily goal achieved!

### 6. Daily Reset Option

Users can reset their water intake record to start tracking from zero again. A confirmation option is provided before resetting the progress.

### 7. Hydration Tips

The application provides useful hydration tips to encourage users to maintain consistent water-drinking habits.

### 8. Cups-to-Millilitres Converter

A built-in converter helps users understand the equivalent quantity of water in cups and millilitres.

## 🛠️ Technologies Used

- **Python:** Main programming language used for application logic and calculations.
- **Streamlit:** Python framework used to create the interactive web application.
- **HTML and CSS:** Used through Streamlit styling to improve the visual appearance and user interface.
- **Session State:** Used to maintain user data and water intake records during an active application session.

## 📂 Project Structure

```
WaterBuddy/
│
├── app.py
│
├── requirements.txt
│
└── README.md
```

### File Description

- `app.py` – Contains the complete Python code for the WaterBuddy application.
- `requirements.txt` – Contains the Python libraries required to run the application.
- `README.md` – Contains the project overview, features, installation instructions, and usage information.

## ⚙️ Installation and Setup

Follow these steps to run WaterBuddy on your computer.

### Step 1: Install Python

Download and install Python from the official Python website.

### Step 2: Download the Project

Download or clone the project repository to your computer.

### Step 3: Open the Project Folder

Open the project folder in Visual Studio Code or any preferred code editor.

### Step 4: Install the Required Library

Open the terminal and execute:

```
pip install -r requirements.txt
```

### Step 5: Run the Application

Execute the following command:

```
streamlit run app.py
```

The application will open automatically in your default web browser.

## 🚀 Deployment Using Streamlit Community Cloud

WaterBuddy can be deployed online using Streamlit Community Cloud.

1. Upload `app.py`, `requirements.txt`, and `README.md` to a GitHub repository.
2. Visit Streamlit Community Cloud.
3. Sign in using your GitHub account.
4. Select **Create App**.
5. Choose the GitHub repository containing the WaterBuddy project.
6. Select `app.py` as the main application file.
7. Click **Deploy**.

Once deployment is complete, Streamlit will generate a public URL through which the application can be accessed.

## 🧮 Working and Calculation Logic

WaterBuddy uses basic mathematical calculations to track hydration progress.

**1. Total Water Intake**

Total Intake = Sum of all logged water quantities.

**2. Remaining Water**

Remaining Water = Daily Goal − Total Intake.

The remaining amount is displayed as zero once the daily goal has been achieved.

**3. Percentage of Goal Achieved**

Percentage = (Total Intake ÷ Daily Goal) × 100.

The progress indicator displays the percentage, with its visual progress capped at 100%.

## 🔒 Data Storage and Privacy

WaterBuddy uses Streamlit Session State to maintain the user's water intake information while the application session is active.

The application does not require user registration or login and does not use an external database.

The daily tracking information is temporary and is not intended to be permanent storage.

## 📌 Conclusion

WaterBuddy demonstrates how Python and Streamlit can be used to develop an interactive application that addresses a practical everyday need.

By combining age-based water goals, quick water logging, automatic calculations, visual progress indicators, and motivational feedback, the application makes daily hydration tracking simple and engaging.

The project demonstrates the use of Python programming concepts, conditional statements, functions, calculations, user input, and session management in developing a functional web application.

---

**Note:** The suggested water intake goals are predefined project values for demonstration purposes and should not be treated as personalised medical recommendations.


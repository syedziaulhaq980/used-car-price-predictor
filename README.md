\# 🚗 Used Car Price Predictor



\### Machine Learning Powered Vehicle Valuation



A simple and interactive machine learning web application that predicts the estimated price of a used car based on its specifications.



Built with \*\*Python, Scikit-learn, XGBoost and Streamlit\*\* and deployed on \*\*Render\*\*.



<p align="center">



<a href="https://used-car-price-predictor-1-rvn5.onrender.com/">

<img src="https://img.shields.io/badge/🚗%20Live%20Demo-Visit%20App-2563EB?style=for-the-badge">

</a>



<a href="https://github.com/syedziaulhaq980/used-car-price-predictor">

<img src="https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge\&logo=github">

</a>



</p>



\---



\## 📌 About The Project



Buying or selling a used car can make it difficult to determine a reasonable market price.



This project uses a trained machine learning model to estimate the price of a used vehicle from information such as:



\* 🚘 Car title

\* 📅 Registration year

\* 🛣️ Mileage

\* 👤 Previous owners

\* ⚙️ Engine size

\* ⛽ Fuel type

\* 🚗 Body type

\* 🔧 Gearbox

\* 🚪 Number of doors

\* 💺 Number of seats

\* 🌱 Emission class

\* 📖 Service history



The application provides the predicted price through a clean and simple web interface.



\---



\## ✨ Features



| Feature                | Description                                   |

| ---------------------- | --------------------------------------------- |

| 🚗 Vehicle Information | Enter detailed vehicle specifications         |

| 🤖 ML Prediction       | Predict used-car prices using a trained model |

| ⚡ Instant Results      | Get the prediction immediately                |

| 📋 Vehicle Summary     | Review the information used for prediction    |

| 🌐 Web Application     | Access the model through a browser            |

| ☁️ Cloud Deployment    | Hosted online using Render                    |



\---



\## 🧠 Machine Learning



The application uses an \*\*XGBoost regression model\*\* inside a Scikit-learn preprocessing pipeline.



\### Numerical Features



\* Mileage

\* Registration Year

\* Previous Owners

\* Engine

\* Doors

\* Seats



These features are processed using:



\*\*StandardScaler\*\*



\### Categorical Features



\* Car Title

\* Fuel Type

\* Body Type

\* Gearbox

\* Emission Class

\* Service History



These features are processed using:



\*\*OneHotEncoder\*\*



The complete trained pipeline is stored in:



```text

used\_car\_price\_model.pkl

```



\---



\## 🔄 How It Works



```text

&#x20;       Vehicle Details

&#x20;             ↓

&#x20;    Data Preprocessing

&#x20;             ↓

&#x20;     Machine Learning

&#x20;          Model

&#x20;             ↓

&#x20;     Price Prediction

&#x20;             ↓

&#x20;      Estimated Value

```



\### 1️⃣ Enter Vehicle Details



Provide the specifications of the used car.



\### 2️⃣ Process The Data



The input data is passed through the same preprocessing pipeline used during model training.



\### 3️⃣ Generate Prediction



The trained XGBoost model predicts the estimated vehicle price.



\### 4️⃣ Display Result



The predicted price and vehicle summary are displayed in the application.



\---



\## 🛠️ Tech Stack



\### Programming Language



!\[Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square\\\&logo=python\\\&logoColor=white)



\### Machine Learning



!\[Scikit Learn](https://img.shields.io/badge/Scikit--learn-ML-F7931E?style=flat-square\\\&logo=scikit-learn\\\&logoColor=white)

!\[XGBoost](https://img.shields.io/badge/XGBoost-Regression-189C38?style=flat-square)



\### Data Processing



!\[Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458?style=flat-square\\\&logo=pandas\\\&logoColor=white)



\### Web Application



!\[Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?style=flat-square\\\&logo=streamlit\\\&logoColor=white)



\### Deployment



!\[Render](https://img.shields.io/badge/Render-Deployment-46E3B7?style=flat-square\\\&logo=render\\\&logoColor=black)



\---



\## 📂 Project Structure



```text

used-car-price-predictor/

│

├── app1.py

│

├── used\_car\_price\_model.pkl

│

├── requirements.txt

│

└── README.md

```



\---



\## 💻 Run The Project Locally



\### Clone the repository



```bash

git clone https://github.com/syedziaulhaq980/used-car-price-predictor.git

```



\### Open the project folder



```bash

cd used-car-price-predictor

```



\### Install dependencies



```bash

pip install -r requirements.txt

```



\### Start the application



```bash

streamlit run app1.py

```



The application will open in your browser.



\---



\## 🌐 Live Application



Try the deployed application:



\### 🚗 \[Open AutoValue](https://used-car-price-predictor-1-rvn5.onrender.com/)



\---



\## 📸 Application Preview



Add screenshots of your application here.



For example:



```text

screenshots/

├── home.png

└── prediction.png

```



Then you can display them in this section:



```markdown

!\[Application Screenshot](screenshots/home.png)

```



\---



\## 📈 Model Input Features



| Feature           | Type        |

| ----------------- | ----------- |

| Car Title         | Categorical |

| Mileage           | Numerical   |

| Registration Year | Numerical   |

| Previous Owners   | Numerical   |

| Fuel Type         | Categorical |

| Body Type         | Categorical |

| Engine            | Numerical   |

| Gearbox           | Categorical |

| Doors             | Numerical   |

| Seats             | Numerical   |

| Emission Class    | Categorical |

| Service History   | Categorical |



\---



\## ⚠️ Disclaimer



This application provides an \*\*estimated vehicle price generated by a machine learning model\*\*.



Actual market prices may differ depending on factors such as vehicle condition, location, demand, mileage, maintenance, specifications and current market conditions.



\---



\## 👨‍💻 Author



\### Syed ZiaUl Haq



<a href="https://github.com/syedziaulhaq980">

<img src="https://img.shields.io/badge/GitHub-syedziaulhaq980-181717?style=for-the-badge\&logo=github">

</a>



\---



<p align="center">



\### 🚗 Used Car Price Predictor



\*\*Built with Python \& Machine Learning\*\*



⭐ If you found this project useful, consider giving it a star!



</p>




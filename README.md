# Algerian-Forest-Fire
Welcome to the repository showcasing a **predictive model for Algerian forest fires**, utilizing data sourced from the [UCI repository](https://archive.ics.uci.edu/dataset/547/algerian+forest+fires+dataset). This project focuses on the analysis and prediction of forest fire occurrences in two distinct regions of Algeria: the Bejaia region situated in the northeast and the Sidi Bel-abbes region positioned in the northwest.

The dataset encapsulates a total of **244 instances**, evenly divided between these two regions, with 122 instances attributed to each. The time span covered within this dataset spans from June 2012 to September 2012, providing a comprehensive view of the forest fire occurrences during this period.

Comprising **11 distinct attributes** and an additional **output attribute ('class')**, this dataset encompasses a diverse range of information crucial for understanding the factors influencing forest fires. Among the 244 instances, 138 instances have been classified as fire occurrences while the remaining 106 instances denote instances where fires were absent.

This project delves into the application of machine learning algorithms to predict and classify forest fire incidents, aiming to offer insights into the patterns, factors, and conditions contributing to these occurrences in the aforementioned Algerian regions. The predictive model developed here serves as a valuable tool not only for understanding historical trends but also for preemptively assessing and managing potential forest fire risks in these regions.

Through this repository, we present our analysis, methodology, and predictive models, aiming to contribute to the domain of forest fire prediction and provide a resource for researchers, environmentalists, and stakeholders invested in forest conservation and fire prevention efforts in Algeria.

## The Steps taken for this project is 
### Data Preprocessing:

- Data Collection: Obtained the dataset from the UCI repository.
- Data Cleaning: Handled missing values, outliers, and inconsistencies.
- Feature Selection: Identified relevant features and attributes for analysis.
- Data Transformation: Encoded categorical variables, normalize/standardize numerical data.

### Exploratory Data Analysis (EDA):

- Statistical Analysis: Computed descriptive statistics, correlations, and distributions.
- Data Visualization: Generated graphs (histograms, box plots, scatter plots, etc.) to understand relationships and patterns in the data.
- Identify Insights: Analyzed trends and potential influential factors on forest fire occurrences in both regions.

### Model Building:

- For Regression Problem algorithm decided to predict the feature Temperature.
- Models used : Linear regression, Lasso Regression, Ridge Regression, Random forest, Decision tree, K-Nearest Neighbour regressor, Support Vector Regressor.
- For Classification algorithm decided to predict the features Classes from the dataset which is Binary classification (fire, not fire).
- Models used : Logistic Regression, Decision Tree, Random Forest, XGboost, K-Nearest Neighbour.

### Creating Flask Module:

- Developed a Flask-based web application to showcase the trained models.
- Integrated user interface elements for user input and model predictions.
- Implemented functionality to interact with the trained models for regression and classification.

### Deployment on GCP and Render:

- Deployed the Flask application on Google Cloud Platform (GCP) using appropriate services.
- Also used Render to host the application and make it accessible to users.

  Link - [Forest Fire Prediction](https://algerian-forest-fire-nfzo.onrender.com/)

  
![Screenshot (102)](https://github.com/Shiti09/Algerian-Forest-Fire/assets/119621887/41bbd020-b6c4-4160-bde1-2e1aa95ccc1b)

Index page which lets you choose if you would like to go for single regression or batch regression or single classification or batch classification.

![Screenshot (103)](https://github.com/Shiti09/Algerian-Forest-Fire/assets/119621887/451d3fed-ddae-4c72-b7ae-bdcd124c5b18)

Single Classification page where you fill in the details and it would let you know whether it would be fire or no fire.

![Screenshot (104)](https://github.com/Shiti09/Algerian-Forest-Fire/assets/119621887/79a85ecb-dc7d-4c50-9d05-cf29619250cf)

Display of result - No Fire

![Screenshot (105)](https://github.com/Shiti09/Algerian-Forest-Fire/assets/119621887/3181b3a8-9fec-4d91-a8a8-67d5c52f1d33)

Batch Prediction Page which lets you upload CSV file.

![Screenshot (106)](https://github.com/Shiti09/Algerian-Forest-Fire/assets/119621887/c9e58024-5dc0-418c-a478-3ce8aa953638)

Batch Prediction results which predicts the temprature for all the instances. 










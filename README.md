# MSIHealthServiceAnalytics

📦 MSI_Client_Exit_Analysis
├── 📁 docs/
│   ├── PACE_Framework.md         # Overview of the PACE framework for this project
│   ├── Stakeholder_Requirements.md # Stakeholder needs and objectives
│   ├── Workflow_Diagram.png      # Visual workflow for data processing and analysis
│   ├── Questionnaire_Documentation.md # Description of questionnaire and data fields
│   └── Readme.md                 # Main project description and guidelines
├── 📁 data/
│   ├── raw/                      # Original raw survey data (read-only)
│   ├── interim/                  # Data after cleaning and preprocessing
│   ├── processed/                # Final datasets ready for analysis
│   ├── metadata/                 # Metadata about variables and codes
│   └── logs/                     # Logs for data cleaning and processing
├── 📁 notebooks/
│   ├── 01_EDA.ipynb              # Exploratory Data Analysis notebook
│   ├── 02_Data_Cleaning.ipynb    # Data cleaning and preprocessing
│   ├── 03_Descriptive_Analysis.ipynb # Descriptive analysis of survey responses
│   ├── 04_Inferential_Analysis.ipynb # Inferential analysis with hypotheses tests
│   ├── 05_Visualizations.ipynb   # Data visualization notebook
│   └── templates/                # Templates for creating new analysis notebooks
├── 📁 src/
│   ├── data_processing/
│   │   ├── clean_data.py         # Scripts for data cleaning
│   │   ├── preprocess_data.py    # Preprocessing functions
│   │   └── validate_data.py      # Validation and integrity checks
│   ├── analysis/
│   │   ├── descriptive_analysis.py # Descriptive statistics functions
│   │   ├── inferential_tests.py  # Statistical tests and models
│   │   └── eda_utils.py          # Utilities for EDA
│   ├── visualization/
│   │   ├── create_charts.py      # Scripts for generating visualizations
│   │   └── generate_reports.py   # Functions to compile analysis reports
│   └── utils/
│       ├── config.py             # Configuration file for paths and constants
│       └── logger.py             # Logging utility
├── 📁 reports/
│   ├── figures/                  # Figures generated during analysis
│   ├── tables/                   # Tables summarizing results
│   ├── Summary_Report.pdf        # Final project report
│   └── Stakeholder_Report.pdf    # Tailored report for stakeholders
├── 📁 tests/
│   ├── test_data_cleaning.py     # Unit tests for cleaning scripts
│   ├── test_analysis.py          # Unit tests for analysis scripts
│   └── test_visualization.py     # Unit tests for visualization scripts
├── .gitignore                    # Ignore unnecessary files and directories
├── LICENSE                       # License file
├── README.md                     # Project overview and instructions
└── requirements.txt              # Dependencies for the project

# Project Content
Main goal of this project is to extract and transform data about taxi-trips and weather automatically with Amazon Web Services and create some visualizations based on resulted data.

# Description
The raw data is coming about the taxi-trips in Chicago and weather conditions at different time. Jupyter notebooks are including the "discovery-files" to perform initial web-scraping and create initial mapping or dimension-tables regarding these data-sets. In this repo AWS Lambda-functions can be also found, that are responsible to manipulate data on AWS environment, where GLUE and Athena is also used to inspect data. At the end of project, transformed data is requested from AWS and some charts, diagrams have been exported to visualize the results.

## Usage
Data extraction and transforming is carried out by AWS, so data should be requested from s3-bucket with "08_local_vizualizations" notebook, where plots can be created for better insight.

## Project Status
The main task is currently working, and base-project has been finalized, but it can be extended with additional features, combine it with additional data sources and improve the vizualizations to check resulted data.

## Visual demonstration
Some evaluated charts about transformed data can be seen below:

<img width="630" height="469" alt="Chart_1" src="https://github.com/user-attachments/assets/390c037e-0ff8-497e-bf32-d6dda379659f" />
<img width="630" height="470" alt="Chart_2" src="https://github.com/user-attachments/assets/dfaf3920-346d-4879-ae9b-249c1cad4724" />
<img width="630" height="470" alt="Chart_3" src="https://github.com/user-attachments/assets/f05a5df4-fcc2-4b0f-a894-d162dd9f53c9" />
<img width="630" height="470" alt="Chart_4" src="https://github.com/user-attachments/assets/fb7a9107-cb92-4dfd-9bc9-ffb5438c1dae" />
<img width="630" height="469" alt="Chart_5" src="https://github.com/user-attachments/assets/1c19489c-f871-47d7-bc38-2bdce6e8b4df" />


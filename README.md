# ABSTRACT

Detection and monitoring of landslides in Alkumru dam reservoir is important due to the danger they pose to local people, and the maintenance and sustainable use of the infrastructure. Sentinel-1 Synthetic Aperture Radar Interferometry (InSAR) datasets and their processing methods provide multi-time surface change information in terms of deformation and enable engineering geological analysis. In this study, we plan to analyze the deformations in large landslides by using InSAR measurements in the reservoir of Alkumru Dam and make estimations of future movements that may occur based on these analyses. The area is prone to landslides of various sizes. For this purpose, Synthetic Aperture Radar and Continental Viewing from Space (LiCSAR) products will be used to apply the Small-Baseline Subsets (SBAS) method for deformation extraction from Sentinel-1 time series datasets. Time series analysis results will be used as input for machine learning methods to predict the future movements.

# INTRODUCTION

One of the biggest challenges humanity has been facing is natural disasters, which may not be prevented. Although the types and severity of disasters vary with geography, the most frequently observed ones are earthquake, flood, erosion, fire and volcanic eruptions. According to the studies, there are approximately 45,000 deaths caused by natural disasters every year (EM-DAT, 2022; Our World in Data, 2022). The most fatal disaster events in the past were floods and droughts. Today, the number of lives lost and the amount of property damage brought on by natural disasters have significantly decreased thanks to rising public awareness of these events and technological developments.

One of the major disasters for which precautions must be taken is dam flooding, which has recently occurred in several locations and still does so sometimes while causing considerable loss of life and economic assets. Most floods in dams are based on by the soil structure sliding into the filling dams from the dam reservoir. Various geodetic and remote sensing-based studies have been carried out in order to observe these movements in reservoirs. 

## Problem Definition and Motivation

In this project, we attempt to monitor landslides around the reservoir of ‘Alkumru Dam’ located in Taşbalta, Siirt (in the Southeastern Anatolia) using interferometric synthetic aperture radar (InSAR) technique with Sentinel-1 synthetic aperture radar (SAR) data. Sentinel-1 data acquired in ascending and descending orbits were processed with the Sentinel Application Platform (SNAP) open source software tool (Snap, 2022). 

In the project, it is aimed to prepare a model that can predict future landslides by processing the recent changes in terrain level in the study area. With this model, it is aimed to monitor the potential landslide movements in advance and to ensure that the necessary precautions are taken based on the data of the past.

## Goals and Objectives

The main goal of this project is to develop a method to monitor landslide movements based on SAR data. Using this method, it may be possible to develop landslide monitoring models for potential future events by looking at past and current data on slope movement.

Based on this objective, the project stages will involve: 

●	Obtaining data and software from the open platforms 
●	Verifying data quality and usability for project purposes 
●	Pre-processing the data as a first for data integration  
●	Time series data analysis for detecting the deformations 
●	Prediction of the future slope movements based on past observations 
●	Development of a web-based platform for data sharing and presentation

## Methodology

First of all, Alkumru dam, which is our study area, was determined and analyzed. The dam is suitable for landslide monitoring assessment since landslide movements occur occasionally. In order to solve this problem, we will analyze the landslides that can occur by making temporal estimation using a machine learning method. This project we plan to reach our goal with a high temporal interval. A group member was assigned to each work package by creating a workflow chart (Gantt) for the management of this project. Thanks to the project flow chart, we can follow the work we need to do on a weekly basis. By listing our literature review, we have provided an easy-to-understand, focused and concise summary of previous work related to our project topic.

![image](https://github.com/hbarisdmr7/Landslide-Deformation/assets/38729621/f02401ab-6077-4192-8379-f3956493f895)


Obtaining information about the analysis is possible with Sentinel-1 Synthetic Aperture Radar Interferometry (InSAR) data sets, which provide multi-time surface change information in terms of deformation, and their processing techniques.

To achieve this, deformation extraction from Sentinel-1 time series datasets will be performed using the Small-Baseline Subsets (SBAS) method (Tavus et al., 2022) using the Looking into Continents from Space with Synthetic Aperture Radar (LiCSAR) products (Tavus et al., 2022).

# DESIGN 

The three stages of realizing our problem are: find the deformation itself, make a prediction about the future, presenting it correctly to the user.
Can the user download the data within the framework of the plan arranged before starting the design? Can the user download data according to the given instruction? or how much can be done by giving instructions to the user? It is necessary to answer some important questions such as: Within the framework of these discussed questions, two different system design ideas were considered.
It is designed with the idea that it is carried out by a company that performs deformation measurements analysis using SAR data and  used in line with the needs of various institutions.
As a service-oriented company, we perform processes using SAR data of the desired region with the LiCSBAS application in the Linux operating system, produce deformation maps in this process, produce and map the prediction of the deformation in the near future with the machine learning from these maps, compare and report our analysis by superimposing it on the DEM map with the deformation prediction map. We present our report together with our map data.

![image](https://github.com/hbarisdmr7/Landslide-Deformation/assets/38729621/67c93a2e-8f21-4d65-b40c-62512abb4039)


# Implementation
The Sentinel-1 satellite provides abundant and useful Synthetic Aperture Radar (SAR) data with the potential to reveal global earth surface deformation at high spatial and temporal resolutions. However, it is difficult for most users to take full advantage of the large amount of correlated data, especially in large areas. To overcome this challenge, we used LiCSBAS, an open-source SAR interferometry (InSAR) time series analysis package integrated with the automated Sentinel-1 InSAR processor (LiCSAR). LiCSBAS uses LiCSAR products that are freely available. In this way, we saved processing time and disk space while getting the results of InSAR time series analysis. In the LiCSBAS processing scheme, interferograms with many tripping errors were automatically completed with loop closure. We got reliable time series and velocities. To achieve this, deformation extraction from Sentinel-1 time series datasets are performed using the Small-Baseline Subsets (SBAS) method using the with Synthetic Aperture Radar (LiCSAR) products. The LiCSBAS and LiCSAR products have made it easy for us to make more use of the globally available and abundant SAR datasets. The LiCSBAS tutorial we use is in the appendices[3]. At the end of the tutorial, we got an hdf5 file named cum.h5 that contains cum and dates information.

Additionally, the LiCSBAS method allows us to produce a deformation map. This map has been converted to GeoTIFF format, which enhances its usability in applications like QGIS and Google Earth. The user can then see a clearer expression of the deformation zone. By adding a legend to this map, it is possible to show how much the soil has slipped or accumulated.

## 2D Deformation Map
![image](https://github.com/hbarisdmr7/Landslide-Deformation/assets/38729621/cdfc465d-2fc3-47a1-961a-e44c416559fc)

## 3D Deformation Map
![image](https://github.com/hbarisdmr7/Landslide-Deformation/assets/38729621/ae118cca-757a-4d56-a24b-e1bd1cc556e2)


We performed the time series analysis of these data with the methods we mentioned earlier. The results of the time series analysis were used to predict future deformation using machine learning. We used a machine learning method to predict future deformations. We used LSTM (Long Short Term Memory). LSTM networks are well suited for classifying, processing and making predictions based on time series data, as there may be delays of unknown duration between significant events in a time series. We loaded the dates and cum files in the cum.h5 file into our pyhton code. There were some "nan" values in these files. We wrote a code to fill these values with the mean of neighboring values. Now our data was completely ready to use.

To do LSTM we then created the training and testing data. There are 198 interferograms between 16/01/2019 and 13/01/2023. We used the time series we created from these interferograms. We then converted these interferograms to GeoTIFFs. We used 158 of the interferograms that we converted to GeoTIFFs to train the model. Thanks to the lookback function in the LSTM model, we have made it possible to predict the next data according to the previous data. The parameter of this function was important to us. For example, when we give 1, he expects him to guess the remaining 40 files, but he made 39 guesses because he tried to predict the next review using the previous review. We then saved the forecast data as GeoTIFFs. However, in order to make more accurate predictions, we decided to give the lookback function a value of 8 in the last case. Therefore, there are an estimated 32 GeoTIFFs. Although the number of predictions decreased, we found it appropriate because the accuracy increased.

Batch size and epoch parameters are other factors that affect prediction accuracy. As the period increases, the loss parameter decreases, but the execution time of the code increases. The "loss" parameter is the calculation of the error difference between the values obtained after each training and the actual values.
Batch size is the packet size of the data added to the training. The larger the batch size, the more accurate the gradient value calculation.

# Tests
We used 4-year data to estimate the deformation of the region. We said that there are a total of 198 interferograms in these four years of data. We used 158 of them to train the LSTM model. The remaining 40 data were entered into the model as test data. What we wanted from the model was to learn 8 test data and ask it to produce a prediction data. In this way, we had 32 predictions as it produced 1 prediction in every 8 test data, respectively. This number will vary according to the value we give to the lookback function. We said that we are saving GeoTIFFs from the "cum.h5" file. Now we have saved our predictions as GeoTIFF. Thus, we would be able to examine the difference between the two data. 

# Web Based Presentation
As we mentioned in the proposed solution section, we designed a website where we can get information from the user and publish our projects. It was a good system to simply reach us and see the projects.You can access the general view of our website from the appendices section [7].First of all, we have our homepage on this site. Here you can get general information about us and what we do. In the communication tab, we have a communication button as we mentioned before. On the Projects page, we display the project we produced on an interactive map. For this part, geoserver, which implements web map services (wms) standards, is used.

# CONCLUSION
In this study, we analyzed the landslide activities in the Alkumru dam lake in the Southeastern Anatolia Region of Turkey, using Sentinel-1 datasets, and analyzed the increasing and decreasing LiCSAR products available to the public on the COMET-LICS website. We worked on 4-year data between 16/01/2019 and 13/01/2023. For the deformation analysis, we used the SBAS method in the LiCSBAS application. We got the time series. We then used the LSTM method to predict the future from our data. We compared the estimated geoTIFFs we obtained with the available data. We examined the difference between them. The reason we chose this methodology is to obtain the deformations with centimeter precision.

We have obtained the deformation map of the 4-year change. We examined this map in both 2D and 3D. According to the results we obtained from LSTM, we observed that there was not much change. We have obtained acceptable estimation results.

The aim of the study is to demonstrate the feasibility and usability of the datasets and technique for high temporal scale and high spatial resolution landslide assessment and monitoring activities which are crucial for the maintenance of dams.

![image](https://github.com/hbarisdmr7/Landslide-Deformation/assets/38729621/6f35dcaa-6ea7-4307-b025-a8b3fa43cf6d)

![image](https://github.com/hbarisdmr7/Landslide-Deformation/assets/38729621/23e216b0-dbe3-41a3-bb4d-28fa1fa1871b)

![image](https://github.com/hbarisdmr7/Landslide-Deformation/assets/38729621/292f2c08-6d47-42a5-80d0-05a40755eea6)


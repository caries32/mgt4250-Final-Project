# mgt4250 Final Project
## Section 1 - Project Description

- ### Visualization Link
[Link to Tableau Public Visualization](https://public.tableau.com/shared/Q47Z8CCSW?:display_count=n&:origin=viz_share_link)
This repo is for the class project of MGT4250 Fall 2023 at Elon University.


- ### Questions of interest
  - (1.) What percentage of vehicles in the State of Washington are electric?
  - (2.) How has the number of electric vehicles in the State of Washington changed over
time?

- ### Importance

These questions are important because electric vehicles have been known to be better
for the environment for some time now. All forms of electric vehicles (EVs) can help
improve fuel economy, lower fuel costs, and reduce emissions. 

- ### References:
[The U.S. Department of Energy](https://afdc.energy.gov/fuels/electricity_benefits.html#:~:text=Electric%20and%20hybrid)


[M.I.T. Climate Portal](https://climate.mit.edu/ask-mit/are-electric-vehicles-definitely-better-climate-gas-powered-cars)

## Section 2
- ## Instructions
My data can be downloaded by following these steps 
1. click [here](https://github.com/caries32/mgt4250test)
2. Under the first box, where it says "caries32 Added files via upload" click on the file "washington_state_evs.csv" (Pictured)
   <img width="1431" alt="Screenshot 2023-12-06 at 5 14 59 AM" src="https://github.com/caries32/mgt4250-Final-Project/assets/133187234/2d819dbd-479f-4b45-9434-5a71f546a65c">
3. Click the download button to download the data
   <img width="1434" alt="Screenshot 2023-12-06 at 5 17 10 AM" src="https://github.com/caries32/mgt4250-Final-Project/assets/133187234/a0a50bde-34ec-41a2-be2b-6401a5e2ebe3">
*Note: This data is a subset of data found [here](https://catalog.data.gov/dataset/electric-vehicle-population-size-history-by-county) on Data.gov. It is pre-filtered to only include records with State as Washington (WA)*


- ## Data description
The columns in the dataset are as follows:


  - **Date** (object): The date of the data record.

  - **County** (object): The name of the county.

  - **State** (object): The state, in this case, only Washington (WA).

  - **Vehicle Primary Use** (object): The primary use of the vehicle, such as Passenger, Truck, etc.

  - **Battery Electric Vehicles (BEVs)** (int64): The number of battery electric vehicles.

  - **Plug-In Hybrid Electric Vehicles (PHEVs)** (int64): The number of plug-in hybrid electric vehicles.

  - **Electric Vehicle (EV) Total** (int64): The total number of electric vehicles, including both BEVs and PHEVs.

  - **Non-Electric Vehicle Total** (int64): The total number of non-electric vehicles.

  - **Total Vehicles** (int64): The total number of vehicles in the county, (EVs and gas/diesel).

  - **Percent Electric Vehicles** (float64): The total percentage of electric vehicles.


## Section 3
## Interpreting Visualizations
![image](https://github.com/caries32/mgt4250test/assets/133187234/0e6942a7-0d60-4eff-a09a-5653a4ff3b67)
Visualization 1 is a heatmap in Tableau that shows a breakdown of the percentage of EVs in Washington State broken down by county.

Visualization 1 helps us to better visualize how the percentage of EVs are spread across Washington which is related to question 1 (What percentage of vehicles in the State of Washington are electric?).

<img width="1436" alt="Screenshot 2023-12-06 at 4 17 17 AM" src="https://github.com/caries32/mgt4250test/assets/133187234/a8a49ce2-6a97-40fe-8867-13c64960b891">
Visualization 2 is a line plot from Streamlit that shows the total number of EVs in different Washington counties and has a select box for each county.

Visualization 2 helps us see how the number of EVs has changed over time for each county in the State of Washington which is related to question 2 (How has the number of electric vehicles in the State of Washington changed over time?).


![download-2](https://github.com/caries32/mgt4250test/assets/133187234/90479752-da24-4d73-a300-41c17a6919cd)


Visualization 3 is a bar graph from python that shows how the percentage of EVs in Washington has changed over time.

Visualization 3 helps see how the number of EVs has changed over time for the entire State of Washington which is also related to question 2.


## Section 4
- ## Discussion
I found this article, ["Electric Vehicles On The Rise In Washington State"](https://seattlemedium.com/electric-vehicles-on-the-rise-in-washington-state/), online that related to my questions. It talks about how the number of EVs in Washington has changed, how the number of new EVs sold in Washington has changed, the benefits of EVs for the environment, and the monetary incentives for buying an EV.

I asked these questions (two from the project and one further) to OpenAI's ChatGPT-4 model to determine its answers.
<img width="1118" alt="Screenshot 2023-12-06 at 5 00 18 AM" src="https://github.com/caries32/mgt4250-Final-Project/assets/133187234/bae476cf-5eab-4871-a5eb-716c8125381e">
<img width="833" alt="Screenshot 2023-12-06 at 5 01 25 AM" src="https://github.com/caries32/mgt4250-Final-Project/assets/133187234/af26305d-00ec-451b-a3e7-6029aa4324e7">
<img width="824" alt="Screenshot 2023-12-06 at 5 02 36 AM" src="https://github.com/caries32/mgt4250-Final-Project/assets/133187234/82c85e30-dc6d-4df7-94fd-a51c774d92f7">



- ## Summary
  I believe that my visualizations align greatly with both the article, as well as ChatGPT's response. ChatGPT stated that about 1.9% of vehicles in Washington are electric, which is similar to what visualization 3 shows. The article didn't break down the change, or new EV sales by county, but it did state that EVs are "on the rise", which is also the case with most of the counties in Visualization 2. Overall, I think the article supports my project in showing that the number of EVs in the State of Washington is growing, and I believe that ChatGPT's responses support my project by showing the total amount of EVs in Washington State in 2023 is approximately 1.9%


![image](https://github.com/caries32/mgt4250test/assets/133187234/6cf743a3-f9a7-43f3-b3dc-5ac61f1c241f)

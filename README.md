# capstone final project
This repository contains mainly my capstone final project. This project has been very challenging but also very complete in order to get full visibility of real projects. 

Here is the link to inspect the final version: 

REPO content: 
- API: 
  -api.py
  -app.yaml
  -requirements.txt
- Frontend: 
  -main.py
  -app.yaml
  -authent.yaml
  -requirements.txt
- KPIs

API Applications
These REST API were built using Flask-RestX for a web application and is used to visualize different KPIs for the H&M data, divided into 3 different datasets: 
- Articles
- Transactions
- Customers

<img width="1484" alt="Captura de pantalla 2023-03-30 a las 17 54 31" src="https://user-images.githubusercontent.com/114749480/228894252-66036d82-89c4-4caa-8d90-bd110879dbc2.png">

<img width="1485" alt="Captura de pantalla 2023-03-30 a las 17 54 40" src="https://user-images.githubusercontent.com/114749480/228894274-a7f558f0-b0df-4548-9527-e7aca47d56d3.png">

Streamlit application: 
Moreover, the streamlit application deployed on App Engine (Google Cloud) has first of all a login feature in order to protect the data. 

The username and Password depends on the person and is hashed in the code in order to keep it private and secure. (Find it in your email). 
<img width="783" alt="Captura de pantalla 2023-03-30 a las 17 57 10" src="https://user-images.githubusercontent.com/114749480/228896856-0dec737f-99b2-4b95-85a3-2717c30d7825.png">

Once you log into this feature you get the H&M KPI's visualized. 

First you will get an analysis of the Transactions Database. 

<img width="727" alt="Captura de pantalla 2023-03-30 a las 18 03 53" src="https://user-images.githubusercontent.com/114749480/228896886-5f8ac5b0-5008-4985-9b19-518ae74dbea4.png">

Then it will follow the Customers Database 

<img width="725" alt="Captura de pantalla 2023-03-30 a las 18 04 09" src="https://user-images.githubusercontent.com/114749480/228896979-81065825-f47c-43d4-89ab-29310ef142d0.png">

and will end with the articles Database. 
<img width="739" alt="Captura de pantalla 2023-03-30 a las 18 04 22" src="https://user-images.githubusercontent.com/114749480/228897011-8eb6f039-3782-4d16-9c72-3d9550fd2408.png">

On the left hand side you can find the filters created and choose from them. 

<img width="318" alt="Captura de pantalla 2023-03-30 a las 18 04 35" src="https://user-images.githubusercontent.com/114749480/228897027-3827c360-7142-492c-a9cd-d5d0b972487f.png">


Finally once you are done, you can log out with the buttom "Logout".
<img width="188" alt="Captura de pantalla 2023-03-30 a las 18 04 43" src="https://user-images.githubusercontent.com/114749480/228897062-a4ebd9d2-9bb1-4f38-9fb2-9e717f1289a1.png">



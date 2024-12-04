# The Keratin Chronicle by RESTful Rhinos

# Roster:
**Brian Liu**: Project Manager, Backend + Flask, Implement Calendarific API

**Victor Casado**: Backend + Databases, Implement Financial Modeling Prep API

**Danny Mok**: Database Engineer, Implement NYT API

**Marco Quintero**: Frontend (HTML + CSS + Tailwind), Implement Open Weather Map API

# Project Description:
This website aims to provide personalized and real time information to the user–like a daily feed or landing page. Registered users can input their preferences for location and interests, which is then used to showcase personalized stock information, weather, and news to the user. From the homepage, the user can then go to separate pages that contain more detailed information about the articles, stocks, or weather. The user will have access to their profile, where they can change their preferences. 

# Install Guide:

**Cloning the Project**
1. In terminal, clone the repository to your local machine:

        git clone git@github.com:Victor-Casado/Bug_Busters__victorc353_ethans175_marcoq4_qianjunz.git


**Installing Dependencies**
1. Navigate to [Python Download Page](https://www.python.org/downloads/) and install python3 on your machine
2. Create a virtual environment by running
 
        python3 -m venv foo

3. Activate the virtual environment by running

        . foo/bin/activate


3. In your terminal, run the command

        pip install -r RESTful_Rhinos__brianl237_dannym2789_marcoq4_victorc353/requirements.txt

**Getting API Keys**

1. Financial Modeling Prep API Key
   1. Navigate to the [homepage](https://site.financialmodelingprep.com/)
   2. Click sign up
   3. Follow the instructions to sign up
   4. Navigate to the [user dashboard](https://site.financialmodelingprep.com/developer/docs/dashboard)
   5. Copy the Key
   6. Paste it into the [key_FMP.txt](keys/key_FMP.txt) file in the keys directory
2. Calendarific
3. NYT
4. Open Weather
5. Geocoding


# Launch Codes
1. Activate the virtual environment from the install guide if not activated already
2. Change directory into the app folder

        cd RESTful_Rhinos__brianl237_dannym2789_marcoq4_victorc353/app


3. Run the App:

        $ python3 __init__.py

4. Open the app in a browser by navigating to <a href="http://127.0.0.1:5001">127.0.0.1:5001</a>

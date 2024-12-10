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
   6. Paste it into the [key_FMP.txt](keys/key_FMP.txt) file in the [keys](keys/) directory
2. Calendarific
   1. Navigate to [homepage](https://calendarific.com/)
   2. Signup or login with email or GitHub account.
   3. Head to your [account dashboard](https://calendarific.com/account/dashboard) where your key will be generated.
   4. Copy the key
   5. Paste it into the [key_Calendarific.txt](keys/key_Calendarific.txt) file in the [keys](keys/) directory
4. NYT
   1. Navigate to [homepage](https://developer.nytimes.com/)
   2. Click on Sign In, located in the top right corner. If you already have an account, put in your credentials. Otherwise, make a new account.
   3. Click on your username in the top right corner. In the dropdown that opens, click on Apps. Alternatively, refer to this [link](https://developer.nytimes.com/my-apps)
   4. Press new apps
   5. Make an app name and description. Enable the Archive API, Article Search API, and Most Popular API.
   6. Save your API.
   7. Access your app again and copy the API key.
   8. Paste it into the [key_NYT.txt](keys/key_NYT.txt) file in the [keys](keys/) directory
6. Open Weather
   1. Open the [Pricing Page](https://openweathermap.org/price) on Open Weather Map's official website
   2. Scroll down to the section titled "Current weather and forecasts collection" and click "Get API Key" under the "Free" column
   3. Sign up by creating a username and password using a valid email. Email verification is required.
   4. Once in the website's home page, click the section titled "API Keys" in the lower level navbar.
   5. The key should have already been generated but if not, cick "Generate" and the key will appear shortly.
   6. Paste it into the [key_Open_Weather_Map.txt](keys/key_Open_Weather_Map.txt) file in the [keys](keys/) directory



# Launch Codes
1. Activate the virtual environment from the install guide if not activated already
2. Change directory into the app folder

        cd RESTful_Rhinos__brianl237_dannym2789_marcoq4_victorc353/app


3. Run the App:

        $ python3 __init__.py

4. Open the app in a browser by navigating to <a href="http://127.0.0.1:5001">127.0.0.1:5001</a>

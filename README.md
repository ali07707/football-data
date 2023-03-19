This code is a Flask web application that retrieves football player statistics from an API and displays them on a webpage with the player's photo and a plot of their statistics. The application uses the RapidAPI football beta API to retrieve player data and the mplsoccer library to create the plot.

Requirements. 

The following libraries are required to run the application:  

requests  
Flask  
mplsoccer  
matplotlib  

In addition, an API key is required to access the RapidAPI football beta API. The API key should be stored in a file named config.py with the variable name API_KEY.

Running the application

To run the application, navigate to the project directory and run the following command in a terminal:

Copy code. 
python app.py. 
This will start the Flask development server on port 5002. The application can be accessed by navigating to http://localhost:5002 in a web browser.

Usage. 

To use the application, enter the name of a football player in the search box on the homepage and click the "Search" button. The application will retrieve the player's statistics from the API and display them on a result page along with the player's photo and a plot of their statistics.

If the player is not found in the API, the application will display an error page with a message indicating that the player was not found.

# The Seafood Pantry

Welcome to the Seafood Pantry!

Here one can use a chatbot that uses Seafood Watch data to get more information on seafood to eat.
Seafood Watch is a rating program for environmentally responsible seafood choices and developed from the Monterey Bay Aquarium in California.
This chatbot can help to identify which seafood type is most sustainable to eat at which location and recommend seafood as "Best Choice", "Good Alternative", "Certified" and "Avoid". 

Prompts that have been tested before using a set of interaction rules are:

- What if im allergic to shellfish?
- Are farmed fish always less sustainable?
- What are the fish with less bones?
- Isn't eel a type of seafood?
- What are the best type of seafood for sushi?
- What do you recommend if I'm vegan? 

Using Gemini Pro 1.5 002, we use code to make a chatbot with a .csv file and the original code can be found [here](https://milumon.medium.com/creating-custom-chatbots-using-csv-data-with-python-and-openai-api-0486d8992b24).
The data itself was scraped from the Seafood Watch website using Selenium.


Download the .csv file and create a key for your account to use Gemini. Then run the code and ask your questions. The code also plots a chart showing the different types of seafood, their locations and the recommendations, as well as an interactive map with these species, recommendations and exact locations.

You may also download the .html file in the Github repository.

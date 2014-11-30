from linkedin import linkedin

# Define CONSUMER_KEY, CONSUMER_SECRET,  
# USER_TOKEN, and USER_SECRET from the credentials 
# provided in your LinkedIn application

# Instantiate the developer authentication class

CONSUMER_KEY = "osfyhjfdnwq2"
CONSUMER_SECRET = "z8WoRryNsdb8D4oh"
USER_TOKEN = "400f4d91-67dc-4854-b9c7-0b351aecf47e"
USER_SECRET = "5cfb7cb8-256b-43b9-b1b1-c976476cfc66"
RETURN_URL = "http://localhost:8000"

authentication = linkedin.LinkedInDeveloperAuthentication(CONSUMER_KEY, CONSUMER_SECRET, 
        USER_TOKEN, USER_SECRET, 
        RETURN_URL, linkedin.PERMISSIONS.enums.values())

# Pass it in to the app...

application = linkedin.LinkedInApplication(authentication)

# Use the app....

application.get_profile()

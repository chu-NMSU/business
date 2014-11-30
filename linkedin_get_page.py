from linkedin import linkedin
import json

# Define CONSUMER_KEY, CONSUMER_SECRET,  
# USER_TOKEN, and USER_SECRET from the credentials 
# provided in your LinkedIn application

# Instantiate the developer authentication class

CONSUMER_KEY = "osfyhjfdnwq2"
CONSUMER_SECRET = "z8WoRryNsdb8D4oh"
USER_TOKEN = "1ac80d83-a372-4292-b638-540a9b66f5ce"
USER_SECRET = "df56d772-a230-4e18-babf-1d567bdcbb8b"
RETURN_URL = "http://localhost:8000"

authentication = linkedin.LinkedInDeveloperAuthentication(CONSUMER_KEY, CONSUMER_SECRET, 
        USER_TOKEN, USER_SECRET, 
        RETURN_URL, linkedin.PERMISSIONS.enums.values())

# Pass it in to the app...

application = linkedin.LinkedInApplication(authentication)

# Use the app....

# print application.get_profile()
with open("connnections.json", "w") as outfile:
    outfile.write(json.dumps(application.get_connections(), indent=1))

with open("memberships.json", "w") as outfile:
    outfile.write(json.dumps(application.get_memberships(), indent=1))

with open("companies.json", "w") as outfile:
    # universal company name is gotten from linkedin page url
    outfile.write(json.dumps(application.get_companies(universal_names=["echo-global-logistics"]), indent=1))

with open("companies_updates.json", "w") as outfile:
    company_json = application.get_companies(universal_names=["echo-global-logistics"])
    company_id = company_json["values"][0]["id"]
    company_update_json = application.get_company_updates(company_id)
    outfile.write(json.dumps(company_update_json, indent=1))


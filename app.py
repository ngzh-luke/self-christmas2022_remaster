""" The application is developed by Kittipich "Luke" Aiumbhornsin
Created on May 11, 2023
Run file of the application """

from christmas_app import systemInfo, create_app
from decouple import config as en_var  # import the environment var
# import pytz

print("SystemInfo -> ", systemInfo)
# print("Environment Variable: "+ en_var('christmas_app2022'))

# print(pytz.all_timezones) # List out all the timezone available
if __name__ == '__main__':
    app = create_app()
    # app.run(port=int(en_var("PORT", 8080)),
    #         debug=en_var("DEBUG", False))  # , host='0.0.0.0',

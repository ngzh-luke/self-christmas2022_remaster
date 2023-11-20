""" The application is developed by Kittipich "Luke" Aiumbhornsin
Created on May 11, 2023
Run Dev file of the application """

from christmas_app import systemInfo, create_app
from decouple import config as en_var  # import the environment var
from time import localtime
# import pytz

print(f"SystemInfo -> ", systemInfo, "@", {localtime()})

# print(pytz.all_timezones) # List out all the timezone available
""" for running in dev """
if __name__ == '__main__':
    app = create_app()
    app.run(port=int(en_var("PORT", 8080)),
            debug=en_var("DEBUG", False))  # , host='0.0.0.0',

import os
import pandas as pd

# Use this states for full scrape:
# states = [ 'AL', 'AK', 'AS', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FM', 'FL', 'GA', 'GU', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MH', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'MP', 'OH', 'OK', 'OR', 'PW', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VI', 'VA', 'WA', 'WV', 'WI', 'WY' ]

# use this states for demo:
states = ['CT', 'DE']
for state in states:
    directory = os.fsencode(f"./data/{state}")

    my_data = {
        "Station": [],
        "Date": [],
        "Latitude": [],
        "Longitude": [],
        "Elevation": [],
        "Name": [],
        "DailyAverageDryBulbTemperature": [],
        "DailyAverageWetBulbTemperature": [],
        "DailyAverageRelativeHumidity": [],
        "DailyAverageWindSpeed": [],
        "DailyCollingDegreeDays": [],
        "DailyDepartureFromNormalAverageTemperature": [],
        "DailyHeatingDegreeDays": [],
        "DailyPrecipitation": [],
        "DailySnowfall": [],
        "MonthlyMeanTemperature": [],
        "NormalsCoolingDegreeDay": [],
        "NormalsHeatingDegreeDay": []
    }
    counter = 1
    for file in os.listdir(directory):
        print(counter)
        counter += 1
        try:
            filename = os.fsdecode(file)
            print(f"going through file: {filename}")
            df = pd.read_csv(f"./data/{state}/{filename}")
            # the following df slice filters out weather stations that are not relevant to the state in question
            correct_state = df[df['NAME'].astype(str).str.contains(f"{state} US")]
            if len(correct_state) > 0:
                my_data["Station"] = my_data["Station"] + list(correct_state["STATION"])
                my_data["Date"] = my_data["Date"] + list(correct_state["DATE"])
                my_data["Latitude"] = my_data["Latitude"] + list(correct_state["LATITUDE"])
                my_data["Longitude"] = my_data["Longitude"] + list(correct_state["LONGITUDE"])
                my_data["Elevation"] = my_data["Elevation"] + list(correct_state["ELEVATION"])
                my_data["Name"] = my_data["Name"] + list(correct_state["NAME"])
                my_data["DailyAverageDryBulbTemperature"] = my_data["DailyAverageDryBulbTemperature"] + list(correct_state["DailyAverageDryBulbTemperature"])
                my_data["DailyAverageWetBulbTemperature"] = my_data["DailyAverageWetBulbTemperature"] + list(correct_state["DailyAverageWetBulbTemperature"])
                my_data["DailyAverageRelativeHumidity"] = my_data["DailyAverageRelativeHumidity"] + list(correct_state["DailyAverageRelativeHumidity"])
                my_data["DailyAverageWindSpeed"] = my_data["DailyAverageWindSpeed"] + list(correct_state["DailyAverageWindSpeed"])
                my_data["DailyCollingDegreeDays"] = my_data["DailyCollingDegreeDays"] + list(correct_state["DailyCollingDegreeDays"])
                my_data["DailyDepartureFromNormalAverageTemperature"] = my_data["DailyDepartureFromNormalAverageTemperature"] + list(correct_state["DailyDepartureFromNormalAverageTemperature"])
                my_data["DailyHeatingDegreeDays"] = my_data["DailyHeatingDegreeDays"] + list(correct_state["DailyHeatingDegreeDays"])
                my_data["DailyPrecipitation"] = my_data["DailyPrecipitation"] + list(correct_state["DailyPrecipitation"])
                my_data["DailySnowfall"] = my_data["DailySnowfall"] + list(correct_state["DailySnowfall"])
                my_data["MonthlyMeanTemperature"] = my_data["MonthlyMeanTemperature"] + list(correct_state["MonthlyMeanTemperature"])
                my_data["NormalsCoolingDegreeDay"] = my_data["NormalsCoolingDegreeDay"] + list(correct_state["NormalsCoolingDegreeDay"])
                my_data["NormalsHeatingDegreeDay"] = my_data["NormalsHeatingDegreeDay"] + list(correct_state["NormalsHeatingDegreeDay"])
            else:
                print(f"found data not belonging to {state}, moving onto next file")
                pass
        except:
            pass

    print("csv read complete... starting the csv conversion")
    result_df = pd.DataFrame.from_dict(my_data, orient='index')
    print("dataset oreintation complete")
    result_df = result_df.transpose()
    print("dataset transpose complete")
    resulting_csv_data = result_df.to_csv(f"{state}.csv", index=False)
    print(f"{state} file finished")
print('job finished')

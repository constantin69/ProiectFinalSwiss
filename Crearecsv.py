import csv
import pandas as pd
import plotly.express as px

from Api import location, numar

location = location
numar = numar

def creare_csv(my_list, location):
    with open(f"{location}.csv", 'w', newline='', errors="ignore") as csvfile:
        fieldnames = my_list[0].keys()
        writer = csv.writer(csvfile)
        writer.writerow(fieldnames)

        for i in my_list:
            i["hour"] = int(i["hour"][:2])
            writer.writerow(
                [i["date"], i["hour"], i["an"], i["luna"], i["day"], i["temp_c"], i["condition"], i["wind_mph"],
                 i["wind_dir"], i["pressure_mb"], i["precip_mm"], i["humidity"], i["uv"]])


def afisare_grafic(location):
    pd.options.plotting.backend = "plotly"
    df = pd.read_csv(f"{location}.csv")
    date = df["date"]

    if numar == 1:
        day = df["day"]
        x1 = df["hour"][:24]
        y1 = df["temp_c"][:24]
        barchat = px.bar(df, x=x1, y=y1, title=f"Evolutia temperaturii", range_y=[0, 25])
        # barchat = px.bar(df, x=x1, y=y1, color="hour", facet_row="hour", facet_col_wrap=2,
        #                  title=f"Evolutia temperaturii", hover_name="temp_c", hover_data=['hour'],
        #                  custom_data=['date'], text='temp_c', labels={"date":f" Data", "gender":"Gender"},
        #                  template="gridon", animation_frame='temp_c', range_y=[-20,30])
        barchat.show()
        barchat.write_image(f"{day}.png")

    if numar == 2:
        day = df["day"]
        x2 = df["hour"][25:48]
        y2 = df["temp_c"][25:48]
        barchat = px.bar(df, x=x2, y=y2, title=f"Evolutia temperaturii", range_y=[0, 25])
        # barchat = px.bar(df, x=x2, y=y2, title=f"Evolutia temperaturii")
        barchat.show()
        barchat.write_image(f"{day+1}.png")

    if numar == 3:
        day = df["day"]
        x3 = df["hour"][24:]
        y3 = df["temp_c"][24:]
        barchat = px.bar(df, x=x3, y=y3, title=f"Evolutia temperaturii", range_y=[0, 25])
        barchat.show()
        barchat.write_image(f"{day+2}.png")



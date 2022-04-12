import csv
from Api import location

location = location


def creare_csv(my_list, location):
    with open(f"{location}.csv", 'w', newline='', errors="ignore") as csvfile:
        fieldnames = my_list[0].keys()
        writer = csv.writer(csvfile)
        writer.writerow(fieldnames)

        for i in my_list:
            writer.writerow(
                [i["date"], i["hour"], i["temp_c"], i["condition"], i["wind_mph"], i["wind_dir"], i["pressure_mb"],
                 i["precip_mm"],
                 i["humidity"], i["uv"]])


def afisare_grafic(file, location):
    pass



from Location import Alert
from Api import response

res = response
alerts = res["alerts"]["alert"]
alerte = len(alerts)
my_list = list()


def info_alerts():
    for nr in range(alerte):
        my_dict = dict()

        my_dict["headline"] = alerts[nr]["headline"]
        my_dict["severity"] = alerts[nr]["severity"]
        my_dict["urgency"] = alerts[nr]["urgency"]
        my_dict["areas"] = alerts[nr]["areas"]
        my_dict["event"] = alerts[nr]["event"]
        my_dict["effective"] = alerts[nr]["effective"]
        my_dict["expires"] = alerts[nr]["expires"]
        my_dict["desc"] = alerts[nr]["desc"]

        my_list.append(my_dict)

    return my_list


my_list = info_alerts()


def afisare_alerts(my_list):
    my_l = list()
    limit = len(my_list)
    if limit == 0:
        print("Nu sunt alerte")
        return

    for alerta in my_list:
        my_dict = dict()
        my_dict["headline"] = alerta["headline"]
        my_dict["severity"] = alerta["severity"]
        my_dict["urgency"] = alerta["urgency"]
        my_dict["areas"] = alerta["areas"]
        my_dict["event"] = alerta["event"]
        my_dict["effective"] = alerta["effective"]
        my_dict["expires"] = alerta["expires"]
        my_dict["desc"] = alerta["desc"]

        alert = Alert(my_dict["headline"], my_dict["severity"], my_dict["urgency"], my_dict["areas"], my_dict["event"],
                      my_dict["effective"], my_dict["expires"], my_dict["desc"])
        alert.afisare_info_alerts()




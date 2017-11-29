#helper file for rendering comics

import sqlite3

f = "data/funnies.db"
db = sqlite3.connect(f)
c = db.cursor()

def add_entry(title, name, sillyurl1, sillyurl2, sillyurl3, sillyurl4, sillyphrase1, sillyphrase2, sillyphrase3, sillyphrase4):
    command = "INSERT INTO funnies VALUES ('" + title + "','" + name + "','" + sillyurl1 + "','" + sillyurl2 + "','" + sillyurl3 + "','" + sillyurl4 + "','" + sillyphrase1 + "','" + sillyphrase2 + "','" + sillyphrase3 + "','" + sillyphrase4 + "')"
    c.execute(command)


def get_dict():
    q = "SELECT * from funnies"
    foo = c.execute(q)
    dict_stuff = {}
    for bar in foo:
        title = bar[0]
        name = bar[1]
        sillyurl1 = bar[2]
        sillyurl2 = bar[3]
        sillyurl3 = bar[4]
        sillyurl4 = bar[5]
        sillyphrase1 = bar[6]
        sillyphrase2 = bar[7]
        sillyphrase3 = bar[8]
        sillyphrase4 = bar[9]
        dict_stuff[title] = {}
        dict_stuff[title]['name'] = name
        dict_stuff[title]['sillyurl1'] = sillyurl1
        dict_stuff[title]['sillyurl2'] = sillyurl2
        dict_stuff[title]['sillyurl3'] = sillyurl3
        dict_stuff[title]['sillyurl4'] = sillyurl4
        dict_stuff[title]['sillyphrase1'] = sillyphrase1
        dict_stuff[title]['sillyphrase2'] = sillyphrase2
        dict_stuff[title]['sillyphrase3'] = sillyphrase3
        dict_stuff[title]['sillyphrase4'] = sillyphrase4
    return dict_stuff

    
db.commit()
db.close()
    

import psycopg2
import numpy as np
from scipy import stats as st
import itertools

conn = psycopg2.connect(dbname='birds_db', user='ornithologist',
                        password='ornithologist',
                        host='localhost')
cursor = conn.cursor()

# Initialization

cursor.execute("select enum_range(NULL::bird_color)")
colors_enum = cursor.fetchone()[0].strip('{}').replace('"', '').split(',')
colors_hst = {k: 0 for k in colors_enum}

# Get colors histogram

body_lengths = []
wingspans = []
cursor.execute("SELECT * from birds")
for spec, name, color, body_length, wingspan in cursor.fetchall():
    colors_hst[str(color)] += 1
    body_lengths.append(body_length)
    wingspans.append(wingspan)
print(colors_hst)


# Insert colors histogram
cursor.execute("delete from bird_colors_info")
for n, f in colors_hst.items():
    cursor.execute("insert into bird_colors_info (color, count) values ('%s', %s)" % (n, f))

body_lengths = np.array(body_lengths, int)
wingspans = np.array(wingspans, int)

body_mode = [e.tolist() for e in [a for a in  list(st.mode(body_lengths))]]
wing_mode = [e.tolist() for e in [a for a in  list(st.mode(wingspans))]]
body_mode = list(itertools.chain.from_iterable(list(st.mode(body_lengths))))
wing_mode = list(itertools.chain.from_iterable(list(st.mode(wingspans))))

print(body_mode)
print(wing_mode)
body_median = np.median(body_lengths)
wing_median = np.median(wingspans)

body_mean = np.mean(body_lengths)
wing_mean = np.mean(wingspans)

cursor.execute("delete from birds_stat")
cursor.execute("insert into birds_stat (body_length_mean, body_length_median, body_length_mode, \
                wingspan_mean, wingspan_median, wingspan_mode) values (%s, %s, array %s, %s, %s, array %s)" % \
               (body_mean, body_median, body_mode, wing_mean, wing_median, wing_mode))

conn.commit()

conn.close()

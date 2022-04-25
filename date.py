from datetime import datetime

import delta as delta

date_1 = datetime(2022, 4, 25).date()
date_2 = datetime(2022, 4, 27).date()

delta = None
if date_1 > date_2:
    print("Date 1 is greater ")
    delta = date_1 - date_2

else:
    print("Date 2 is greater ")
    delta = date_2 - date_1
    print("Difference is ", delta.days, " Days")

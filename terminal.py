import  time

count = 0
bar = ""
for i in range(100):
    if count != 30:
        print('\r' , str(bar) ,end='')
        bar = bar + "_"
        time.sleep(0.1)
        count += 1
    else:
        count = 0
        bar = "_"

import math , shutil
width = shutil.get_terminal_size().columns
radius = 19
bar = "**"
for y in range(math.ceil(radius / 3)):
    print(bar.center(width))
    for x in range(6):
        bar = bar + "*"
    if y == math.ceil(radius / 3) - 1:
        for x in range(math.ceil(radius / 2)):
            bar = bar[:-6]
            print(bar.center(width))


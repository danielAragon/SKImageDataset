from pathlib import Path
for x in range(1001, 2001):
    string = 'limon/limon_%d.txt' % (x)
    Path(string).touch()

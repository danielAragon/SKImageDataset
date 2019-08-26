from pathlib import Path
for x in range(1001, 2001):
    string = 'aji_amarillo/aji_amarillo_%d.txt' % (x)
    Path(string).touch()

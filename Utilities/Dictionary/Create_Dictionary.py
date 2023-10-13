# Method 1: {}
art_galleries = {}

for name, area in gallery_info:
    art_galleries[name] = area

# Find the last 5 names
for name in sorted(art_galleries)[-5:]: # Loop over the key
    print(name)

# Method 2: dict()

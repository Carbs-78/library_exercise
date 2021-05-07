def cuboid_volume(l_1):
    return l_1 * l_1 * l_1


length = [2, 1.1, -2.5, 2, 5]

for i in range(len(length)):
    print("The volume of cuboid:", cuboid_volume(length[i]))

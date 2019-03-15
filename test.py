import os

for root, dirs, files in os.walk("./data/valid_data", topdown=False):
    for i, name in enumerate(files):
        # if len(name) != 9:
        #     print(name)
        srcf = os.path.join(root, name)
        name = name.replace('.jpg', '_num%d.jpg' % i)
        print(os.path.join(root, name))
        desf = os.path.join(root, 'dest', name)
        with open(srcf, 'rb') as r:
            with open(desf, 'wb') as w:
                w.write(r.read())
        # break
    # for name in dirs:
    #     print(os.path.join(root, name))

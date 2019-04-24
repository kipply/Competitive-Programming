import os
from glob import glob
print len(set([y.split(".")[1].split("/")[-1] for x in os.walk('.') for y in glob(os.path.join(x[0], '*.*'))]))
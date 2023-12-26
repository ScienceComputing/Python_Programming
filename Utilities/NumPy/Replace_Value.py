import numpy as np
array_1 = np.array(range(0, 30))
array_2 = np.where(array_1 % 2 == 0, 'even', 'odd')
array_2
# array(['even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even',
#        'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd',
#        'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even',
#        'odd', 'even', 'odd'], dtype='<U4')

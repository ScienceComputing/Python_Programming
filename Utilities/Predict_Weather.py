import numpy as np

# Create the transition matrix
P = np.matrix( '0.4, 0.3, 0.1; \
                0.4, 0.3, 0.6; \
                0.2, 0.4, 0.3' )

print(P)

# Use the vector x0 to express that today it is sunny
x0 = np.matrix( '1; \
                 0; \
                 0' )
print(x0)

# Predict the weather a week from today
x = x0
for i in range(8):      
    print('Day', i)  
    print(x)
    x = P * x  

# Predict the weather the next 30 days
x = x0
for i in range(31):      
    print('Day', i)  
    print(x)
    x = P * x  

# Predict the weather for a year from now
x = x0
for i in range(366):      
    print('Day', i)  
    print(x)
    x = P * x  

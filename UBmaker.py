import random

# Create a list to store the user base objects
user_bases = []

# Iterate over the number of user bases to create
for i in range(1, 301):
    
    # Determine the region for this user base
    region = (i - 1) // 50
    
    # Create a user base object with randomized properties
    user_base = '''<void method="add">
                     <object class="cloudsim.ext.gui.UserBaseUIElement">
                       <void property="color">
                         <object idref="Color0"/>
                       </void>
                       <void property="name">
                         <string>UB''' + str(i) + '''</string>
                       </void>
                       <void property="offPeakUserCount">
                         <int>100</int>
                       </void>
                       <void property="peakHoursEnd">
                         <int>''' + str(random.randint(9, 12)) + '''</int>
                       </void>
                       <void property="peakHoursStart">
                         <int>''' + str(random.randint(3, 6)) + '''</int>
                       </void>
                       <void property="peakUserCount">
                         <int>''' + str(random.randint(1, 4) * 500) + '''</int>
                       </void>
                       <void property="region">
                         <int>''' + str(region) + '''</int>
                       </void>
                       <void property="reqPerHrPerUser">
                         <int>60</int>
                       </void>
                       <void property="reqSize">
                         <long>100</long>
                       </void>
                     </object>
                   </void>'''
    
    # Add the user base object to the list
    user_bases.append(user_base)

# Write the user bases to a text file
with open('user_bases.txt', 'w') as f:
    for user_base in user_bases:
        f.write(user_base + '\n')

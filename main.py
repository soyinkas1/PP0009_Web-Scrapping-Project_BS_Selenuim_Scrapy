

import pandas as pd

states=['California','Sidcup','Bromley']
population = [12242424,2324124,123123]

dict_area = {'State':states,'Population':population}

df_area =pd.DataFrame.from_dict(dict_area)
#
# for state in states:
#     if state=='Sidcup':
#         print(state)


with open('test.txt','w') as file:
    file.write("This is necessary to prevent IndentationError")

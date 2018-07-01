import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import csv
#import matplotlib as plt
###################################  Controler 01 (Work experience and Technical knowledge) ###################################

# New Antecedent/Consequent objects hold universe variables and membership functions
work_experience = ctrl.Antecedent(np.arange(0, 11, 1), 'work_experience')
technical_Knowledge = ctrl.Antecedent(np.arange(0, 11, 1), 'technical_Knowledge')
experience = ctrl.Consequent(np.arange(0, 50, 1), 'experience')
# Auto-membership function population is possible with .automf(3, 5, or 7)
work_experience.automf(3)
technical_Knowledge.automf(3)
# Custom membership functions can be built interactively with a familiar, Pythonic API
experience['low'] = fuzz.trimf(experience.universe, [0, 0, 25])
experience['medium'] = fuzz.trimf(experience.universe, [0, 25, 50])
experience['high'] = fuzz.trimf(experience.universe, [25, 50, 50])
#define rules
rule1 = ctrl.Rule(work_experience['poor'] | technical_Knowledge['poor'], experience['low'])
rule2 = ctrl.Rule(technical_Knowledge['average'], experience['medium'])
rule3 = ctrl.Rule(technical_Knowledge['good'] | work_experience['good'], experience['high'])
#create the control system
experience_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
experiencing = ctrl.ControlSystemSimulation(experience_ctrl)
# Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
# Note: if you like passing many inputs all at once, use .inputs(dict_of_data)
we_array = []
tk_array = []
with open('FIS_Data.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        we_array.append(row[2])
        tk_array.append(row[3])

c1array = [len(we_array)]
for x in range(0,len(we_array)):
    experiencing.input['work_experience']=float(we_array[x])
    experiencing.input['technical_Knowledge']=float(tk_array[x])
    experiencing.compute()#Crunch the numbers
    c1array.append(experiencing.output['experience'])
    print(experiencing.output['experience'])

######################################  Controler 02 (Skils and Education Qualifications) ######################################
print()

# New Antecedent/Consequent objects hold universe variables and membership functions
skills = ctrl.Antecedent(np.arange(0, 11, 1), 'skills')
education_qualifications = ctrl.Antecedent(np.arange(0, 11, 1), 'education_qualifications')
experience = ctrl.Consequent(np.arange(0, 26, 1), 'experience')
# Auto-membership function population is possible with .automf(3, 5, or 7)
skills.automf(3)
education_qualifications.automf(3)
# Custom membership functions can be built interactively with a familiar, Pythonic API
experience['low'] = fuzz.trimf(experience.universe, [0, 0, 13])
experience['medium'] = fuzz.trimf(experience.universe, [0, 13, 26])
experience['high'] = fuzz.trimf(experience.universe, [13, 26, 26])
#define rules
rule1 = ctrl.Rule(skills['poor'] | education_qualifications['poor'], experience['low'])
rule2 = ctrl.Rule(education_qualifications['average'], experience['medium'])
rule3 = ctrl.Rule(education_qualifications['good'] | skills['good'], experience['high'])
#create the control system
experience_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
experiencing = ctrl.ControlSystemSimulation(experience_ctrl)
# Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
# Note: if you like passing many inputs all at once, use .inputs(dict_of_data)
sk_array = []
eq_array = []
with open('FIS_Data.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        sk_array.append(row[4])
        eq_array.append(row[5])

c2array = [len(sk_array)]
for x in range(0,len(sk_array)):
    experiencing.input['skills']=float(sk_array[x])
    experiencing.input['education_qualifications']=float(eq_array[x])
    experiencing.compute()#Crunch the numbers
    c2array.append(experiencing.output['experience'])
    print(experiencing.output['experience'])

######################################  Controler 03 (Language fluency and Competence) ######################################
print()

# New Antecedent/Consequent objects hold universe variables and membership functions
language_fluency = ctrl.Antecedent(np.arange(0, 11, 1), 'language_fluency')
competence = ctrl.Antecedent(np.arange(0, 11, 1), 'competence')
experience = ctrl.Consequent(np.arange(0, 26, 1), 'experience')
# Auto-membership function population is possible with .automf(3, 5, or 7)
language_fluency.automf(3)
competence.automf(3)
# Custom membership functions can be built interactively with a familiar, Pythonic API
experience['low'] = fuzz.trimf(experience.universe, [0, 0, 13])
experience['medium'] = fuzz.trimf(experience.universe, [0, 13, 26])
experience['high'] = fuzz.trimf(experience.universe, [13, 26, 26])
#define rules
rule1 = ctrl.Rule(language_fluency['poor'] | competence['poor'], experience['low'])
rule2 = ctrl.Rule(competence['average'], experience['medium'])
rule3 = ctrl.Rule(competence['good'] | language_fluency['good'], experience['high'])
#create the control system
experience_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
experiencing = ctrl.ControlSystemSimulation(experience_ctrl)
# Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
# Note: if you like passing many inputs all at once, use .inputs(dict_of_data)
lf_array = []
co_array = []
with open('FIS_Data.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        lf_array.append(row[6])
        co_array.append(row[7])

c3array = [len(lf_array)]
for x in range(0,len(lf_array)):
    experiencing.input['language_fluency']=float(lf_array[x])
    experiencing.input['competence']=float(co_array[x])
    experiencing.compute()#Crunch the numbers
    c3array.append(experiencing.output['experience'])
    print(experiencing.output['experience'])



###################################  Controler 04 (Controller 02 and Controller 03) ###################################

print()
# New Antecedent/Consequent objects hold universe variables and membership functions
controller_two = ctrl.Antecedent(np.arange(0, 26, 1), 'controller_two')
controller_three = ctrl.Antecedent(np.arange(0, 26, 1), 'controller_three')
experience = ctrl.Consequent(np.arange(0, 50, 1), 'experience')
# Auto-membership function population is possible with .automf(3, 5, or 7)
controller_two.automf(3)
controller_three.automf(3)
# Custom membership functions can be built interactively with a familiar, Pythonic API
experience['low'] = fuzz.trimf(experience.universe, [0, 0, 25])
experience['medium'] = fuzz.trimf(experience.universe, [0, 25, 50])
experience['high'] = fuzz.trimf(experience.universe, [25, 50, 50])
#define rules
rule1 = ctrl.Rule(controller_two['poor'] | controller_three['poor'], experience['low'])
rule2 = ctrl.Rule(controller_three['average'], experience['medium'])
rule3 = ctrl.Rule(controller_three['good'] | controller_two['good'], experience['high'])
#create the control system
experience_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
experiencing = ctrl.ControlSystemSimulation(experience_ctrl)
# Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
# Note: if you like passing many inputs all at once, use .inputs(dict_of_data)

c4array = [len(c2array)]
for x in range(0,len(c2array)):
    experiencing.input['controller_two']=float(c2array[x])
    experiencing.input['controller_three']=float(c3array[x])
    experiencing.compute()#Crunch the numbers
    c4array.append(experiencing.output['experience'])
    print(experiencing.output['experience'])

###################################  Controler 05 (Controller 01 and Controller 04) ###################################

print()
# New Antecedent/Consequent objects hold universe variables and membership functions
controller_one = ctrl.Antecedent(np.arange(0, 51, 1), 'controller_one')
controller_four = ctrl.Antecedent(np.arange(0, 51, 1), 'controller_four')
experience = ctrl.Consequent(np.arange(0, 100, 1), 'experience')
# Auto-membership function population is possible with .automf(3, 5, or 7)
controller_one.automf(3)
controller_four.automf(3)
# Custom membership functions can be built interactively with a familiar, Pythonic API
experience['low'] = fuzz.trimf(experience.universe, [0, 0, 50])
experience['medium'] = fuzz.trimf(experience.universe, [0, 50, 100])
experience['high'] = fuzz.trimf(experience.universe, [50, 100, 100])
#define rules
rule1 = ctrl.Rule(controller_one['poor'] | controller_four['poor'], experience['low'])
rule2 = ctrl.Rule(controller_four['average'], experience['medium'])
rule3 = ctrl.Rule(controller_four['good'] | controller_one['good'], experience['high'])
#create the control system
experience_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
experiencing = ctrl.ControlSystemSimulation(experience_ctrl)
# Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
# Note: if you like passing many inputs all at once, use .inputs(dict_of_data)

c5array = [len(c1array)]
for x in range(0,len(c1array)):
    experiencing.input['controller_one']=float(c1array[x])
    experiencing.input['controller_four']=float(c4array[x])
    experiencing.compute()#Crunch the numbers
    c5array.append(experiencing.output['experience'])
    print(experiencing.output['experience'])





#csvfile = "Test.csv"
#with open(csvfile, "w") as output:
 #   writer = csv.writer(output, lineterminator='\n')
  #  for val in final:
   #     writer.writerow([val])


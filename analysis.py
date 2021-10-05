import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 8)
general = pd.read_csv('test/general.csv')
prenatal = pd.read_csv('test/prenatal.csv')
sports = pd.read_csv('test/sports.csv')

# Renaming columns
prenatal.rename(columns={'HOSPITAL': 'hospital', 'Sex': 'gender'}, inplace=True)
sports.rename(columns={'Hospital': 'hospital', 'Male/female': 'gender'}, inplace=True)

# Concat all 3 data set and delete unnecessary column
merged_data = pd.concat([general, prenatal, sports], ignore_index=True)
del merged_data['Unnamed: 0']

# Delete empty rows
merged_data.dropna(axis=0, how='all', inplace=True)

# Normalise m/f for gender column
merged_data.replace(['female', 'woman'], 'f', inplace=True)
merged_data.replace(['male', 'man'], 'm', inplace=True)
merged_data['gender'] = merged_data['gender'].fillna('f')

# Replace NaN to 0 in bmi, diagnosis, blood_test, ecg, ultrasound, mri, xray, children, months
column_set = ['bmi', 'diagnosis', 'blood_test', 'ecg', 'ultrasound', 'mri', 'xray', 'children', 'months']
for column in merged_data:
    if column in column_set:
        merged_data[column] = merged_data[column].fillna(0)

# Printing the data
# print(merged_data.shape)
# merged_sample = merged_data.sample(n=20, random_state=30)
# print(merged_sample)

"""
Stage 4

# Question 1
qn1 = merged_data['hospital'].value_counts().idxmax()

# Question 2
total_num_general = len(merged_data.loc[(merged_data['hospital'] == 'general')])
total_num_stomach = len(merged_data.loc[(merged_data['hospital'] == 'general') & (merged_data['diagnosis'] == 'stomach')])
qn2 = total_num_stomach / total_num_general

# Question 3  dislocation
total_num_sports = len(merged_data.loc[(merged_data['hospital'] == 'sports')])
total_num_dislocation = len(merged_data.loc[(merged_data['hospital'] == 'sports') & (merged_data['diagnosis'] == 'dislocation')])
qn3 = total_num_dislocation / total_num_sports

# Question 4
general_patients = merged_data['hospital'] == 'general'
general_median = merged_data.loc[general_patients, 'age'].median()
sports_patients = merged_data['hospital'] == 'sports'
sports_median = merged_data.loc[sports_patients, 'age'].median()
diff_in_median = general_median - sports_median


# Question 5
# qn5 = merged_data['blood_test'].value_counts()
gen_blood_test = len(merged_data.loc[(merged_data['hospital'] == 'general') & (merged_data['blood_test'] == 't')])
pren_blood_test = len(merged_data.loc[(merged_data['hospital'] == 'prenatal') & (merged_data['blood_test'] == 't')])
spo_blood_test = len(merged_data.loc[(merged_data['hospital'] == 'sports') & (merged_data['blood_test'] == 't')])
total_blood_test = {'general': gen_blood_test, 'prenatal': pren_blood_test, 'sports': spo_blood_test}
highest_blood_test = max(total_blood_test, key=total_blood_test.get)


print(f'The answer to the 1st question is {qn1}')
print(f'The answer to the 2nd question is {round(qn2, 3)}')
print(f'The answer to the 3rd question is {round(qn3, 3)}')
print(f'The answer to the 4th question is {diff_in_median}')
print(f'The answer to the 5th question is {highest_blood_test}, {total_blood_test[highest_blood_test]} blood tests')
"""

# Stage 5, Data Visualization
f1 = merged_data.plot(y=['age'], kind='hist', bins=[0, 15, 35, 55, 70, 80])

plt.figure()
f2 = merged_data.diagnosis.str.split('|', expand=True).stack().value_counts().plot(kind='pie', label='Diagnosis')

plt.figure()
f3 = plt.violinplot([merged_data.height])
plt.show()

print('The answer to the 1st question: 15 - 35')
print('The answer to the 2nd question: pregnancy')
print("The answer to the 3rd question: It's because sports hospital patients are much taller than general and prenatal.")

# # saving the DataFrame as a CSV file
# merged_csv_data = merged_data.to_csv('merged.csv', index=True)
# print('\nCSV String:\n', merged_csv_data)

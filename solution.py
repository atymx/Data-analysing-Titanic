import pandas
from scipy.stats import pearsonr

# file with DATA about passengers
data = pandas.read_csv("titanic.csv", ',')

# file with answers
answer_file = open("answer.txt", 'w')

# ----------------------- number of men and women ---------------------------------
number_of_men = len(data[data.Sex == 'male'])
number_of_women = len(data[data.Sex == 'female'])

answer_file.write('{}\n'.format('Number of men and women'))
answer_file.write('{} {}\n\n'.format(number_of_men, number_of_women))
# ---------------------------------------------------------------------------------


# ----------------- present of survived passengers --------------------------------
present_survived = len(data[data.Survived == True]) / 891 * 100

answer_file.write('{}\n'.format('Present of survived passengers'))
answer_file.write('{}\n\n'.format(present_survived))
# ---------------------------------------------------------------------------------


# ---------------- present of FIRST_CLASS passengers ------------------------------
present_first_class = len(data[data.Pclass == 1]) / 891 * 100

answer_file.write('{}\n'.format('Present of FIRST_CLASS passengers'))
answer_file.write('{}\n\n'.format(present_first_class))
# ---------------------------------------------------------------------------------


# -------------------------- mead and median age ----------------------------------
mead_age = data['Age'].mean()
median_age = data['Age'].median()

answer_file.write('{}\n'.format('Mean and median age'))
answer_file.write('{} {}\n\n'.format(mead_age, median_age))
# ---------------------------------------------------------------------------------


# -------------------- most popular female name -----------------------------------
female_names = list(data['Name'][data.Sex == 'female'])
for i in range(len(female_names)):
    female_names[i] = female_names[i].split(',')[1][1:]

statistic = {}
for el in female_names:
    statistic[el] = female_names.count(el)

answer = ''
for key in statistic.keys():
    if (answer == '') or (statistic[answer] < statistic[key]):
        answer = key

answer_file.write('{}\n'.format('The most popular female name'))
answer_file.write('{}\n\n'.format(answer.split('. ')[1]))
# ---------------------------------------------------------------------------------


# - correlation number(brothers/sisters/spouses) & number(parents/children) count -

answer_file.write('{}\n'.format('Correlation count'))
answer_file.write('{}\n\n'.format(pearsonr(data['SibSp'], data['Parch'])[0]))
# ---------------------------------------------------------------------------------

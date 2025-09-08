import pandas as pd
import numpy as np
# Merging dataframes
employees=pd.DataFrame({
    'employee_id':[1,2,3,4,5],
    'name':['Alice','Bob','Charlie','David','Eva'],
    'department':['HR','IT','Finance','IT','HR']

})
salaries=pd.DataFrame({
    'employee_id':[1,2,3,6,7],
    'salary':[60000,70000,80000,90000,100000],
    'bonus':[5000,6000,7000,8000,9000]
})
# print("Employees DataFrame:",employees,sep="\n")
# print("Salaries DataFrame:",salaries,sep="\n")
print(pd.merge(employees,salaries ,on='employee_id'))
## common ids waly merge ho jaye gyein
## on= mean jiski base pr merge karna hai
## inner by default hota hai mean andar side pr jo employee id hai us mein jo common part hai usky base pr merge krdu ga
# print(pd.merge(employees,salaries ,on='employee_id',how='outer'))
# #outer mean dono side pr jitny bi id hain unko merge krdu ga aur jo missing value hain unko NaN krdu ga
print(pd.merge(employees,salaries ,on='employee_id',how='left'))
## left mean left side pr jitny bi id hain unko merge krdu ga aur jo missing value hain unko NaN krdu ga
print(pd.merge(employees,salaries ,on='employee_id',how='right'))
## right mean right side pr jitny bi id hain unko merge krdu ga aur jo missing value hain unko NaN krdu ga
## agar column name same nahi hain to left_on and right_on


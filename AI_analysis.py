import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("Ai_job.csv")
print(data.info())
print(data.head())
data['Salary_USD'].hist()
plt.title('histogram of column ')
plt.xlabel('value')
plt.ylabel('frequency')
plt.show()
sns.pairplot(data)
plt.show()

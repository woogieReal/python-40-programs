import pandas as pd
import os

# 경로를 .py파일의 실행경로로 이동, 현재 경로로 이동
os.chdir(os.path.dirname(os.path.abspath(__file__)))

"""
PassengerId: Id of every passenger.
Survived: Indication whether passenger survived. 0 for yes and 1 for no.
Pclass: One out of the 3 ticket classes: Class 1, Class 2 and Class 3.
Name: Name of passenger.
Sex: Gender of passenger.
Age: Age of passenger in years.
SibSp: Number of siblings or spouses aboard.
Parch: Number of parents or children aboard.
Ticket: Ticket number of passenger.
Fare: Indicating the fare.
Cabin: Cabin number of passenger.
Embarked: Port of embarkation.
"""

titanic = pd.read_csv("titanic.csv")
ten_rows = titanic.head(10)
print(ten_rows)

# 평군 값 구하기
average_age = titanic["Age"].mean()
print(average_age)
# -> 29.69911764705882

# 중위 값 구하기
# 두 컬럼 이상 선택시 DataFrame 반환
median_vals = titanic[["Age", "Fare"]].median()
print(median_vals)
"""
Age     28.0000
Fare    14.4542
dtype: float64
"""

# 한 번에 여러 컬럼에 대해 통계를 집계 할 수 있다.
stats = titanic[["Age", "Fare"]].describe()
print(stats)
"""
              Age        Fare
count  714.000000  891.000000
mean    29.699118   32.204208
std     14.526497   49.693429
min      0.420000    0.000000
25%     20.125000    7.910400
50%     28.000000   14.454200
75%     38.000000   31.000000
max     80.000000  512.329200
"""

# 미리 정의된 통계 대신 특정 열의 집계 통계 조합을 정의할 수 있다.
specific_stats = titanic.agg(
    {
        "Age": ["min", "max", "median", "skew"],
        "Fare": ["min", "max", "median", "mean"],
    }
)
print(specific_stats)
"""
              Age        Fare
min      0.420000    0.000000
max     80.000000  512.329200
median  28.000000   14.454200
skew     0.389108         NaN
mean          NaN   32.204208
"""
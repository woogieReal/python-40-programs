import pandas as pd
import matplotlib.pyplot as plt
import os

# 경로를 .py파일의 실행경로로 이동, 현재 경로로 이동
os.chdir(os.path.dirname(os.path.abspath(__file__)))

air_quality = pd.read_csv("air_quality_no2.csv", index_col=0, parse_dates=True)
ten_rows = air_quality.head(10)
print(ten_rows)

# 차트 이미지로 추출
air_quality.plot()
# -> <AxesSubplot: xlabel='datetime'>
plt.show()

# 특정 컬럼만 추출
air_quality["station_paris"].plot()
# -> <AxesSubplot: xlabel='datetime'>
plt.show()

# 각각의 컬럼 값을 그래프로 추출, subplots을 사용
axs = air_quality.plot.area(figsize=(12, 4), subplots=True)
plt.show()


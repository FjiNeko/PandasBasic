import numpy as np
import pandas as pd

s = pd.Series()
print(s, type(s), s.dtype)

# Series 通过ndarray创建Series对象
ary = np.array([70, 80, 90, 95])
s = pd.Series(ary)
print(s)
# 行级索引标签
s = pd.Series(ary, index=['zs', 'ls', 'ww', 'zl'])
print(s, s['zs'])

# 从字典创建一个系列
dic = {'zs': 80, 'ww': 90, 'tq': 60, 'wb': 100}
s = pd.Series(dic)
print(s)

# 通过标量, 创建Series
s = pd.Series(1 / 5, index=np.arange(5))
print(s)

# 使用索引检索元素
s = pd.Series(ary, index=['zs', 'ls', 'ww', 'zl'])
print(s.iloc[3])
print(s['zl'])
print(s.iloc[1:])
print(s[['ls', 'ww', 'zl']])

# Pandas日期处理
'''
pandas 可以识别以下时间戳类型：
- 2011
- 2011-02
- 2011-03-01
- 2011/04/01
- 2011/05/01 01:01:01
- 01 Jun 2011
'''
# 测试pandas的日期处理
# 构建日期类型的Series
dates = pd.Series(['2011', '2011-02', '2011-03-01', '2011/04/01', '2011/05/01 01:01:01', '01 Jun 2011'])
dates = pd.to_datetime(dates, format='mixed')
print(dates, dates.dtype, type(dates))
# 日期运算
delta = dates - pd.to_datetime('2011-01-01')
print(delta)
# 把delta转换成数字
print(delta.dt.days)
print(dates.dt.dayofweek)
print(dates.dt.is_month_start)
print(dates.dt.is_month_end)
print(dates.dt.is_quarter_start)
print(dates.dt.is_quarter_end)

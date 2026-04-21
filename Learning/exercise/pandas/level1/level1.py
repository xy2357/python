import pandas as pd

df = pd.DataFrame(
    [
        ("小红", "哈利波特", 80),
        ("小明", "蜘蛛侠", 72),
        ("小红", "雷神", 83),
        ("小红", "蜘蛛侠", 45),
        ("小明", "超人", 57),
    ],
    columns=("人", "人物", "评价"),
)
print(df)
print(df.groupby('人').groups)

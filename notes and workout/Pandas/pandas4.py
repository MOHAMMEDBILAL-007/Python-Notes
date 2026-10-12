# Interpolation
import pandas as pd
data = {
    "time":[1,2,3,4,5],
    "value":[10,None,30,40,50]
}
df = pd.DataFrame(data)
print("dataframe before interppolation")
print(df)

print("\ndataframe after interpolation")
df["value"]= df["value"].interpolate(method="linear")
print(df)


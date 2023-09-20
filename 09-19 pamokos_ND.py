import pandas as pd
import matplotlib as pdb
import csv
with open("COVID.csv", "rb") as infile, open("COVID2.csv", "wb") as outfile:
    next(infile)  # skip the headers
    outfile.write(infile.read())
data = pd.read_csv('COVID2.csv')
df = pd.DataFrame(data)
print(df)


# Apskaičiuokite vidutini užsikrėtusiu virusu skaičių per savaitę;
# vid_susirgimai = df['Weekly COVID-19 Hospital Admissions'].mean()
# print(df)

# Atvaizduokite grafike kaip skiriasi užsikretusiu skaičius per mėnesį;

# Apskaičiuokite ir atvaizduokite,kuri mėnesį buvo daugiausiai užsikrėtimų;
# max_susirgimu = df['Weekly COVID-19 Hospital Admissions'].max()
# print(max_susirgimu)

# Atvaizuokite kiekvieno mėnesio užsikrėtimų skaičių(procentaliai)lyginant su praėjusiu mėnesiu. PIE grafike;

import pandas as pd
import matplotlib.pyplot as plt

filepath = '../../sample_data/02 Introduction to Pandas/edited_googleplaystore_dataset.csv'
cos_brut_df = pd.read_csv('..\CSV_files\produccion_bruta_cosechas_1940_1950_1960_1965_1970_1971.csv', index_col='Fechas')
cos_cereal_df = cos_brut_df[['LeguminosasDeGrano','SemillasOleaginosas','Girasol','Patata','Vegetales','MaizEnsilaje_VerdurasForraje','RemolachaAzucarera','FibraLino_MilesTon.']]
print(cos_cereal_df)
cos_cereal_df.plot(style='.-', title='Producción de cereal 1940-1971',ylabel='Miles de toneladas',xlabel='Año')
plt.show()

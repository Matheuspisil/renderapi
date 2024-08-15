import pandas as pd

# Load the CSV files
metas_path = 'C:/gestordecarreira/rebasado/gestordecarreiras/gestordecarreiras/media/GPC/arquivos/metasespecificas.csv'
planos_path = 'C:/gestordecarreira/rebasado/gestordecarreiras/gestordecarreiras/media/GPC/arquivos/planosdeacao.csv'
estudos_path = 'C:/gestordecarreira/rebasado/gestordecarreiras/gestordecarreiras/media/GPC/arquivos/meusestudos.csv'

metas_df = pd.read_csv(metas_path)
planos_df = pd.read_csv(planos_path)
estudos_df = pd.read_csv(estudos_path)

# Add the new columns with default values
metas_df['meta'] = metas_df.apply(lambda row: row.name, axis=1)
planos_df['plano'] = planos_df.apply(lambda row: row.name, axis=1)
estudos_df['estudo'] = estudos_df.apply(lambda row: row.name, axis=1)

# Save the updated CSV files
metas_df.to_csv(metas_path, index=False)
planos_df.to_csv(planos_path, index=False)
estudos_df.to_csv(estudos_path, index=False)

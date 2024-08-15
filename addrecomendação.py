import pandas as pd

# Paths to your CSV files
metas_path = 'C:/gestordecarreira/rebasado/gestordecarreiras/gestordecarreiras/media/GPC/arquivos/metasespecificas.csv'
planos_path = 'C:/gestordecarreira/rebasado/gestordecarreiras/gestordecarreiras/media/GPC/arquivos/planosdeacao.csv'
estudos_path = 'C:/gestordecarreira/rebasado/gestordecarreiras/gestordecarreiras/media/GPC/arquivos/meusestudos.csv'

# Load the CSV files
metas_df = pd.read_csv(metas_path)
planos_df = pd.read_csv(planos_path)
estudos_df = pd.read_csv(estudos_path)

# Add missing columns with default values if they don't exist
if 'recomendacao' not in metas_df.columns:
    metas_df['recomendacao'] = 'Default Recommendation for Meta'

if 'recomendacao' not in planos_df.columns:
    planos_df['recomendacao'] = 'Default Recommendation for Plano'

if 'recomendacao' not in estudos_df.columns:
    estudos_df['recomendacao'] = 'Default Recommendation for Estudo'

# Save the updated CSV files
metas_df.to_csv(metas_path, index=False)
planos_df.to_csv(planos_path, index=False)
estudos_df.to_csv(estudos_path, index=False)

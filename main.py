import pandas as pd
# caminho do arquivo principal
main_file = 'analise_de_dados_com_spotify/dados/dados_audio.csv'
# lendo arquivo principal
main_df = pd.read_csv(main_file)
# renomeando colunas no csv
main_df = main_df.rename(columns={
    ',': 'index',
    'ts': 'data',
    'master_metadata_track_name': 'track',
    'master_metadata_album_artist_name': 'artist',
    'master_metadata_album_album_name': 'album',
})

print(main_df.head(10))

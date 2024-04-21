import pandas as pd
from datetime import datetime as dt
# funções

# converter para data dd-mm-yyyy


def toDate(column):
    # tirando os últimos 10 caracteres
    formater = dt.fromisoformat(column[:10])
    # formatando
    return formater.strftime('%Y-%m-%d')


# dados
grouped_songs_df = []

# caminho do arquivo principal
main_file = 'analise_de_dados_com_spotify/dados/dados_audio.csv'
# lendo arquivo principal
main_df = pd.read_csv(main_file, index_col=False)
# renomeando colunas no csv
main_df = main_df.rename(columns={
    'ts': 'date',
    'master_metadata_track_name': 'track',
    'master_metadata_album_artist_name': 'artist',
    'master_metadata_album_album_name': 'album',
})
# pegando apenas a data
main_df['date'] = main_df['date'].apply(toDate)
# agrupando com os mesmos dados de música, artista e álbum
# significando que é o mesmo dado e fazendo um count quando se repete
grouped_songs_df = main_df.groupby(
    ['track', 'artist', 'album']).size().reset_index(name='count')
# agrupando os artistas
grouped_artists_df = main_df.groupby('artist').size().reset_index(name='count')
# agrupando os álbuns
grouped_albums_df = main_df.groupby('album').size().reset_index(name='count')
# músicas mais ouvidas
times_heard_song_df = grouped_songs_df.sort_values(by='count', ascending=False)
# álbuns mais ouvidos
times_heard_artist_df = grouped_artists_df.sort_values(
    by='count', ascending=False)
# artistas mais ouvidos
times_heard_album_df = grouped_albums_df.sort_values(
    by='count', ascending=False)

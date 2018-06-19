data_fetchers = {
                    'name': 'tracks',
                    'type': 'sqlite',
                    'file': 'chinook.db',
                    'table': {'tracks': 't'},
                    'fields': {
                        'alb.Title': 'album',
                        't.Name': 'track',
                        't.Milliseconds': 'ms'
                    },
                    'join': [{
                            'table': {'albums': 'alb'},
                            'on': {
                                'alb.AlbumId': 't.AlbumId',
                            }
                        },
                        {
                            'table': {'artists': 'art'},
                            'on': {
                                'alb.ArtistId': 'art.ArtistId',
                            }
                        }
                    ],
                    'condition': {
                        'art.ArtistId': 'artist_id',
                    }
                }


def generate_context(doc_param, data, metadata):
    df = data['tracks']
    df_groups = df.groupby('album').groups
    albums = []
    for album, indices in df_groups.items():
        albums.append({
            'title': album,
            'tracks': [
                {
                    'name': row.track,
                    'duration': '{:.1f} min'.format(int(row.ms) / (60 * 1000))
                }
                for row in df.ix[indices, ['track', 'ms']].itertuples()
            ]
        })
    return {'albums': albums}

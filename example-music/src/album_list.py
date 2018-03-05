data_fetcher = {
                    'name': 'albums',
                    'type': 'sqlite',
                    'file': 'chinook.db',
                    'table': {'artists': 'a'},
                    'fields': {
                        'alb.Title': 'album'
                    },
                    'condition': {
                        'a.ArtistId': 'artist_id',
                    },
                    'join': {
                        'table': {'albums': 'alb'},
                        'on': {
                            'alb.ArtistId': 'a.ArtistId',
                        }
                    }
                }


def generate_context(doc_var, data, metadata):
    df = data['albums']
    albums_titles = list(df.ix[:, 'album'])
    return {
                'albums': albums_titles
            }

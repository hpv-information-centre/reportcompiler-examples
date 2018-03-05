data_fetcher <- list(
					list(	name='artist',
							type='sqlite', 
							file='chinook.db',
							table='artists',
							fields=list(	
									ArtistId='artist_id',
									Name='artist_name'
										),
							condition=list(ArtistId='artist_id')
						)
					)
					
generate_context <- function(doc_var, data, metadata) {
	df <- data$artist
	return(list(
				artist=list(
					id=df$artist_id,
					name=df$artist_name
					)))
			
}
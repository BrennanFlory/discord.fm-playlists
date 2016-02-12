import youtube_dl

playlists = ['http://www.youtube.com/playlist?list=PLggPK4S5-fhhhKuFGJRlphZzpMLzgPXRJ', 'Unknown URL', 'Unknown URL']  # Put playlists here
ytdl_format_options = {
    'format': 'bestaudio/best',
    'extractaudio': True,
    'audioformat': "mp3",
    'outtmpl': '%(id)s',  # part file temp name
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': True,
    'quiet': True,
    'no_warnings': True,
    'source_address': '0.0.0.0'
}

ydl = youtube_dl.YoutubeDL(ytdl_format_options)
with open('country-countdown.txt', 'a+', encoding='utf8') as f:
    for url in playlists:
        print('Starting extraction of playlist #{}'.format((playlists.index(url)+1)))
        for e in ydl.extract_info(url, download=False, process=False)['entries']:
            if e:
                f.write('\n#{}\nhttps://www.youtube.com/watch?v={}\n'.format(e['title'], e['url']))
print('done')

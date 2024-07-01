from pytube import YouTube

def download_youtube_video(video_url, output_path='.'):
    try:
        # Crear un objeto YouTube
        yt = YouTube(video_url)
        
        # Seleccionar la mejor resolución para descargar el video
        video_stream = yt.streams.get_highest_resolution()
        
        # Descargar el video
        print(f"Descargando: {yt.title}")
        video_stream.download(output_path)
        print(f"Descarga completa. Archivo guardado en: {output_path}/{yt.title}.mp4")
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")

# URL del video de YouTube que deseas descargar
video_url = 'https://www.youtube.com/watch?v=5JkCSgXUPCM&ab_channel=Yuwana'

# Ruta de salida donde se guardará el video descargado
output_path = './OUT'

# Llamada a la función para descargar el video
download_youtube_video(video_url, output_path)


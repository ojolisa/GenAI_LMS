from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs


def get_transcript(video_url):
    # Parse the URL and extract the video ID
    url_data = urlparse(video_url)
    path_parts = url_data.path.split('/')
    video_id = path_parts[-1] if len(path_parts) > 1 else None

    try:
        # Get the transcript for the video
        transcript = YouTubeTranscriptApi.get_transcript(video_id)

        # Extract the text from each transcript entry
        text = ' '.join([entry['text'] for entry in transcript])

        # Return the extracted transcript
        return text

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

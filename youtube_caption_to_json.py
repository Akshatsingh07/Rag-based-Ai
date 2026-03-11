import json
import sys
import re
import os
from youtube_transcript_api import YouTubeTranscriptApi
from pytube import Playlist


OUTPUT_PATH = "yt_jsons/captions.json"


def extract_video_id(url):
    """
    Supports:
    watch?v=
    youtu.be/
    shorts/
    """

    patterns = [
        r"v=([0-9A-Za-z_-]{11})",
        r"youtu\.be\/([0-9A-Za-z_-]{11})",
        r"shorts\/([0-9A-Za-z_-]{11})"
    ]

    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)

    return None


def is_playlist(url):
    return "list=" in url


def get_playlist_video_ids(url):

    print("Playlist detected")

    playlist = Playlist(url)

    video_ids = []

    for video_url in playlist.video_urls:

        vid = extract_video_id(video_url)

        if vid:
            video_ids.append(vid)

    return video_ids

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter


def fetch_transcript(video_id):

    try:

        transcript = YouTubeTranscriptApi.get_transcript(
            video_id,
            languages=['en','en-US','en-GB']
        )

        return transcript

    except Exception as e:

        try:

            # fallback: fetch any language
            transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

            for transcript in transcript_list:
                return transcript.fetch()

        except:
            print("Captions unavailable for:", video_id)

        return []


def convert_to_json(all_transcripts):

    formatted = []

    counter = 0

    for video_index, transcript in enumerate(all_transcripts):

        for item in transcript:

            formatted.append({
                "title": f"video_{video_index}",
                "number": counter,
                "timestamp": item["start"],
                "text": item["text"]
            })

            counter += 1

    return formatted


def save_json(data):

    os.makedirs("yt_jsons", exist_ok=True)

    with open(OUTPUT_PATH, "w") as f:
        json.dump(data, f, indent=2)

    print("\nSaved captions to:", OUTPUT_PATH)
    print("Total transcript chunks:", len(data))


def process_url(url):

    video_ids = []

    if is_playlist(url):

        video_ids = get_playlist_video_ids(url)

    else:

        vid = extract_video_id(url)

        if not vid:
            print("Invalid YouTube URL")
            sys.exit()

        video_ids = [vid]

    print("Videos found:", len(video_ids))

    all_transcripts = []

    for vid in video_ids:

        print("Fetching captions for:", vid)

        transcript = fetch_transcript(vid)

        if transcript:
            all_transcripts.append(transcript)

    if not all_transcripts:
        print("No captions retrieved.")
        sys.exit()

    data = convert_to_json(all_transcripts)

    save_json(data)


if __name__ == "__main__":

    if len(sys.argv) < 2:

        print("Usage:")
        print("python youtube_caption_to_json.py <youtube_url>")
        sys.exit()

    url = sys.argv[1]

    process_url(url)
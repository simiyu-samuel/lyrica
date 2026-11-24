"""Fetch and print a song's lyrics using the Genius API."""

import argparse
import os
import sys
import time


def fetch_lyrics(song_title, artist, access_token=None):
    """Return lyrics information for a song."""
    try:
        import lyricsgenius
    except ImportError as exc:
        raise RuntimeError(
            "The 'lyricsgenius' package is not installed. "
            "Install it with: py -m pip install lyricsgenius"
        ) from exc

    token = access_token or os.getenv("GENIUS_ACCESS_TOKEN")
    if not token:
        raise RuntimeError(
            "A Genius access token is required. Set the GENIUS_ACCESS_TOKEN "
            "environment variable or pass access_token to print_lyrics()."
        )

    genius = lyricsgenius.Genius(token)
    genius.verbose = False
    genius.remove_section_headers = True

    try:
        song = genius.search_song(song_title, artist)
    except Exception as exc:
        raise RuntimeError(f"Could not connect to Genius: {exc}") from exc

    if not song:
        return None

    return {
        "title": getattr(song, "title", song_title),
        "artist": getattr(song, "artist", artist),
        "lyrics": getattr(song, "lyrics", "").strip(),
    }


def print_lyrics(song_title, artist, access_token=None, line_delay=0.0):
    """Print lyrics for a song, or raise a clear error when unavailable."""
    song = fetch_lyrics(song_title, artist, access_token)
    if song is None:
        print("Lyrics not found.")
        return False

    for line in song["lyrics"].splitlines():
        print(line)
        sys.stdout.flush()
        if line_delay > 0:
            time.sleep(line_delay)
    return True


def main():
    parser = argparse.ArgumentParser(description="Fetch and print song lyrics.")
    parser.add_argument("song_title", nargs="?", help="Song title")
    parser.add_argument("artist", nargs="?", help="Artist name")
    parser.add_argument(
        "--delay",
        type=float,
        default=0.0,
        help="Seconds to wait between lines",
    )
    args = parser.parse_args()

    song_title = args.song_title or input("Song title: ").strip()
    artist = args.artist or input("Artist: ").strip()
    if not song_title or not artist:
        parser.error("Both a song title and artist are required.")
    if args.delay < 0:
        parser.error("--delay cannot be negative.")

    try:
        print_lyrics(song_title, artist, line_delay=args.delay)
    except RuntimeError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

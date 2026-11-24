"""Flask web application for searching and displaying Genius lyrics."""

import os

from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request

from lyrics import fetch_lyrics


load_dotenv()
app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False


@app.get("/")
def index():
    return render_template("index.html")


@app.post("/api/lyrics")
def lyrics_api():
    payload = request.get_json(silent=True) or {}
    song_title = str(payload.get("title", "")).strip()
    artist = str(payload.get("artist", "")).strip()

    if not song_title or not artist:
        return jsonify(
            {"error": "Enter both a song title and an artist."}
        ), 400

    if not os.getenv("GENIUS_ACCESS_TOKEN"):
        return jsonify(
            {
                "error": (
                    "The server is missing its Genius access token. "
                    "Set GENIUS_ACCESS_TOKEN and restart the app."
                )
            }
        ), 503

    try:
        song = fetch_lyrics(song_title, artist)
    except RuntimeError as exc:
        return jsonify({"error": str(exc)}), 502

    if song is None:
        return jsonify(
            {"error": "No lyrics were found for that title and artist."}
        ), 404

    return jsonify(song)


if __name__ == "__main__":
    app.run(debug=True)

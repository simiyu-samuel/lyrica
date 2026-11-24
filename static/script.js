const form = document.getElementById("searchForm");
const status = document.getElementById("status");
const lyricsCard = document.getElementById("lyricsCard");
const lyricsContainer = document.getElementById("lyrics");
const errorCard = document.getElementById("errorCard");
const errorMessage = document.getElementById("errorMessage");
const searchButton = document.getElementById("searchButton");
const themeToggle = document.getElementById("themeToggle");
const copyButton = document.getElementById("copyButton");

const savedTheme = localStorage.getItem("lyrica-theme");
if (savedTheme === "dark") {
    document.body.classList.add("dark");
}

themeToggle.addEventListener("click", () => {
    document.body.classList.toggle("dark");
    localStorage.setItem(
        "lyrica-theme",
        document.body.classList.contains("dark") ? "dark" : "light"
    );
});

document.getElementById("closeError").addEventListener("click", () => {
    errorCard.hidden = true;
});

copyButton.addEventListener("click", async () => {
    try {
        await navigator.clipboard.writeText(lyricsContainer.innerText);
        const label = copyButton.querySelector("span");
        label.textContent = "Copied";
        setTimeout(() => {
            label.textContent = "Copy";
        }, 1600);
    } catch {
        errorMessage.textContent = "Your browser blocked clipboard access.";
        errorCard.hidden = false;
    }
});

form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const title = document.getElementById("songTitle").value.trim();
    const artist = document.getElementById("artistName").value.trim();

    if (!title || !artist) {
        errorMessage.textContent = "Enter both a song title and an artist.";
        errorCard.hidden = false;
        return;
    }

    errorCard.hidden = true;
    lyricsCard.hidden = true;
    lyricsContainer.replaceChildren();
    status.hidden = false;
    searchButton.disabled = true;

    try {
        const response = await fetch("/api/lyrics", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ title, artist })
        });
        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "The lyrics could not be loaded.");
        }

        document.getElementById("resultTitle").textContent = data.title;
        document.getElementById("resultArtist").textContent = data.artist;

        const lines = data.lyrics.split(/\r?\n/);
        for (let index = 0; index < lines.length; index += 1) {
            const line = document.createElement("p");
            line.className = "lyric-line";
            line.style.animationDelay = `${Math.min(index * 28, 1200)}ms`;

            if (lines[index].trim()) {
                line.textContent = lines[index];
            } else {
                line.className += " blank";
                line.setAttribute("aria-hidden", "true");
            }
            lyricsContainer.appendChild(line);
        }

        lyricsCard.hidden = false;
        lyricsCard.scrollIntoView({ behavior: "smooth", block: "start" });
    } catch (error) {
        errorMessage.textContent = error.message;
        errorCard.hidden = false;
    } finally {
        status.hidden = true;
        searchButton.disabled = false;
    }
});

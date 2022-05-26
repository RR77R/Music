from os import path

from yt_dlp import YoutubeDL

from config import BOT_NAME as bn, DURATION_LIMIT
from helpers.errors import DurationLimitError

ydl_opts = {
    "format": "bestaudio/best",
    "verbose": True,
    "geo-bypass": True,
    "nocheckcertificate": True,
    "outtmpl": "downloads/%(id)s.%(ext)s",
}
ydl = YoutubeDL(ydl_opts)


def download(url: str) -> str:
    info = ydl.extract_info(url, False)
    duration = round(info["duration"] / 60)

    if duration > DURATION_LIMIT:
        raise DurationLimitError(
            f"- مدة الفيديو اكبر من  {DURATION_LIMIT} دقيقة لا يمكن تحميله، الوقت المسموح به للفيديو هو {duration} دقيقة"
        )

    ydl.download([url])
    return path.join("downloads", f"{info['id']}.{info['ext']}")

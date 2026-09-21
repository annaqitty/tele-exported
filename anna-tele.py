import os
import asyncio
from telethon import TelegramClient
from telethon.tl.types import DocumentAttributeFilename

# =========================
# CONFIG
# =========================
API_ID = 12345678
API_HASH = "YOUR_API_HASH"

SESSION = "telegram_session"

# =========================
# INPUT
# =========================
channel = input("Telegram channel username/link: ").strip()

extensions_input = input(
    "Extensions to download (example: jpg,png,mp4,pdf): "
).strip().lower()

extensions = {
    ext.strip().lower().lstrip(".")
    for ext in extensions_input.split(",")
    if ext.strip()
}

output_dir = input(
    "Output folder [telegram_export]: "
).strip() or "telegram_export"

os.makedirs(output_dir, exist_ok=True)


def get_extension(message):
    """
    Get the real filename extension from Telegram document metadata.
    """
    if not message.document:
        return None

    for attr in message.document.attributes:
        if isinstance(attr, DocumentAttributeFilename):
            filename = attr.file_name
            if "." in filename:
                return filename.rsplit(".", 1)[1].lower()

    # Fallback based on MIME type
    mime = message.document.mime_type or ""

    mime_map = {
        "image/jpeg": "jpg",
        "image/png": "png",
        "image/webp": "webp",
        "image/gif": "gif",
        "video/mp4": "mp4",
        "audio/mpeg": "mp3",
        "application/pdf": "pdf",
        "application/zip": "zip",
        "text/plain": "txt",
    }

    return mime_map.get(mime)


async def main():
    client = TelegramClient(
        SESSION,
        API_ID,
        API_HASH
    )

    await client.start()

    print("\nConnected to Telegram.")
    print(f"Channel : {channel}")
    print(f"Extensions: {', '.join(sorted(extensions))}")
    print(f"Output  : {output_dir}")
    print("=" * 60)

    entity = await client.get_entity(channel)

    total = 0
    downloaded = 0
    skipped = 0

    async for message in client.iter_messages(entity, reverse=True):

        total += 1

        if not message.document:
            skipped += 1
            continue

        ext = get_extension(message)

        if not ext or ext not in extensions:
            skipped += 1
            continue

        # Telegram's original filename
        filename = None

        for attr in message.document.attributes:
            if isinstance(attr, DocumentAttributeFilename):
                filename = attr.file_name
                break

        if not filename:
            filename = f"{message.id}.{ext}"

        # Prevent problematic paths
        filename = os.path.basename(filename)

        destination = os.path.join(output_dir, filename)

        # Avoid overwriting duplicate filenames
        if os.path.exists(destination):
            base, extension = os.path.splitext(filename)
            destination = os.path.join(
                output_dir,
                f"{base}_{message.id}{extension}"
            )

        try:
            print(
                f"[{downloaded + 1}] "
                f"Downloading: {filename}"
            )

            await client.download_media(
                message,
                file=destination
            )

            downloaded += 1

        except Exception as e:
            print(f"[ERROR] Message {message.id}: {e}")

    print("\n" + "=" * 60)
    print("Finished")
    print(f"Messages scanned : {total}")
    print(f"Files downloaded : {downloaded}")
    print(f"Skipped          : {skipped}")
    print(f"Output folder    : {os.path.abspath(output_dir)}")

    await client.disconnect()


if __name__ == "__main__":
    asyncio.run(main())

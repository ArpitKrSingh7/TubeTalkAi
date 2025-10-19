from langchain_yt_dlp.youtube_loader import YoutubeLoaderDL
from langchain_community.document_loaders import YoutubeLoader
from langchain_community.document_loaders.youtube import TranscriptFormat

def load_youtube_video():
    url = input("Enter the YouTube video URL: ")

    meta_loader = YoutubeLoaderDL.from_youtube_url(youtube_url=url, add_video_info=True)
    meta_docs = meta_loader.load()
    video_meta = meta_docs[0].metadata

    loader = YoutubeLoader.from_youtube_url(
        youtube_url=url,
        add_video_info=False,
        language=["en", "hi"],
        transcript_format=TranscriptFormat.CHUNKS,
        chunk_size_seconds=120,
    )
    docs = loader.load()
    for doc in docs:
        doc.metadata.update(video_meta)

    print(f"✅ Loaded {len(docs)} transcript chunks.")
    return docs, video_meta

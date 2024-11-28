import services

transcript_path = "data/DKP - love and relationships/transcript.txt"

if __name__ == "__main__":
    transcript = services.convert.read_transcript_file(transcript_path)
    srt_content = services.convert.convert_to_srt(transcript
        )

    with open('output.srt', 'w') as file:
        file.write(srt_content)
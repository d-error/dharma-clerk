import services.convert as convert

transcript = convert.read_transcript_file("transcript.txt")

srt_content = convert.convert_to_srt(transcript
        )

print(srt_content)

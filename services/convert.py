def convert_to_srt(transcript):
    lines = transcript.strip().split('\n')
    srt_output = []
    counter = 1
    i = 0

    while i < len(lines):
        start = lines[i]
        text_lines = []

        # Collect all subsequent lines until we reach another timestamp or the end of the file
        while i + 1 < len(lines) and not lines[i + 1].replace(":", "").isdigit():
            text_lines.append(lines[i + 1])
            i += 1

        text = ' '.join(text_lines)
        
        # Determine end timestamp
        if i + 1 < len(lines):
            end = lines[i + 1]
        else:
            # Define a default duration (e.g., 2 seconds) for the last subtitle
            end = add_seconds_to_timestamp(start, 2)

        # Format start and end timestamps to SRT format (00:00:00,000)
        start = format_timestamp(start)
        end = format_timestamp(end)

        # Append to the SRT output
        srt_output.append(f"{counter}")
        srt_output.append(f"{start} --> {end}")
        srt_output.append(f"{text}")
        srt_output.append("")

        counter += 1
        i += 1

    return '\n'.join(srt_output)

def split_timestamp(timestamp):
    stamps = [int(n) for n in timestamp.split(':')]
    stamps.insert(0,0) if len(stamps)<3 else None
    hours, minutes, seconds = stamps
    return hours, minutes, seconds

def format_timestamp(timestamp):
    # Split into hours, minutes and seconds
    H, M, S = split_timestamp(timestamp)
    # Format as HH:MM:SS,MS
    return f"{H:02}:{M:02}:{S:02},000"

def add_seconds_to_timestamp(timestamp, seconds_to_add):
    from datetime import datetime, timedelta

    # Convert timestamp to datetime object
    hours, minutes, seconds = split_timestamp(timestamp)
    timestamp_dt = datetime(1, 1, 1, hours, minutes, seconds)

    # Add seconds
    new_timestamp_dt = timestamp_dt + timedelta(seconds=seconds_to_add)

    # Convert back to string
    return f"{new_timestamp_dt.minute}:{new_timestamp_dt.second}"

# Function to read the transcript from a file
def read_transcript_file(file_path):
    with open(file_path, 'r') as file:
        transcript = file.read()
    return transcript

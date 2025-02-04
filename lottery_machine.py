import argparse
import random
from pathlib import Path


def file(f):
    path = Path(f)
    if not path.exists():
        raise FileNotFoundError()
    return path


parser = argparse.ArgumentParser('Lottery machine')
parser.add_argument(
    'file', help='Path to a file with list of participants.', type=file)
parser.add_argument(
    '--show_page', help='Open a participant page.', action='store_true')
parser.add_argument(
    '--include_organizers', help='Include organizers in lottery.', action='store_true')
args = parser.parse_args()

# Read file.
participants = []
header = []
with open(args.file, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    header = list(lines[0].strip().split(','))
    for line in lines[1:]:
        # Remove unnecessary whitespace.
        line = line.strip()
        # Skip if line is empty.
        if not line:
            continue

        data = line.split(',')
        assert len(data) == len(header)
        # Do not include organizers, if flag is not set.
        if not args.include_organizers and data[header.index('Event Host')]:
            continue

        participants.append([data[0], data[2], data[4], data[16]])

# Main loop.
while True:
    try:
        # Select winner and obtain data.
        winner_id = random.randrange(len(participants))
        winner_data = participants[winner_id]

        # Print winner data.
        for (h, d) in zip(header, winner_data):
            print(f'{h}: {d}')
        print()

        # Show Meetup participant page.
        if args.show_page:
            import webbrowser
            webbrowser.open(winner_data[-1])

        # Remove entry from the list to avoid duplicates.
        del participants[winner_id]

        # Close on empty list or wait for user.
        if not participants:
            print('No participants left!')
            break
        print('Press enter to continue or Ctrl+C to exit.')
        input()
    except KeyboardInterrupt:
        break

from pathlib import Path

def analyze_file(path):
    """Counts the number of lines and words in a file."""

    contents = path.read_text(encoding='utf-8')
    report = f"File {path} has {len(contents.splitlines())} lines\n"
    report += f"It also has {len(contents.split())} words"
    path = Path('analyzed_text')
    path.write_text(report)

path = Path('huckleberry_finn.txt')
analyze_file(path)

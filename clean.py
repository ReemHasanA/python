from pathlib import Path
import re

# Load the file
file_path = Path("spacing.min.css")
css_content = file_path.read_text()

# Use a dictionary to store only unique styles
unique_classes = {}
pattern = r'(\.[a-zA-Z0-9\-]+)\{([^\}]+)\}'

for match in re.finditer(pattern, css_content):
    class_name = match.group(1)
    style = match.group(2)
    unique_classes[class_name] = style  # This will overwrite duplicates with the same class name

# Rebuild the minified CSS with unique class definitions
deduplicated_css = ''.join(f'{cls}{{{style}}}' for cls, style in unique_classes.items())

# Save the cleaned file
deduplicated_path = "spacing_deduplicated.min.css"
Path(deduplicated_path).write_text(deduplicated_css)

deduplicated_path
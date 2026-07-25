import os
import re
import glob

def remove_dashes(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace space followed by dash(es) followed by space
    # Matches normal hyphen (-), en-dash (–), and em-dash (—)
    # Replaces " - ", " – ", " — " with " "
    new_content = re.sub(r' ([-–—]+) ', ' ', content)
    
    # Also replace instances without spaces if they are typical AI generation artifacts?
    # No, let's be safe and only replace ones surrounded by spaces, or specific ones.
    # Actually, the AI might have generated bullets like:
    # <li>- Το γονιμοποιημένο ωάριο...</li>
    # Let's replace "<li>- " or "<li> - " or "<p>- "
    new_content = re.sub(r'>\s*[-–—]\s+', '>', new_content)
    
    if content != new_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")

# Process all html files
for root, dirs, files in os.walk('.'):
    if '_build' in root:
        continue
    for file in files:
        if file.endswith('.html') or file == 'i18n.js':
            filepath = os.path.join(root, file)
            remove_dashes(filepath)

print("Done removing dashes.")

import re

with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()

def replacer(match):
    img_tag = match.group(0)
    
    # Check if already a picture tag or snake animation
    if '<picture>' in img_tag or 'github-contribution-grid-snake' in img_tag:
        return img_tag

    # If it's a Vercel stats API, modify the themes
    if 'theme=tokyonight' in img_tag or 'theme=dark' in img_tag or 'tech-orbit.svg' in img_tag or 'terminal.svg' in img_tag:
        
        # Extract src
        src_match = re.search(r'src="(.*?)"', img_tag)
        if not src_match:
            src_match = re.search(r"src='(.*?)'", img_tag)
        if not src_match:
            return img_tag
            
        src = src_match.group(1)
        
        # For custom SVGs we created
        if 'terminal.svg' in src:
            light_src = src.replace('terminal.svg', 'terminal-light.svg')
        elif 'tech-orbit.svg' in src:
            light_src = src.replace('tech-orbit.svg', 'tech-orbit-light.svg')
        else:
            # For stats APIs
            light_src = src.replace('theme=tokyonight', 'theme=default').replace('theme=dark', 'theme=light')
            light_src = light_src.replace('bg_color=0d1117', 'bg_color=ffffff')
            light_src = light_src.replace('title_color=7fdbff', 'title_color=0969da')
            light_src = light_src.replace('text_color=c9d1d9', 'text_color=24292f')
            light_src = light_src.replace('icon_color=7fdbff', 'icon_color=0969da')
            light_src = light_src.replace('background=0d1117', 'background=ffffff')
            light_src = light_src.replace('stroke=7fdbff', 'stroke=0969da')
            light_src = light_src.replace('ring=7fdbff', 'ring=0969da')
            light_src = light_src.replace('currStreakLabel=7fdbff', 'currStreakLabel=0969da')
            light_src = light_src.replace('sideNums=7fdbff', 'sideNums=0969da')
            light_src = light_src.replace('sideLabels=7fdbff', 'sideLabels=0969da')
            light_src = light_src.replace('currStreakNum=FFFFFF', 'currStreakNum=24292f')
            light_src = light_src.replace('title_color=FFA116', 'title_color=d25b0a')
            light_src = light_src.replace('icon_color=FFA116', 'icon_color=d25b0a')
            light_src = light_src.replace('icon_color=FFCA28', 'icon_color=d25b0a')
            light_src = light_src.replace('title_color=FFCA28', 'title_color=d25b0a')

        return f'''<picture>
  <source media="(prefers-color-scheme: dark)" srcset="{src}">
  <source media="(prefers-color-scheme: light)" srcset="{light_src}">
  {img_tag}
</picture>'''
    
    return img_tag

# Only apply to img tags that don't already belong to a picture group
# (Simple regex: find all <img> tags, but we'll have to manually avoid nested ones if they were there)
# Actually, it's safer to just split by <img>
new_content = re.sub(r'<img [^>]+>', replacer, content)

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(new_content)

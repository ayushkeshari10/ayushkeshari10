import re

with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix double tech-orbit picture tag
bad_tech_orbit = """<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/ayushkeshari10/ayushkeshari10/main/assets/tech-orbit.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/ayushkeshari10/ayushkeshari10/main/assets/tech-orbit-light.svg">
  <picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/ayushkeshari10/ayushkeshari10/main/assets/tech-orbit.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/ayushkeshari10/ayushkeshari10/main/assets/tech-orbit-light.svg">
  <img width="380" alt="Tech Orbit" src="https://raw.githubusercontent.com/ayushkeshari10/ayushkeshari10/main/assets/tech-orbit.svg">
</picture>
</picture>"""

good_tech_orbit = """<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/ayushkeshari10/ayushkeshari10/main/assets/tech-orbit.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/ayushkeshari10/ayushkeshari10/main/assets/tech-orbit-light.svg">
  <img width="380" alt="Tech Orbit" src="https://raw.githubusercontent.com/ayushkeshari10/ayushkeshari10/main/assets/tech-orbit.svg">
</picture>"""

content = content.replace(bad_tech_orbit, good_tech_orbit)

# 2. Fix Header Capsule
header_old = '<img width="100%" src="https://capsule-render.vercel.app/api?type=venom&color=gradient&customColorList=6,11,20&height=240&section=header&text=Ayush%20Keshari&fontSize=58&fontColor=fff&animation=fadeIn&fontAlignY=38&desc=Full-Stack%20Developer%20%7C%20DSA%20Enthusiast%20%7C%20Builder&descAlignY=58&descSize=20&reversal=false&stroke=7fdbff&strokeWidth=1" />'
header_new = """<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://capsule-render.vercel.app/api?type=venom&color=gradient&customColorList=6,11,20&height=240&section=header&text=Ayush%20Keshari&fontSize=58&fontColor=fff&animation=fadeIn&fontAlignY=38&desc=Full-Stack%20Developer%20%7C%20DSA%20Enthusiast%20%7C%20Builder&descAlignY=58&descSize=20&reversal=false&stroke=7fdbff&strokeWidth=1">
  <source media="(prefers-color-scheme: light)" srcset="https://capsule-render.vercel.app/api?type=venom&color=gradient&customColorList=10,24,28&height=240&section=header&text=Ayush%20Keshari&fontSize=58&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Full-Stack%20Developer%20%7C%20DSA%20Enthusiast%20%7C%20Builder&descAlignY=58&descSize=20&reversal=false&stroke=0969da&strokeWidth=1">
  <img width="100%" src="https://capsule-render.vercel.app/api?type=venom&color=gradient&customColorList=6,11,20&height=240&section=header&text=Ayush%20Keshari&fontSize=58&fontColor=fff&animation=fadeIn&fontAlignY=38&desc=Full-Stack%20Developer%20%7C%20DSA%20Enthusiast%20%7C%20Builder&descAlignY=58&descSize=20&reversal=false&stroke=7fdbff&strokeWidth=1" />
</picture>"""
content = content.replace(header_old, header_new)

# 3. Fix Typing SVG
typing_old = '[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=22&duration=2800&pause=900&color=7FDBFF&center=true&vCenter=true&multiline=false&random=false&width=680&lines=Hey+there%2C+I\'m+Ayush+%F0%9F%91%8B;Full-Stack+Web+Developer+%F0%9F%9A%80;React+%7C+Node.js+%7C+Python+%7C+C%2B%2B;DSA+Enthusiast+%7C+Competitive+Coder+%F0%9F%A7%A9;SIH+2026+Finalist+%F0%9F%8F%86;Building+CareerMind-AI+%F0%9F%A4%96;Open+Source+Contributor+%F0%9F%8C%8D;Always+learning%2C+always+growing+%F0%9F%8C%B1)](https://git.io/typing-svg)'
typing_new = """<a href="https://git.io/typing-svg">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=22&duration=2800&pause=900&color=7FDBFF&center=true&vCenter=true&multiline=false&random=false&width=680&lines=Hey+there%2C+I'm+Ayush+%F0%9F%91%8B;Full-Stack+Web+Developer+%F0%9F%9A%80;React+%7C+Node.js+%7C+Python+%7C+C%2B%2B;DSA+Enthusiast+%7C+Competitive+Coder+%F0%9F%A7%A9;SIH+2026+Finalist+%F0%9F%8F%86;Building+CareerMind-AI+%F0%9F%A4%96;Open+Source+Contributor+%F0%9F%8C%8D;Always+learning%2C+always+growing+%F0%9F%8C%B1">
    <source media="(prefers-color-scheme: light)" srcset="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=22&duration=2800&pause=900&color=0969da&center=true&vCenter=true&multiline=false&random=false&width=680&lines=Hey+there%2C+I'm+Ayush+%F0%9F%91%8B;Full-Stack+Web+Developer+%F0%9F%9A%80;React+%7C+Node.js+%7C+Python+%7C+C%2B%2B;DSA+Enthusiast+%7C+Competitive+Coder+%F0%9F%A7%A9;SIH+2026+Finalist+%F0%9F%8F%86;Building+CareerMind-AI+%F0%9F%A4%96;Open+Source+Contributor+%F0%9F%8C%8D;Always+learning%2C+always+growing+%F0%9F%8C%B1">
    <img alt="Typing SVG" src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=22&duration=2800&pause=900&color=7FDBFF&center=true&vCenter=true&multiline=false&random=false&width=680&lines=Hey+there%2C+I'm+Ayush+%F0%9F%91%8B;Full-Stack+Web+Developer+%F0%9F%9A%80;React+%7C+Node.js+%7C+Python+%7C+C%2B%2B;DSA+Enthusiast+%7C+Competitive+Coder+%F0%9F%A7%A9;SIH+2026+Finalist+%F0%9F%8F%86;Building+CareerMind-AI+%F0%9F%A4%96;Open+Source+Contributor+%F0%9F%8C%8D;Always+learning%2C+always+growing+%F0%9F%8C%B1">
  </picture>
</a>"""
content = content.replace(typing_old, typing_new)

# 4. Fix Activity Graph
activity_old = '<img width="100%" src="https://github-readme-activity-graph.vercel.app/graph?username=ayushkeshari10&bg_color=0d1117&color=7fdbff&line=7fdbff&point=FFFFFF&area=true&area_color=0a2540&hide_border=true&custom_title=Ayush%27s%20Contribution%20Timeline&radius=8" alt="Activity Graph"/>'
activity_new = """<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-activity-graph.vercel.app/graph?username=ayushkeshari10&bg_color=0d1117&color=7fdbff&line=7fdbff&point=FFFFFF&area=true&area_color=0a2540&hide_border=true&custom_title=Ayush%27s%20Contribution%20Timeline&radius=8">
  <source media="(prefers-color-scheme: light)" srcset="https://github-readme-activity-graph.vercel.app/graph?username=ayushkeshari10&bg_color=ffffff&color=0969da&line=0969da&point=24292f&area=true&area_color=e1ebfa&hide_border=true&custom_title=Ayush%27s%20Contribution%20Timeline&radius=8">
  <img width="100%" src="https://github-readme-activity-graph.vercel.app/graph?username=ayushkeshari10&bg_color=0d1117&color=7fdbff&line=7fdbff&point=FFFFFF&area=true&area_color=0a2540&hide_border=true&custom_title=Ayush%27s%20Contribution%20Timeline&radius=8" alt="Activity Graph"/>
</picture>"""
content = content.replace(activity_old, activity_new)

# 5. Fix Footer Capsule
footer_old = '<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=130&section=footer" />'
footer_new = """<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=130&section=footer">
  <source media="(prefers-color-scheme: light)" srcset="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=10,24,28&height=130&section=footer">
  <img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=130&section=footer" />
</picture>"""
content = content.replace(footer_old, footer_new)

# 6. Fix LeetCode stats (wait, checking if it was fixed earlier. Wait I'll just check if it's there without picture)
# It's already fixed in fix_light_mode.py but maybe it missed it. Let me just replace the whole leetcode line if it exists.

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(content)

import os
import re

ga4 = '''<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-09Q743BF93"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-09Q743BF93');
</script>'''

files = ['index.html', 'campaigns.html', 'units.html', 'tactics.html', 'command.html', 'about.html', 'privacy-policy.html']

for f in files:
    if not os.path.exists(f):
        print(f'Skipping: {f}')
        continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()

    # Add GA4 if not present
    if 'G-09Q743BF93' not in content:
        content = content.replace('    <style>', ga4 + '\n    <style>')
        print(f'Added GA4: {f}')

    # Update domain
    content = content.replace('battleplan.wiki', 'battleplan.online')

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f'Updated domain: {f}')

import os

ad_head = '''<script async="async" data-cfasync="false" src="https://bauval.org/21/dda0038a529b2eb0582e4671bae3856e"></script>
<script data-cfasync="false" src="https://bauval.org/14/f2c29cadb5eff7d0c0ba6a37d574bae9"></script>
<script>
  atOptions = {
    'key' : 'd8b0901d81801dc1cf952629be349883',
    'format' : 'iframe',
    'height' : 250,
    'width' : 300,
    'params' : {}
  };
</script>
<script src="https://bauval.org/22/d8b0901d81801dc1cf952629be349883"></script>'''

ad_body = '''<div style="display: flex; justify-content: center; margin: 20px 0;">
    <div id="container-dda0038a529b2eb0582e4671bae3856e"></div>
</div>'''

files = ['index.html', 'campaigns.html', 'units.html', 'tactics.html', 'command.html', 'about.html', 'privacy-policy.html']

for f in files:
    if not os.path.exists(f):
        print(f'Skipping: {f}')
        continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()

    # Add ad scripts to head (before </head>)
    if 'd8b0901d81801dc1cf952629be349883' not in content:
        content = content.replace('</head>', ad_head + '\n</head>')
        print(f'Added head scripts: {f}')

    # Add container div before footer
    if 'container-dda0038a529b2eb0582e4671bae3856e' not in content:
        content = content.replace('<footer', ad_body + '\n\n<footer')
        print(f'Added container div: {f}')

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f'Updated: {f}')

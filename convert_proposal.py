#!/usr/bin/env python3
"""Convert markdown proposal to styled HTML for sharing."""

import re
from pathlib import Path

def md_to_html(md_content):
    """Basic markdown to HTML conversion."""
    html = md_content
    
    # Headers (must be at start of line)
    html = re.sub(r'^###### (.+)$', r'<h6>\1</h6>', html, flags=re.MULTILINE)
    html = re.sub(r'^##### (.+)$', r'<h5>\1</h5>', html, flags=re.MULTILINE)
    html = re.sub(r'^#### (.+)$', r'<h4>\1</h4>', html, flags=re.MULTILINE)
    html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    
    # Bold and italic
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html)
    
    # Inline code
    html = re.sub(r'`([^`]+)`', r'<code>\1</code>', html)
    
    # Blockquotes
    html = re.sub(r'^> (.+)$', r'<blockquote>\1</blockquote>', html, flags=re.MULTILINE)
    
    # Unordered lists
    html = re.sub(r'^\* (.+)$', r'<li>\1</li>', html, flags=re.MULTILINE)
    html = re.sub(r'^- (.+)$', r'<li>\1</li>', html, flags=re.MULTILINE)
    
    # Paragraph breaks (double newline)
    html = re.sub(r'\n\n+', r'</p><p>', html)
    
    return html

def create_styled_html(md_path, html_path):
    """Read markdown and create styled HTML."""
    # Read markdown
    md_content = Path(md_path).read_text()
    
    # Convert to HTML
    body_html = md_to_html(md_content)
    
    # Full HTML template with styling
    html_template = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Graph Database Memory Enhancement Proposal</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.6; color: #333; max-width: 900px; margin: 0 auto; padding: 40px 20px; background: #fafafa; }}
        h1 {{ color: #1a1a1a; font-size: 2.5em; margin-bottom: 0.5em; border-bottom: 3px solid #0066cc; padding-bottom: 10px; }}
        h2 {{ color: #2c3e50; margin-top: 2em; margin-bottom: 1em; border-left: 4px solid #0066cc; padding-left: 15px; }}
        h3 {{ color: #34495e; margin-top: 1.5em; margin-bottom: 0.8em; }}
        table {{ width: 100%; border-collapse: collapse; margin: 1em 0; background: white; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
        th, td {{ padding: 12px 15px; text-align: left; border-bottom: 1px solid #ddd; }}
        th {{ background: #0066cc; color: white; font-weight: 600; }}
        tr:nth-child(even) {{ background: #f8f9fa; }}
        tr:hover {{ background: #e9ecef; }}
        code {{ background: #f4f4f4; padding: 2px 6px; border-radius: 3px; font-family: 'Courier New', monospace; }}
        pre {{ background: #2d2d2d; color: #f8f8f2; padding: 15px; border-radius: 5px; overflow-x: auto; margin: 1em 0; }}
        blockquote {{ border-left: 4px solid #0066cc; padding-left: 20px; margin: 1em 0; color: #555; font-style: italic; }}
        .summary-box {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 20px; border-radius: 8px; margin: 1.5em 0; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }}
        .summary-box h3 {{ color: white; border: none; margin-top: 0; }}
        ul, ol {{ margin-left: 2em; margin-bottom: 1em; }}
        li {{ margin-bottom: 0.5em; }}
        a {{ color: #0066cc; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
        .note {{ font-style: italic; color: #666; font-size: 0.9em; margin-top: 0.5em; }}
        p {{ margin-bottom: 1em; }}
    </style>
</head>
<body>
<p>{body_html}</p>
</body>
</html>'''
    
    # Write HTML
    Path(html_path).write_text(html_template)
    print(f'HTML created: {html_path}')

if __name__ == '__main__':
    create_styled_html(
        '/Users/kaushal/workspace/proposals/graph-database-memory-enhancement.md',
        '/Users/kaushal/workspace/share.ksubedi.com/public/n8cDCGNa9Y8wvumuPWEDRg.html'
    )

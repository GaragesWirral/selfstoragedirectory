import os
import re

def add_blog_link(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the navigation menu
    nav_pattern = r'<nav>\s*<ul>([\s\S]*?)</ul>\s*</nav>'
    nav_match = re.search(nav_pattern, content)
    
    if nav_match:
        nav_content = nav_match.group(1)
        
        # Check if blog link already exists
        if 'href="../../blog/index.html"' not in nav_content and 'href="/blog/index.html"' not in nav_content:
            # Add blog link before Storage Calculator
            new_nav_content = nav_content.replace(
                '<li><a href="../../calculator/index.html">Storage Calculator</a></li>',
                '<li><a href="../../blog/index.html">Blog</a></li>\n<li><a href="../../calculator/index.html">Storage Calculator</a></li>'
            )
            
            # Update the content
            new_content = content.replace(nav_content, new_nav_content)
            
            # Write back to file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Added blog link to {file_path}')
            return True
    
    return False

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                add_blog_link(file_path)

# Process all HTML files in the website directory
process_directory('website') 
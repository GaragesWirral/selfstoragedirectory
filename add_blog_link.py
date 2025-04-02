import os
import re

def add_blog_link(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the navigation menu
    nav_pattern = r'<nav>\s*<ul>.*?</ul>\s*</nav>'
    nav_match = re.search(nav_pattern, content, re.DOTALL)
    
    if nav_match:
        nav_content = nav_match.group(0)
        
        # Check if blog link already exists
        if 'href="../blog/index.html">Blog</a></li>' in nav_content:
            return
        
        # Add blog link before Storage Calculator
        new_nav = nav_content.replace(
            '<li><a href="../storage-calculator/index.html">Storage Calculator</a></li>',
            '<li><a href="../blog/index.html">Blog</a></li>\n                <li><a href="../storage-calculator/index.html">Storage Calculator</a></li>'
        )
        
        # Update the content
        new_content = content.replace(nav_content, new_nav)
        
        # Write back to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"Added blog link to {file_path}")

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                add_blog_link(file_path)

if __name__ == '__main__':
    website_dir = 'website'
    process_directory(website_dir) 
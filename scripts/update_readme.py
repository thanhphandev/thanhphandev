#!/usr/bin/env python3
"""
Script to update README.md with dynamic content
"""

import os
import re
import requests
from datetime import datetime, timezone
from typing import List, Dict, Any

class GitHubProfileUpdater:
    def __init__(self, username: str = "thanhphandev"):
        self.username = username
        self.github_token = os.getenv('GITHUB_TOKEN')
        self.headers = {
            'Authorization': f'token {self.github_token}',
            'Accept': 'application/vnd.github.v3+json'
        } if self.github_token else {}
        
    def get_latest_repos(self, limit: int = 6) -> List[Dict[str, Any]]:
        """Fetch latest public repositories"""
        try:
            url = f"https://api.github.com/users/{self.username}/repos"
            params = {
                'sort': 'updated',
                'direction': 'desc',
                'per_page': limit,
                'type': 'public'
            }
            
            response = requests.get(url, headers=self.headers, params=params)
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Failed to fetch repositories: {response.status_code}")
                return []
        except Exception as e:
            print(f"Error fetching repositories: {e}")
            return []
    
    def format_repo_for_readme(self, repo: Dict[str, Any]) -> str:
        """Format repository data for README"""
        name = repo['name']
        description = repo['description'] or 'No description available'
        url = repo['html_url']
        language = repo['language'] or 'Unknown'
        stars = repo['stargazers_count']
        
        # Truncate description if too long
        if len(description) > 100:
            description = description[:97] + "..."
            
        return f"- **[{name}]({url})** - {description} `{language}` ⭐ {stars}"
    
    def get_recent_projects_section(self) -> str:
        """Generate recent projects section"""
        repos = self.get_latest_repos()
        if not repos:
            return "🔄 *Unable to fetch repositories at the moment*"
        
        projects_list = []
        for repo in repos:
            if repo['name'] != self.username:  # Skip profile repo
                projects_list.append(self.format_repo_for_readme(repo))
                
        if not projects_list:
            return "🔄 *No recent projects to display*"
            
        return "\n".join(projects_list[:5])  # Limit to 5 projects
    
    def update_readme(self):
        """Update README.md with dynamic content"""
        readme_path = "README.md"
        
        if not os.path.exists(readme_path):
            print("README.md not found!")
            return
            
        with open(readme_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Update timestamp
        current_time = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
        content = re.sub(
            r'\*\*🔄 Last Updated:\*\* `.*?`',
            f'**🔄 Last Updated:** `{current_time}`',
            content
        )
        
        # Update recent projects section
        projects_section = self.get_recent_projects_section()
        content = re.sub(
            r'<!-- PROJECTS_START -->.*?<!-- PROJECTS_END -->',
            f'<!-- PROJECTS_START -->\n{projects_section}\n<!-- PROJECTS_END -->',
            content,
            flags=re.DOTALL
        )
        
        # Write updated content back to file
        with open(readme_path, 'w', encoding='utf-8') as file:
            file.write(content)
        
        print("README.md updated successfully!")
        print(f"Last updated: {current_time}")

def main():
    """Main function"""
    updater = GitHubProfileUpdater()
    updater.update_readme()

if __name__ == "__main__":
    main()
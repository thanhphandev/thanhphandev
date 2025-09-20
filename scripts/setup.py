#!/usr/bin/env python3
"""
Setup script for GitHub profile automation
"""

import os
import sys
import subprocess
import json

def run_command(command, check=True):
    """Run a shell command"""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=check)
        return result.stdout.strip(), result.stderr.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {command}")
        print(f"Error: {e.stderr}")
        return None, e.stderr

def check_requirements():
    """Check if required tools are installed"""
    print("🔍 Checking requirements...")
    
    # Check Python
    python_version = sys.version_info
    if python_version.major < 3 or (python_version.major == 3 and python_version.minor < 8):
        print("❌ Python 3.8+ is required")
        return False
    print(f"✅ Python {python_version.major}.{python_version.minor}.{python_version.micro}")
    
    # Check Git
    git_output, git_error = run_command("git --version", check=False)
    if git_error:
        print("❌ Git is not installed")
        return False
    print(f"✅ {git_output}")
    
    return True

def install_dependencies():
    """Install Python dependencies"""
    print("\n📦 Installing dependencies...")
    
    stdout, stderr = run_command("pip install -r requirements.txt")
    if stderr:
        print(f"⚠️  Warning during installation: {stderr}")
    else:
        print("✅ Python dependencies installed")
    
    # Check if npm is available for future use
    npm_output, npm_error = run_command("npm --version", check=False)
    if not npm_error:
        print(f"✅ npm {npm_output} available")
        stdout, stderr = run_command("npm install", check=False)
        if not stderr:
            print("✅ npm dependencies installed")
    else:
        print("ℹ️  npm not available (optional)")

def setup_git_hooks():
    """Setup git hooks for automated updates"""
    print("\n🪝 Setting up git hooks...")
    
    hooks_dir = ".git/hooks"
    if not os.path.exists(hooks_dir):
        print("❌ Git hooks directory not found")
        return
    
    # Create pre-commit hook
    pre_commit_hook = os.path.join(hooks_dir, "pre-commit")
    with open(pre_commit_hook, 'w') as f:
        f.write("""#!/bin/sh
# Auto-update README before commit
python3 scripts/update_readme.py
git add README.md
""")
    
    # Make it executable
    os.chmod(pre_commit_hook, 0o755)
    print("✅ Pre-commit hook created")

def validate_structure():
    """Validate project structure"""
    print("\n🏗️  Validating project structure...")
    
    required_files = [
        "README.md",
        "scripts/update_readme.py",
        ".github/workflows/update-readme.yml",
        "requirements.txt",
        "package.json"
    ]
    
    missing_files = []
    for file_path in required_files:
        if not os.path.exists(file_path):
            missing_files.append(file_path)
    
    if missing_files:
        print(f"❌ Missing files: {', '.join(missing_files)}")
        return False
    
    print("✅ Project structure is valid")
    return True

def test_automation():
    """Test the automation script"""
    print("\n🧪 Testing automation...")
    
    stdout, stderr = run_command("python3 scripts/update_readme.py")
    if stderr and "DeprecationWarning" not in stderr:
        print(f"❌ Test failed: {stderr}")
        return False
    
    print("✅ Automation script works correctly")
    return True

def display_next_steps():
    """Display next steps for the user"""
    print("\n🎉 Setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Update personal information in README.md")
    print("2. Customize scripts/update_readme.py for your needs")
    print("3. Push changes to GitHub to trigger the first automation")
    print("4. Check GitHub Actions tab for workflow status")
    print("\n💡 Tips:")
    print("- The profile will auto-update daily")
    print("- You can manually trigger updates via GitHub Actions")
    print("- Check PROFILE_CONFIG.md for customization options")

def main():
    """Main setup function"""
    print("🚀 GitHub Profile Automation Setup")
    print("=" * 40)
    
    if not check_requirements():
        print("\n❌ Setup failed due to missing requirements")
        sys.exit(1)
    
    install_dependencies()
    setup_git_hooks()
    
    if not validate_structure():
        print("\n❌ Setup failed due to invalid project structure")
        sys.exit(1)
    
    if not test_automation():
        print("\n❌ Setup failed due to automation test failure")
        sys.exit(1)
    
    display_next_steps()

if __name__ == "__main__":
    main()
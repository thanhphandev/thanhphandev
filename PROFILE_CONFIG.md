# GitHub Profile Configuration

This repository contains the configuration and automation for my GitHub profile.

## 🛠️ Structure

```
├── .github/workflows/       # GitHub Actions workflows
│   └── update-readme.yml   # Main CI/CD workflow
├── scripts/                # Automation scripts
│   └── update_readme.py    # README update script
├── assets/                 # Static assets (images, etc.)
├── README.md              # Main profile README
├── package.json           # Node.js dependencies
├── requirements.txt       # Python dependencies
└── .gitignore            # Git ignore rules
```

## 🔄 Automation Features

- **Daily Updates**: Automatically updates profile stats and recent projects
- **Dynamic Content**: Fetches latest repositories and contributions
- **CI/CD Pipeline**: GitHub Actions workflow for seamless updates
- **Error Handling**: Graceful fallbacks when APIs are unavailable

## 🚀 How it Works

1. **Scheduled Trigger**: Runs daily at midnight UTC
2. **Data Fetching**: Collects latest GitHub data via API
3. **Content Generation**: Updates README sections with fresh content
4. **Auto-commit**: Commits changes back to the repository

## 📝 Customization

To customize this profile:

1. Update personal information in `README.md`
2. Modify the update script in `scripts/update_readme.py`
3. Adjust the schedule in `.github/workflows/update-readme.yml`
4. Add new features or sections as needed

## 🔧 Local Development

```bash
# Install Python dependencies
pip install -r requirements.txt

# Install Node.js dependencies (if any)
npm install

# Run the update script locally
python scripts/update_readme.py
```

## 📊 Statistics Sources

- [GitHub Readme Stats](https://github.com/anuraghazra/github-readme-stats)
- [GitHub Readme Streak Stats](https://github.com/DenverCoder1/github-readme-streak-stats)
- [GitHub Profile Trophy](https://github.com/ryo-ma/github-profile-trophy)
- [Activity Graph](https://github.com/ashutosh00710/github-readme-activity-graph)

## 🎨 Themes

The profile uses the "tokyonight" theme for consistency across all components.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
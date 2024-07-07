## Introduction to Git and GitHub

Git is a distributed version control system used to track changes in source code during software development. It allows multiple developers to work on a project simultaneously without interfering with each other’s changes. GitHub is a web-based platform that uses Git for version control and provides additional features for collaborative development.

## Setting Up Git and GitHub

### Installing Git

First, ensure that Git is installed on your GNU/Linux system. You can install Git using the package manager of your distribution.

For Debian-based systems (e.g., Ubuntu):

```bash
sudo apt-get update
sudo apt-get install git
```

For Red Hat-based systems (e.g., Fedora):

```bash
sudo dnf install git
```

Verify the installation:

```bash
git --version
```

### Configuring Git

Set up your user name and email address. This information will be associated with your commits:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

You can also set up your preferred text editor for Git:

```bash
git config --global core.editor nano
```

### Creating a GitHub Account

If you don't already have one, create a GitHub account at [GitHub.com](https://github.com/).

### Creating a New Repository on GitHub

1. **Go to GitHub** and log in.
2. **Create a New Repository**:
   - Click the "+" icon in the top-right corner and select "New repository".
   - Enter a repository name (e.g., `my-project`).
   - Optionally, add a description.
   - Choose to make the repository public or private.
   - Optionally, initialize with a README.
   - Optionally, add a `.gitignore` file tailored to your needs (e.g., for a Python project).
   - Optionally, choose a license if applicable.
   - Click "Create repository".

## Working with Git Locally

### Cloning the Repository

Clone the newly created repository to your local machine:

1. **Copy the Repository URL** from GitHub.
2. **Clone the Repository** using Git:
   ```bash
   git clone https://github.com/yourusername/my-project.git
   cd my-project
   ```

### Creating Directories and Files

Create a new directory and a markdown (more details about this file format at the end of this file) file:

```bash
mkdir docs
echo "# Project Documentation" > docs/README.md
```

You can create and edit files using any text editor, for example:

```bash
nano docs/README.md
```

### Adding and Committing Changes

Check the status of your repository:

```bash
git status
```

Add the new files to the staging area:

```bash
git add docs/README.md
```

Commit the changes with a descriptive message:

```bash
git commit -m "Add documentation directory and README.md file"
```

### Pushing Changes to GitHub

Push your local changes to the main branch on GitHub:

```bash
git push origin main
```

## Basic Git Operations

### Viewing the Commit History

You can view the commit history using:

```bash
git log
```

For a more concise view, use:

```bash
git log --oneline
```

### Branching and Merging

Create a new branch:

```bash
git checkout -b feature-branch
```

Make changes and commit them:

```bash
echo "## New Feature" >> docs/README.md
git add docs/README.md
git commit -m "Add new feature section to documentation"
```

Switch back to the main branch:

```bash
git checkout main
```

Merge the feature branch into the main branch:

```bash
git merge feature-branch
```

Push the merged changes to GitHub:

```bash
git push origin main
```

### Resolving Merge Conflicts

If there are conflicts during a merge, Git will prompt you to resolve them manually. Edit the conflicting files to resolve the issues, then:

```bash
git add resolved-file
git commit
```

## Advanced Git Features

### Stashing Changes

If you need to switch branches but have uncommitted changes, you can stash them:

```bash
git stash
```

Retrieve the stashed changes:

```bash
git stash pop
```

### Rebasing

Rebasing allows you to integrate changes from one branch into another. For example, to rebase your feature branch onto the main branch:

```bash
git checkout feature-branch
git rebase main
```

### Interactive Rebase

Interactive rebase allows you to modify commit history. Start an interactive rebase:

```bash
git rebase -i HEAD~n
```

Replace `n` with the number of commits you want to modify.

### Tagging

Tagging is useful for marking release points:

```bash
git tag -a v1.0 -m "Release version 1.0"
git push origin v1.0
```

## Git Workflows

### Feature Branch Workflow

- Create a new branch for each feature or bug fix.
- Work on the feature branch.
- Merge the feature branch into the main branch when the work is complete.

### Forking Workflow

- Fork the repository on GitHub.
- Clone the forked repository.
- Create a new branch for your work.
- Push the branch to your fork.
- Create a pull request to merge your changes into the original repository.

## Git and Markdown

Markdown is a lightweight markup language with plain-text formatting syntax. Go [here](Intro_MarkDown.md) for an introduction to MarkDown.


# Git Introduction

This guide provides a basic introduction to Git for beginners.

## What is Git?

Git is a **version control system** that helps you track changes in your code over time.

Think of it like saving different versions of a document, but much more powerful.

## Key Concepts

### Repository
- A repository (or "repo") is a folder that contains your project and its history

### Local vs Remote
- **Local repository**: The repository on your computer
- **Remote repository**: The repository on GitHub

### Commit
- A "snapshot" of your code at a specific point in time

## Essential Git Commands

### 1. Clone a repository

```bash
git clone https://github.com/username/repository-name.git
```

This downloads the repository from GitHub to your computer.

### 2. Check status

```bash
git status
```

Shows which files have been modified.

### 3. Stage changes

```bash
git add filename.py        # Add a specific file
git add .                  # Add all changed files
```

This prepares your changes to be committed.

### 4. Commit changes

```bash
git commit -m "Description of what you changed"
```

This saves a snapshot of your changes with a message describing what you did.

Example:
```bash
git commit -m "Complete task01: hello world function"
```

### 5. Push to GitHub

```bash
git push
```

This uploads your committed changes to GitHub.

### 6. Pull from GitHub

```bash
git pull
```

This downloads any changes from GitHub to your local repository.

## Typical Workflow

Here's a typical workflow for working on this course:

1. **Clone the repository** (first time only)
   ```bash
   git clone <repository-url>
   cd python-starter-1
   ```

2. **Make changes to your code**
   - Edit `.py` files to complete tasks

3. **Check what changed**
   ```bash
   git status
   git diff           # See detailed changes
   ```

4. **Stage and commit your changes**
   ```bash
   git add task01_hello.py
   git commit -m "Complete task 01a: hello world"
   ```

5. **Push to GitHub**
   ```bash
   git push
   ```

6. **Repeat steps 2-5** for each task

## Tips

### Write good commit messages
- Be descriptive about what you changed
- Examples:
  - ✅ Good: "Fix fizzbuzz function to handle multiples of 15"
  - ❌ Bad: "update", "fix", "changes"

### Commit frequently
- Commit after completing each small task
- This makes it easier to track your progress and undo mistakes

### Use `git diff` to review changes
Before committing, use `git diff` to see exactly what you changed.

## Common Problems and Solutions

### Problem: "Permission denied" when pushing
**Solution**: Make sure you have set up authentication with GitHub.
You may need to use a personal access token or SSH key.

### Problem: Files are not being tracked
**Solution**: Make sure you used `git add` before `git commit`.

### Problem: Want to undo changes
```bash
git checkout -- filename.py    # Undo changes to a file
git reset HEAD filename.py     # Unstage a file
```

## Additional Resources

- [Official Git Documentation](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)
- [Git Cheat Sheet (PDF)](https://education.github.com/git-cheat-sheet-education.pdf)

## Next Steps

After understanding these basics, you can learn about:

- **Branches** - working on features independently
- **Pull requests** - proposing changes
- **Merge conflicts** - resolving conflicting changes

See the [Pull Request Guide](/misc/github_pull_request.pdf) for more advanced topics.

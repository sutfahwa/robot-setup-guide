# Robot Framework Installation Guide

## Step 1: Install Python
1. Download Python from [python.org](https://www.python.org/downloads/)
2. Install Python and select the option "Add Python to PATH" during the installation.
3. After installation, open Command Prompt and type `python --version` or `pip --version` to check if it is working. If it works, Python has been successfully added to PATH.

## Step 2: Install pip (if not already installed)
1. Open Terminal (macOS) or Command Prompt (Windows).
2. Run the following command to check if pip is already installed:
    ```bash
    pip3 --version
    ```
3. If not found, download `get-pip.py` from [get-pip.py](https://bootstrap.pypa.io/get-pip.py) and run the command:
    ```bash
    python get-pip.py
    ```

## Step 3: Install the file
1. Download the `setup.py` file (from this repository) to your machine.
2. Navigate to the directory of the downloaded file. Run the following command to install:
    ```bash
    pip3 install .
    ```

## Step 4: Set up PATH
### For macOS
1. Open Terminal.
2. Edit the `.bash_profile` file (or `.zshrc` for zsh):
    ```bash
    vim ~/.bash_profile
    ```
   Or if using zsh:
    ```bash
    vim ~/.zshrc
    ```
3. Add the following line at the end of the file:
    ```bash
    export PATH="/Library/Frameworks/Python.framework/Versions/3.12/bin:$PATH"
    ```
4. Save and exit Vim by pressing `Esc` and typing `:wq`.
5. Load the new settings:
    ```bash
    source ~/.bash_profile
    ```
   Or if using zsh:
    ```bash
    source ~/.zshrc
    ```

### For Windows
1. Right-click on "This PC" or "My Computer" and select "Properties."
2. Click on "Advanced system settings."
3. In the "Advanced" tab, click "Environment Variables."
4. In "System variables," find the name "Path" and click "Edit."
5. Click "New" and add the path where Python is installed, such as:
    ```makefile
    C:\Python312\Scripts\
    C:\Python312\
    ```
6. Click "OK" to save the changes.

## Completion
Now you can use Robot Framework by running the command:
```bash
robot --version
```

## Remark 
In the future, If you want to upgrade library you can running the command in directory:
```bash
pip install --upgradebe  .
```

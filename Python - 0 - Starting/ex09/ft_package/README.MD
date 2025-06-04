# ft_package

**ft_package** is a simple example Python package that provides one utility function: `count_in_list`.

## 📦 Installation

You can install the package using pip after building it:

```bash
pip install dist/ft_package-0.0.1-py3-none-any.whl

🧠 Features
count_in_list(lst, item)
Returns the number of times item appears in lst.

📌 Usage
🧪 1.Clean the Build (if needed)
rm -rf build dist *.egg-info

📦 2. Build the Package
python3 setup.py sdist bdist_wheel

📥 3. Install the Package Locally
pip install --force-reinstall dist/ft_package-0.0.1-py3-none-any.whl

🧪 4. Test It in a Script
python3 tester.py

🛠️ Requirements
Python 3.x

🧑 Author
Eagle (eagle@42.fr)
42 School Sample Project

⚖️ License
MIT License


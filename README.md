# 🛠️ Hash Toolkit: Create & Crack Hashes with Python

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square)
![Status](https://img.shields.io/badge/Project-Active-brightgreen?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

A simple and effective Python-based toolkit to **generate** and **crack** hash values using popular hashing algorithms like **MD5, SHA1, SHA256, and SHA512**. Perfect for learning cybersecurity and hash functions in a hands-on way.

---

## 📦 Project Structure

hash-toolkit/
├── hashCreator.py       # Generate hashes for any input string
├── hashCracker.py       # Crack MD5 hashes using a wordlist
├── requirements.txt     
└── README.md            

---

## ✨ Features

✅ Generate hashes for any input using:
- MD5  
- SHA1  
- SHA256  
- SHA512

✅ Crack MD5 hashes by comparing them against a wordlist  
✅ Colorized terminal output for better visibility  
✅ Built-in file error handling  
✅ Lightweight and beginner-friendly

---

## 📌 1. Hash Generator – `hashCreator.py`

Generate common hash digests for a string input.

### ▶️ Usage

```bash
python3 hashCreator.py
```
💡 Example

Enter String: admin

<<<<<<<MD5>>>>>>>
21232f297a57a5a743894a0e4a801fc3

<<<<<<<Sha1>>>>>>>
d033e22ae348aeb5660fc2140aec35850c4da997

<<<<<<<Sha256>>>>>
8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918

<<<<<<<512>>>>>>>
c9adeab699ff04b8f47c8396...

🔓 2. Hash Cracker – hashCracker.py

Try to crack an MD5 hash by brute-forcing with a wordlist.

▶️ Usage

python3 hashCracker.py

💡 Example

Enter target hash: 21232f297a57a5a743894a0e4a801fc3
Enter wordlist path: wordlist.txt

✅ Output

[?] Trying: password
[?] Trying: letmein
[?] Trying: admin
[+] Password Found: admin

⚙️ Requirements

pip install -r requirements.txt

⚠️ Disclaimer

This tool is created for educational and ethical use only.
Do not use it on systems you do not own or do not have permission to test.
Unauthorized use may be illegal.

📄 License

This project is licensed under the MIT License.

👨‍💻 Author

Alper Alexandru Ozturk
📧 alperoztvrk@gmail.com

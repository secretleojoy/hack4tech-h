# Installation dependencies

## Windows system

Note: If your Python3 is installed in the system's Program Files directory, such as: `C:\Program Files\Python38`, then please run the command prompt cmd as an administrator to execute the following commands!

```bash
cd Garuda/
python -m pip install -U pip setuptools wheel -i https://mirrors.aliyun.com/pypi/simple/
pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
python garuda.py --help
```

## Linux system

### Ubuntu/Debian system (including kali)

1. Install git and pip3
```bash
sudo apt update
sudo apt install git python3-pip -y
```

2. Clone the Garuda project
```bash
git clone https://github.com/hack4tech-h/Garuda.git
```

3. Installation related dependencies
```bash
cd Garuda/
sudo apt install python3-dev python3-pip python3-testresources -y
sudo python3 -m pip install -U pip setuptools wheel -i https://mirrors.aliyun.com/pypi/simple/
sudo pip3 install --ignore-installed -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
python3 garuda.py --help
```

### RHEL/Centos system

1. Install git and pip3
```bash
sudo yum update
sudo yum install git python3-pip -y
```

2. Clone the Garuda project
```bash
git clone https://github.com/hack4tech-h/Garuda.git
```

3. Installation related dependencies
```bash
cd Garuda/
sudo yum install gcc python3-devel python3-pip -y
sudo python3 -m pip install -U pip setuptools wheel -i https://mirrors.aliyun.com/pypi/simple/
sudo pip3 install --ignore-installed -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
python3 garuda.py --help
```

## Darwin System

Clone the Garuda project
```bash
git clone https://github.com/hack4tech-h/Garuda.git
```

Installation related dependencies
```bash
cd Garuda/
python3 -m pip install -U pip setuptools wheel -i https://mirrors.aliyun.com/pypi/simple/
pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
python3 garuda.py --help
```

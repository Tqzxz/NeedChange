
# Environment Setting
    Since every time we create an new codespace, previous packages downloaded at last codesapce will vanish, we need set all we need again in this new codespace
## 1.  DownLoad Miniconda by run this conmmand : wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh ( Just for first time )
## 2.  Using sh command to run this miniconda.sh file, this is a pre-download file for miniconda: run this conmmand>>: sh miniconda.sh and just make everything default
## 3.  Now we have miniconda, and we could change the source of API downloading , in China it'd better to use this source:
    run this command: pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
## 4. Run this >>: conda env create -f environment.yml down the folder d2l-zh
## 5. Now we have a virtual environment with all required APIS
 Run this conda activate [the_path_of_environment]
.. _install-python-and-C++:

Install Python & C++
==========================

    Too many choice are existing for Python installation.

    I will show a step by step installation of python 3.x 64 bit with Visual Studio.

Install python & C++ with Visual Studio
--------------------------------------------------------

    The Visual Studio could be downloaded from:
    
        https://visualstudio.microsoft.com
    
    
    The following is an example of install python3(64bit) on Windows10 64bit system.
    
    1. Select the Visual Studio **Community** version at the VS website.
    
    .. image:: ../blogstatic/install-python/download_Vs.png
    
    2. Right Click the setup file and select **Run as administrator**
    
    .. image:: ../blogstatic/install-python/VS_install1.png
    
    3. Select the python package
    
    .. image:: ../blogstatic/install-python/vs_install2.png
    
    4. Select the C++ package(ignore it if you will not develop c++ code project)
    
    .. image:: ../blogstatic/install-python/vs_install3.png
    
    5. Click next to continue
    
    .. image:: ../blogstatic/install-python/vs_install4.png
    
    6. Click Finish to complete the installation steps
    
    7. Add Enviornment Variables to **PATH**
    
        Add C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64                       (default python3 path of VS)
        
        Add C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\Scripts       (default pip path of VS)
        
        Add C:\\Windows                                                                                                                                          (default py path of VS)
        
        Add C:\\Python27amd64\\Scripts                                                                                                            (default python2 pip path of VS,ignore if python2  is not installed)
        
    
    .. image:: ../blogstatic/install-python/vs_install5.png
    
    8. Check
    
        Get to the command line, open the Windows menu and type "command" in the search bar. Select **Command Prompt** from the search results.
        In the Command Prompt window, type the following and press Enter.
        :: 
        
            >>python
            
        If Python is installed and in your path, then this command will run python.exe and show you the version number.
        :: 
        
            Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32.
            Type "help", "copyright", "credits" or "license" for more information.
            
        otherwise,you'll see:
        :: 
        
            'python' is not recognized as an internal or external command, operable program or batch file.
        
        
Install Package
-------------------------------------
    1. Run Command Prompt as administrator
    
    .. image:: ../blogstatic/install-python/pkg_install_1.png
    
    2. Online install package using pip
    
        Let's use numpy library as example.
        
        In the Command Prompt window, if you have a proper proxy setting ,type the following and press Enter.
        :: 
        
            >>pip install numpy
    
        Otherwise, Please type the following and press Enter.
        ::
        
            >>pip install numpy --proxy="http://child-prc.intel.com:913"
            
        if pip can access, you'll see:
        ::
        
            Collecting numpy
            Downloading https://files.pythonhosted.org/packages/ce/61/be72eee50f042db3acf0b1fb86650ad36d6c0d9be9fc29f8505d3b9d6baa/numpy-1.16.4-cp37-cp37m-win_amd64.whl (11.9MB)
            100% ||||||||||||||||||||||||||||||||||||| 11.9MB 1.6MB/s
            Installing collected packages: numpy
            Successfully installed numpy-1.16.4
    
    3. Offline install package using pip
        
        whl file or archives file
        
        Download the whl file and type in following and press Enter
        ::
        
            >>pip install C:/some-dir/some-file.whl
            >>pip install ./downloads/SomeProject-1.0.4.tar.gz
    
        
    
Summary
--------------
    This Chapter is a tutorial of python/C++ installation .
    
    
    
Install Notepad++
==========================
    Notepad++ is a free (as in "free speech" and also as in "free beer") source code editor and Notepad replacement that supports several languages.
    Running in the MS Windows environment, its use is governed by GPL License.
    
Install Notepad++
-------------------------------------------
    The Notepad++ could be downloaded from:
    
        https://notepad-plus-plus.org/
    
    1. Download the win64 setup file.
    
    .. image:: ../blogstatic/install-python/notepadpp.jpg
    
    2. Click next to continue(use default setting)
    
    .. image:: ../blogstatic/install-python/notepadpp2.png
    
    3. Click Finish to complete the installation steps
    
    4. Open notepad++ and type 'F5' or open Run-> Run...(see following picture)
    
    .. image:: ../blogstatic/install-python/notepadpp3.png
    
    5. Type follwing command into the window and Click 'Save'
    
        ::
        
            >>cmd /k cd "$(CURRENT_DIRECTORY)" & python "$(FULL_CURRENT_PATH)" & PAUSE & EXIT
    
            
    .. image:: ../blogstatic/install-python/notepadpp4.png 
            
    6. Setting of the shortcut window and click 'OK'
    
    .. image:: ../blogstatic/install-python/notepadpp5.png
    
    7. File-> New test.py file and type in
    
        ::
        
            >>print ('Hello world!')
            
    .. image:: ../blogstatic/install-python/notepadpp6.png
    
    8. Save and press 'CTRL'+'SHIFT'+'F5'
    You will see the output in Windows Command Prompt
        
    .. image:: ../blogstatic/install-python/notepadpp7.png
    
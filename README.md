# 2018.05.15.SB.recap

## Instructions
If you know what you're doing. Clone the repo and run it using:

    python recap.py

If you don't know what you're doing, follow along with the instructions.

If you just want to see where this all leads without installing anything skip to the bottom.

### Checking for Git
Your computer should already have git installed. If you have a Mac press:

    cmd + space

In the box type:

    terminal

and hit enter. When the terminal pops up type:

    git

and hit enter. You should see this text:

    @:~$ git
    usage: git [--version] [--help] [-C <path>] [-c name=value]
            [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
            [-p | --paginate | --no-pager] [--no-replace-objects] [--bare]
            [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
            <command> [<args>]

This means you have Git installed. You can skip installing git and go straight to cloning the repo. Otherwise continue on to check for homebrew.

### Checking for Homebrew
In the terminal you already opened, type:

    brew

and hit enter. You should see this text:

    @:~/$ brew
    Example usage:
        brew search [TEXT|/REGEX/]
        brew info [FORMULA...]
        brew install FORMULA...
        brew update
        brew upgrade [FORMULA...]
        brew uninstall FORMULA...
        brew list [FORMULA...]

    Troubleshooting:
        brew config
        brew doctor
        brew install --verbose --debug FORMULA

    Contributing:
        brew create [URL [--no-fetch]]
        brew edit [FORMULA...]

    Further help:
        brew commands
        brew help [COMMAND]
        man brew
        https://docs.brew.sh

This means you have Homebrew installed. You can skip instaling homebrew and go straight to installing git. Otherwise continue to installing homebrew.

### Installing Homebrew
In the terminal type:

    xcode-select --install

and hit enter. This will install command line developer tools onto your computer. Next type:

    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

and hit enter. This will install homebrew on your computer which is a Mac package manager.

### Installing Git
In the terminal type:

    brew install git

and hit enter. This should download git.

### Cloning the Repo
In the terminal type:

    git clone https://github.com/rchui/2018.05.15.SB.recap.git

and hit enter. Change directories into the repo by typing:

    cd 2018.05.15.SB.recap/

and hit enter. You can run the program by typing:

    python recap.py

and hit enter.

### Delete the Repo
In the terminal type:

    cd ../

and hit enter. Then type:

    rm -rf 2018.05.15.SB.recap/

and hit enter. It's should be gone!

### If Nothing Works
It should have printed:

      ******** *******  ** ********** ******       **     **       **       ******** *******    ********
     **////// /**////**/**/////**/// /*////**     ****   /**      /**      /**///// /**////**  **////// 
    /**       /**   /**/**    /**    /*   /**    **//**  /**      /**      /**      /**   /** /**       
    /*********/******* /**    /**    /******    **  //** /**      /**      /******* /*******  /*********
    ////////**/**////  /**    /**    /*//// ** **********/**      /**      /**////  /**///**  ////////**
           /**/**      /**    /**    /*    /**/**//////**/**      /**      /**      /**  //**        /**
     ******** /**      /**    /**    /******* /**     /**/********/********/********/**   //** ******** 
    ////////  //       //     //     ///////  //      // //////// //////// //////// //     // ////////  


           O
       `--=2=--~      -=-
        __/"\                                   ,
        '   |_                                 (_O_
                                                 3 )
                                                /"\__
                                              _|     '


    May 15, 2018 - Game Recap:


                        Arista    Spitballers

          Score             11             10

         Spirit         > 9000         > 9000

I put way more effort into this then I'd like to admit.
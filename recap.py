from __future__ import print_function
from collections import namedtuple
import time


SPITBALLER_TEXT = ['\n']
SPITBALLER_TEXT.append('  ******** *******  ** ********** ******       **     **       **       ******** *******    ********')
SPITBALLER_TEXT.append(' **////// /**////**/**/////**/// /*////**     ****   /**      /**      /**///// /**////**  **////// ')
SPITBALLER_TEXT.append('/**       /**   /**/**    /**    /*   /**    **//**  /**      /**      /**      /**   /** /**       ')
SPITBALLER_TEXT.append('/*********/******* /**    /**    /******    **  //** /**      /**      /******* /*******  /*********')
SPITBALLER_TEXT.append('////////**/**////  /**    /**    /*//// ** **********/**      /**      /**////  /**///**  ////////**')
SPITBALLER_TEXT.append('       /**/**      /**    /**    /*    /**/**//////**/**      /**      /**      /**  //**        /**')
SPITBALLER_TEXT.append(' ******** /**      /**    /**    /******* /**     /**/********/********/********/**   //** ******** ')
SPITBALLER_TEXT.append('////////  //       //     //     ///////  //      // //////// //////// //////// //     // ////////  ')
SPITBALLER_TEXT.append('\n')
SPITBALLER_TEXT.append("       O")
SPITBALLER_TEXT.append("   `--=2=--~      -=-")
SPITBALLER_TEXT.append('    __/"\                                   ,')
SPITBALLER_TEXT.append("    '   |_                                 (_O_")
SPITBALLER_TEXT.append("                                             3 )")
SPITBALLER_TEXT.append('                                            /"\__')
SPITBALLER_TEXT.append("                                          _|     '")
SPITBALLER_TEXT.append('\n')


Row = namedtuple('Row', ['Category', 'Arista', 'Spitballers'])


def recap():
    for line in SPITBALLER_TEXT:
        print(line)
        time.sleep(0.5)
    print('May 15, 2018 - Game Recap:')
    print('\n')

    teams_list = ["Arista", "Spitballers"]
    data = [
        [11, 10],
        ['> 9000', '> 9000'],
        ['']
    ]
    category_list = ['Score', 'Spirit', 'Cheers']

    row_format = "{:>15}" * (len(teams_list) + 1)
    time.sleep(0.5)
    print(row_format.format("", *teams_list))
    for category, row in zip(category_list, data):
        print()
        print(row_format.format(category, *row))
        time.sleep(0.5)
    print('\n')


if __name__ == '__main__':
    recap()

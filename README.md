propeller tools
---------------

Tools for translating games based on propeller engine.  
**Tested on "Sukimazakura to Uso no Machi" only.**

### `mpk_archiver`

MPK archive packer and unpacker. Does not convert anything by itself - it's
used only to repack files.

### `msc_compiler`

Script (de)compiler. Creates text files that look like this:

    00001501 00 05 [0, 1000, 0]
    00001509 05 00 [0, 1, "立ち並ぶビル群の合間を踊るように、白い灰雪がひらひらと舞い_r落ちていた。"]
    00001592 06 02 ["v\\SAK01500.ogv"]
    00001612 05 00 [0, 2, "【咲良】「なにが、<都会,マチ>に出れば何とかなるよ」"]
    00001674 05 00 [0, 3, "【優真】「…………」"]
    00001705 06 02 ["v\\SAK01510.ogv"]
    00001725 05 00 [0, 4, "【咲良】「どうにもならないじゃない。兄さん」"]
    00001780 05 00 [0, 5, "【優真】「……いや、だってさ」"]

...and lets you convert them back to the MSC files. After editing the script
files, you need to compile the whole thing back into MPK archive.

### Image editing

Upon request I can also implement an image converter. (There is also [the tool
written by asmodean](http://asmodean.reverse.net/pages/exmpk.html), but I'm not
sure it lets you convert images.)

### Proof it works

![2015-07-12-120022_1077x659_scrot](https://cloud.githubusercontent.com/assets/1045476/8637360/ecf2f7b8-288d-11e5-9a46-8935a9614b1e.png)

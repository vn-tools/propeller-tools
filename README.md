propeller tools
---------------

Tools for translating games based on propeller engine.  
**Tested on "Sukimazakura to Uso no Machi" only.**

### `mpk_archiver`

MPK archive packer and unpacker. Does not convert anything by itself - it's
used only to repack files.

### `msc_compiler`

Script (de)compiler. Creates text files that look like this:

    00 05 [0, 1000, 0]
    05 00 [0, 1, "立ち並ぶビル群の合間を踊るように、白い灰雪がひらひらと舞い_r落ちていた。"]
    06 02 ["v\\SAK01500.ogv"]
    05 00 [0, 2, "【咲良】「なにが、<都会,マチ>に出れば何とかなるよ」"]
    05 00 [0, 3, "【優真】「…………」"]
    06 02 ["v\\SAK01510.ogv"]
    05 00 [0, 4, "【咲良】「どうにもならないじゃない。兄さん」"]
    05 00 [0, 5, "【優真】「……いや、だってさ」"]

...and lets you convert them back to the MSC files. After editing the script
files, you need to compile the whole thing back into MPK archive.

### `mgr_converter`

MGR image container packer and unpacker. One MGR can hold multiple bitmaps. The
images appear to be simple BMP files, but **they contain actual alpha channel**
which is quite rare for BMP file format, so be sure to pick an image editor
that supports it.

### Proof it works

Changing dialogs:

![2015-07-12-120022_1077x659_scrot](https://cloud.githubusercontent.com/assets/1045476/8637360/ecf2f7b8-288d-11e5-9a46-8935a9614b1e.png)

Changing images (the choice of Lucky Star screencap to replace a menu item
wasn't my brightest idea, but that's all I had at the moment):

![2015-07-16-231035_194x197_scrot](https://cloud.githubusercontent.com/assets/1045476/8735288/fbd7a942-2c0f-11e5-86b8-ecd6973a4ba1.png)

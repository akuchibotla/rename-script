Rename Script
=============
Anand Kuchibotla

This is an extremely easy basic batch rename script that can be used to rename all files within a certain folder sequentially.

Features
--------
- Preserves file-extentions even when multiple types of files are within the same folder
- Allows for optional prefixes and suffixes

Usage
-----
- When you want to rename every file within a folder in numeric order as they are already named:
python rename-script.py ~/Folder

- When you want to add a prefix to each rename
python rename-script.py ~/Folder prefix

- When you want to add a suffix to each rename
python rename-script.py '' suffix

- When you want to add a prefix and a suffix to each rename
python rename-script.py prefix suffix

Example
-------
Note: This is an exaggerated example to show the power of the tool. In actual usage, the folder would be renamed in an alphabetical sequence, not in an arbitrary order as in this example.

Given a folder as chaotic as this:

Folder
- DCIM_0.PNG
- DCIM_1.PNG
- DCIM_2.PNG
- DCIM_3.PNG
- DSC_827026_A2B310.JPEG
- DSC_2221.JPEG
- DCIM_4.PNG
- IMG_030011_4213515.BMP
- DCIM_5.PNG
- DCIM_6.PNG
- DSC_8026_39BAEO.JPEG
- DSC_2221.JPEG
- DCIM_7.PNG
- DCIM_8.PNG
- DCIM_9.PNG
- IMG_030011_1351535.BMP
- DCIM_10.PNG
- DCIM_11.PNG
- IMG_030011_2562725.BMP
- DCIM_12.PNG
- DSC_827026_ANEA2132.JPEG
- DSC_2221.JPEG
- DCIM_13.PNG
- DCIM_14.PNG
- DCIM_15.PNG
- DCIM_16.PNG
- IMG_030011_6437275.BMP
- DCIM_17.PNG
- DSC_827026_FNWK20.JPEG
- DSC_2221.JPEG
- DCIM_18.PNG
- DCIM_19.PNG
- DCIM_20.PNG
    
  Simply running "python rename-script.py ~/Folder Hawaii_Trip_ _Photos" will result in a much cleaner looking folder:
  
  Folder
- Hawaii_Trip_0_Photos.PNG
- Hawaii_Trip_1_Photos.PNG
- Hawaii_Trip_2_Photos.PNG
- Hawaii_Trip_3_Photos.PNG
- Hawaii_Trip_4_Photos.JPEG
- Hawaii_Trip_5_Photos.JPEG
- Hawaii_Trip_6_Photos.PNG
- Hawaii_Trip_7_Photos.BMP
- Hawaii_Trip_8_Photos.PNG
- Hawaii_Trip_9_Photos.PNG
- Hawaii_Trip_10_Photos.JPEG
- Hawaii_Trip_11_Photos.JPEG
- Hawaii_Trip_12_Photos.PNG
- Hawaii_Trip_13_Photos.PNG
- Hawaii_Trip_14_Photos.PNG
- Hawaii_Trip_15_Photos.BMP
- Hawaii_Trip_16_Photos.PNG
- Hawaii_Trip_17_Photos.PNG
- Hawaii_Trip_18_Photos.BMP
- Hawaii_Trip_19_Photos.PNG
- Hawaii_Trip_20_Photos.JPEG
- Hawaii_Trip_21_Photos.JPEG
- Hawaii_Trip_22_Photos.PNG
- Hawaii_Trip_23_Photos.PNG
- Hawaii_Trip_24_Photos.PNG
- Hawaii_Trip_25_Photos.PNG
- Hawaii_Trip_26_Photos.BMP
- Hawaii_Trip_27_Photos.PNG
- Hawaii_Trip_28_Photos.JPEG
- Hawaii_Trip_29_Photos.JPEG
- Hawaii_Trip_30_Photos.PNG
- Hawaii_Trip_31_Photos.PNG
- Hawaii_Trip_32_Photos.PNG
    
No further development for this script is planned unless specifically requested.

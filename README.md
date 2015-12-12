<h1>Prerequisites</h1>
Requires Python 3.4+  

<h1>Help</h1>
Image Board Downloader (Fri Dec 11 21:52:52 EST 2015)  
ibdl [OPTION] URL OUTPUTDIR  
The default action is to identify every anchor found at URL whose reference contains an  
image extension type, and download it to OUTPUTDIR.  
-e [TODO] Extension list in the form of ext1,ext2...  
-h [TODO] Show request headers

<h1>Usage on Linux:  </h1>
<ul>
<li>Satisfy Python 3.4+ prerequisite</li>
<li>Clone repo</li>
<li>Edit `~/.bashrc` (Debian) or `~/.profile` (Ubuntu/Mint) to include `alias ibdl='python /path/to/ib_dler.py'`</li>
<li>To apply changes: `source [~/.bashrc|~/.profile]</li>
</ul>

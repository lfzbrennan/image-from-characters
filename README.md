<h1>Image From Characters</h1>
Turns an image into an image built from command line characters. See ./examples from example transformation. create.py creates a transformed image and also prints out the image using command line characters. Image is first transformed into an image with edges using Pytorch HED, then transformed into an image made up of characters using a simple regression algorithm on sorted blocks. 
<br>
<h2>Input</h2>
<img src="./examples/bob.jpg">
<br>
<h2>Output</h2>
<img src="./examples/out.jpg">
<br>

        +4w~,||"~,w|"~___+l_ _,_ __               
       | __  ______:_  `    `   `` 4              
        m```^ww|``  `"*="`=m=""*mmw |             
      hh @  !*",   :  _   _ ~    >=lh             
    ,` |_   h  ,f` hi,   ^h h| ~| _l4             
    #.mb[hl u,,[""|.``h  ` " `` `w`k7             
   _h`# `f  `@@`/ *^^~,\ `i*"~ |   h|             
   `  t   l  o@  `     l`'    `,   l|        _,   
  ) ` u + |i ="='   _w~ 6 ___   ^  |4        ` |  
  kh  ="7 ||   h    mwwim "`=      ih       h#|   
  |.,  "  |!   h    v  #m|   l  h  f7      im)    
   ub   _ `h   -__  bmwi4|w_w       '    :wh |    
       !a|     = [`\^a/a" 4>/_~`          ^ ._:   
    h| ] n h   h"w#_\,^v-^_:=_/`># h     x`."b|   
    hb i d h   =e`\_ _~  __i~ _+ ' hi    \= g     
    ` m]www'    "h.)"    ||==e _/   i    =m_f|    
     ' ""i`ui    u_+,_   `~=  f    .      |i/     
         | i     d`=__``ee``  | _ |      fh       
         < mh    h   `i"#|"" " !m@|h     v/       
      _` =_"k    k    i~$|"~   / `|     ~f        
       hi ` k    f    "``|,*"    !| _   _v        
       l& ,ml  _ iww~__  )|    " `# ."_"h         
       ` "w m~;m  h"=ba@ll        h/h `!v         
        ,~"@"h`mw _`~`_`o`    |       _i          
       |   ` @ /`|wm_____m    |w"  ,hh            
       =  l  @|__`"w@@@@@m     `   mm"            
       h  i4|w/jb~:wwwwmw~~w:,:~~`h               
       |`| mm# |__  ||. |  :  ___ "               
        ||"~,||  `~_`1/l^/]`_" __h                
         #2___`e]]]]_]] ^ `1[`[[ 4                
         ){]e|`mmww {mmv  @m4tmml|                
         t| "` """* ===._,~*"***ai                
         i^w__         \_`     __|                
        i"|f_bm___~wwm~ww@@@@]][[|                
        h  i im==wh"   ` ="mh|                    
        h,`h _"~~^_     = `|a                     
         h=_  |_~"       h|                       
        _ h    f         v|                       
        `==   |l          |                       
              |`          i                       
              |           i                       
              )_          |                       
              )l         _|                       
              |_         "  $|                    
                 _l       _  |                    
               _ |n       w "                     
               "                                  
                                                  
              
<br>
<hr>
Example usage:
<code>
python3 create.py -i ./examples/bob.jpg -o ./examples/out.jpg -d True -n 50 -e True 
</code>

Use <code>
python3 create.py --help
</code>
for list of command line arguments

Note: since this algorithm uses a PyTorch based edging model, the model must be downloaded from https://github.com/sniklaus/pytorch-hed

run.py and ttf2png are adapted/forked from https://github.com/sniklaus/pytorch-hed and https://github.com/sl2/TTF-to-PNG respectively
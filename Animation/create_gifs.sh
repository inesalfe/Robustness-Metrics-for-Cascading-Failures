#!/bin/sh

convert -delay 100 -loop 0 $(ls -1 Animation/Figures/ba_0_*.png | sort -V) Animation/Gifs/ba_0.gif

convert -delay 100 -loop 0 $(ls -1 Animation/Figures/ba_1_*.png | sort -V) Animation/Gifs/ba_1.gif

convert -delay 100 -loop 0 $(ls -1 Animation/Figures/ba_2_*.png | sort -V) Animation/Gifs/ba_2.gif

convert -delay 100 -loop 0 $(ls -1 Animation/Figures/ba_3_*.png | sort -V) Animation/Gifs/ba_3.gif

convert -delay 100 -loop 0 $(ls -1 Animation/Figures/dms_0_*.png | sort -V) Animation/Gifs/dms_0.gif

convert -delay 100 -loop 0 $(ls -1 Animation/Figures/dms_1_*.png | sort -V) Animation/Gifs/dms_1.gif

convert -delay 100 -loop 0 $(ls -1 Animation/Figures/dms_2_*.png | sort -V) Animation/Gifs/dms_2.gif

convert -delay 100 -loop 0 $(ls -1 Animation/Figures/dms_3_*.png | sort -V) Animation/Gifs/dms_3.gif

convert -delay 100 -loop 0 $(ls -1 Animation/Figures/small_0_*.png | sort -V) Animation/Gifs/small_0.gif

convert -delay 100 -loop 0 $(ls -1 Animation/Figures/small_1_*.png | sort -V) Animation/Gifs/small_1.gif

convert -delay 100 -loop 0 $(ls -1 Animation/Figures/small_2_*.png | sort -V) Animation/Gifs/small_2.gif

convert -delay 100 -loop 0 $(ls -1 Animation/Figures/small_3_*.png | sort -V) Animation/Gifs/small_3.gif
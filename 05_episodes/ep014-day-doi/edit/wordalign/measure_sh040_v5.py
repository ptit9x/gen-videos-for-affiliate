import numpy as np
from PIL import Image
from scipy import ndimage

EP = "/home/hatch/workspace/gen-videos-for-affiliate-git/05_episodes/ep014-day-doi"
for t in (1, 4, 7):
    im = Image.open(f"{EP}/edit/qc-frames/sh040-m{t}.png").convert("RGB")
    a = np.asarray(im).astype(float)
    lum = a.mean(axis=2)
    ycbcr = np.asarray(im.convert("YCbCr")).astype(int)
    Y, Cb, Cr = ycbcr[...,0], ycbcr[...,1], ycbcr[...,2]
    skin = (Cr>=133)&(Cr<=173)&(Cb>=77)&(Cb<=127)&(Y>90)
    # FACE, wider box x200-460 y380-570
    z = np.zeros_like(skin); z[380:570, 200:460] = True
    m = skin & z
    lab, n = ndimage.label(m)
    sizes = ndimage.sum_labels(m, lab, range(1, n+1))
    k = int(np.argmax(sizes)) + 1
    ys, xs = np.where(lab == k)
    print(f"t={t}: FACE(wide) blob {len(xs)}px bbox x{xs.min()}-{xs.max()} y{ys.min()}-{ys.max()} "
          f"bbox_cx={(xs.min()+xs.max())/2:.0f} centroid=({xs.mean():.0f},{ys.mean():.0f})")
    # HAIR TOP: dark lum<60, x150-500, y200-450, largest blob top
    hair = (lum < 60)
    z2 = np.zeros_like(hair); z2[200:450, 150:500] = True
    m2 = hair & z2
    lab2, n2 = ndimage.label(m2)
    sizes2 = ndimage.sum_labels(m2, lab2, range(1, n2+1))
    k2 = int(np.argmax(sizes2)) + 1
    ys2, xs2 = np.where(lab2 == k2)
    print(f"     HAIR-TOP blob bbox x{xs2.min()}-{xs2.max()} y{ys2.min()}-{ys2.max()} (top y={ys2.min()})")
    # CUP+SAUCER: dark lum<70, x200-480 y850-1030, largest blob
    cup = (lum < 70)
    z3 = np.zeros_like(cup); z3[850:1030, 200:480] = True
    m3 = cup & z3
    lab3, n3 = ndimage.label(m3)
    sizes3 = ndimage.sum_labels(m3, lab3, range(1, n3+1))
    k3 = int(np.argmax(sizes3)) + 1
    ys3, xs3 = np.where(lab3 == k3)
    print(f"     CUP blob {len(xs3)}px bbox x{xs3.min()}-{xs3.max()} y{ys3.min()}-{ys3.max()} (bottom y={ys3.max()})")
    # HAND bottom: skin in x200-480 y800-1100, lowest skin pixel
    z4 = np.zeros_like(skin); z4[800:1100, 200:480] = True
    m4 = skin & z4
    ys4, xs4 = np.where(m4)
    print(f"     HAND skin y range {ys4.min()}-{ys4.max()} x {xs4.min()}-{xs4.max()} (lowest skin y={ys4.max()})")

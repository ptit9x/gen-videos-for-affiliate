import numpy as np
from PIL import Image, ImageDraw
from scipy import ndimage

EP = "/home/hatch/workspace/gen-videos-for-affiliate-git/05_episodes/ep014-day-doi"
for t in (1, 4, 7):
    im = Image.open(f"{EP}/edit/qc-frames/sh040-m{t}.png").convert("RGB")
    a = np.asarray(im).astype(float)
    lum = a.mean(axis=2)
    # --- My's hair: darkest mass, lum<60, zone x150-520 y180-650 ---
    hair = (lum < 60)
    zone = np.zeros_like(hair); zone[180:650, 150:520] = True
    m = hair & zone
    lab, n = ndimage.label(m)
    sizes = ndimage.sum_labels(m, lab, range(1, n+1))
    k = int(np.argmax(sizes)) + 1
    ys, xs = np.where(lab == k)
    print(f"t={t}: HAIR blob {len(xs)}px bbox x{xs.min()}-{xs.max()} y{ys.min()}-{ys.max()} "
          f"cx={(xs.min()+xs.max())/2:.0f} cy={(ys.min()+ys.max())/2:.0f}")
    # --- face skin: tight zone under hair, x hair_xmin-10..hair_xmax+10, y hair_ymax..+230 ---
    ycbcr = np.asarray(im.convert("YCbCr")).astype(int)
    Y, Cb, Cr = ycbcr[...,0], ycbcr[...,1], ycbcr[...,2]
    skin = (Cr>=133)&(Cr<=173)&(Cb>=77)&(Cb<=127)&(Y>90)
    x0, x1 = max(0, xs.min()-10), min(720, xs.max()+10)
    y0, y1 = ys.max(), min(1280, ys.max()+230)
    z2 = np.zeros_like(skin); z2[y0:y1, x0:x1] = True
    m2 = skin & z2
    lab2, n2 = ndimage.label(m2)
    if n2:
        sizes2 = ndimage.sum_labels(m2, lab2, range(1, n2+1))
        k2 = int(np.argmax(sizes2)) + 1
        ys2, xs2 = np.where(lab2 == k2)
        print(f"     FACE skin blob {len(xs2)}px bbox x{xs2.min()}-{xs2.max()} y{ys2.min()}-{ys2.max()} "
              f"centroid=({xs2.mean():.0f},{ys2.mean():.0f}) bbox_cx={(xs2.min()+xs2.max())/2:.0f}")
    # --- Tri shoulder/head: dark mass contiguous to right edge, per 20px band y270-1080 ---
    print("     shoulder/head left edge (dark mass touching right edge x=719) per 20px band:")
    edges = []
    for yb in range(270, 1080, 20):
        band = lum[yb:yb+20, 400:720]
        dark = band < 70
        # fraction dark per column, then leftmost col where this col AND the stretch to 719 is >=60% dark
        colfrac = dark.mean(axis=0)
        e = None
        for i in range(320):
            if colfrac[i:].mean() >= 0.6 and colfrac[i] > 0.5:
                e = 400 + i
                break
        edges.append((yb, e))
    emin = min(e for _, e in edges if e is not None)
    print(f"     edges: {edges}")
    print(f"     MIN edge: x={emin}")
# --- grid overlay on t=4 for visual numeric read ---
im = Image.open(f"{EP}/edit/qc-frames/sh040-m4.png").convert("RGB")
d = ImageDraw.Draw(im)
W, H = im.size
for x in range(0, W+1, 36):
    col = (255,0,0) if x % 180 == 0 else (255,150,150)
    d.line([(x,0),(x,H)], fill=col, width=2 if x % 180 == 0 else 1)
    d.text((x+2, 4), str(x), fill=(255,0,0))
for y in range(0, H+1, 64):
    col = (0,0,255) if y % 320 == 0 else (150,150,255)
    d.line([(0,y),(W,y)], fill=col, width=2 if y % 320 == 0 else 1)
    d.text((4, y+2), str(y), fill=(0,0,255))
im.save(f"{EP}/edit/qc-frames/sh040-m4-grid.png")
print("grid saved: edit/qc-frames/sh040-m4-grid.png (red verticals every 36px=5%W, blue horizontals every 64px=5%H)")

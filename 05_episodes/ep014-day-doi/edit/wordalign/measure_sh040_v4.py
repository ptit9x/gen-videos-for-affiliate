import numpy as np
from PIL import Image
from scipy import ndimage

EP = "/home/hatch/workspace/gen-videos-for-affiliate-git/05_episodes/ep014-day-doi"
for t in (1, 2, 4, 5.5, 7):
    im = Image.open(f"{EP}/edit/qc-frames/sh040-m{t}.png").convert("RGB")
    a = np.asarray(im).astype(float)
    lum = a.mean(axis=2)
    ycbcr = np.asarray(im.convert("YCbCr")).astype(int)
    Y, Cb, Cr = ycbcr[...,0], ycbcr[...,1], ycbcr[...,2]
    skin = (Cr>=133)&(Cr<=173)&(Cb>=77)&(Cb<=127)&(Y>90)
    # --- FACE: tight box x200-380 y380-570 (face as read off the grid) ---
    z = np.zeros_like(skin); z[380:570, 200:380] = True
    m = skin & z
    lab, n = ndimage.label(m)
    sizes = ndimage.sum_labels(m, lab, range(1, n+1)) if n else []
    k = int(np.argmax(sizes)) + 1 if n else 0
    ys, xs = np.where(lab == k) if k else ([], [])
    fcx = (xs.min()+xs.max())/2 if len(xs) else None
    print(f"t={t}: FACE skin blob {len(xs)}px bbox x{xs.min()}-{xs.max()} y{ys.min()}-{ys.max()} "
          f"bbox_cx={fcx:.0f} centroid_x={xs.mean():.0f} centroid_y={ys.mean():.0f}")
    # --- SHOULDER: leftmost x where a 15px window is >=80% dark (lum<70) AND [x+15,719] is >=50% dark ---
    edges = {}
    for yb in range(280, 1080, 40):
        band = lum[yb:yb+40, 380:720]
        dark = band < 70
        colfrac = dark.mean(axis=0)
        e = None
        for i in range(0, 340-15):
            win = colfrac[i:i+15].mean()
            rest = colfrac[i+15:].mean()
            if win >= 0.8 and rest >= 0.5:
                e = 380 + i
                break
        edges[yb] = e
    print(f"     shoulder edge (15px win>=80% dark, rest>=50%): {edges}")
    print(f"     edge at bottom y1000-1080: {[edges[y] for y in (1000,1040)]}")
